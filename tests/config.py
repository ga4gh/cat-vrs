# Import core Python modules
import json
import re

# Import modules installed as dependencies (via .requirements.txt)
from jsonschema import Draft202012Validator
from pathlib import Path
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

# Define directory paths for schemas, tests, and examples
root_path = Path(__file__).parents[1]
schema_path = root_path / "schema"
catvrs_schema_path = schema_path / "cat-vrs"
test_path = root_path / 'tests'
fixtures_path = root_path / 'examples'

ga4gh_re = re.compile(r'.*\/ga4gh\/schema\/([\w\-\.]+)\/[\w\.]+\/(.*)$')

def retrieve_rel_ref(ga4gh_ref: str) -> Resource:
    """
    Retrieves a schema from an imported submodule (currently gks-core and vrs).

    Args:
    ga4gh_reference (str): A regex string to identify these imported schemas
        Question: cat-vrs-source.yaml contains these lines, which the regex is finding, I think
            namespaces:
                gks.core: /ga4gh/schema/gks-core/1.0.0/json/
                vrs: /ga4gh/schema/vrs/2.0.1/json/
        Is this finding the path from the cat-vrs repo? Or is this importing from elsewhere?
        I'm having trouble grasping what exactly the referencing module is doing.

    Returns:
        Resource: The schema resource

    Raises:
        ValueError: If the referenced schema is not found.
    """

    # Regular expression to identify submodules (I think?)
    # PyCharm thinks that the \ is a redundant regex character, may revisit that.

    ga4gh_match = ga4gh_re.match(ga4gh_ref)
    if ga4gh_match is None:
        raise ValueError(f'ga4gh_reference {ga4gh_ref} is not a root GA4GH reference')

    schema_module = ga4gh_match.group(1)
    local_path = ga4gh_match.group(2)
    resolved_path = (schema_path / schema_module / local_path).resolve()
    schema = json.loads(resolved_path.read_text())
    return Resource.from_contents(schema)

js_registry = Registry(
    # In the VA-spec example, they do not pass any arguments when providing
    # the retrieve_rel_ref (or retrieve_relative_reference) function
    retrieve=retrieve_rel_ref
)
js_def = dict()
validator = dict()
coverage = dict()

# Loop over schema paths
# Isn't this double evaluating some paths?
paths = []
paths.extend(list(schema_path.glob('*/json/*')))
paths.extend(list(catvrs_schema_path.glob('*/json/*')))

def assess_schema_coverage(coverage_dictionary, name, property_name, property_definition):
    """
    Loops through all properties of a schema and assesses their typing, I think

    Args:
        coverage_dictionary (dict): The coverage dictionary for the provided schema
        name (str): The name of the schema
        property_name (str): The name of the property being evaluated
        property_definition (dict): The definition of the schema property

    Returns:
        coverage_dictionary (dict): The coverage dictionary for the provided schema, with `property_name` detailed populated
    """
    if coverage_dictionary.get(property_name, None) is False:
        # What is this doing? Is it looking to see if a property has already been evaluated?
        # Since this function loops on itself, I think so
        return coverage
    elif 'oneOf' in property_definition:
        for element in property_definition['oneOf']:
            assess_schema_coverage(
                coverage_dictionary=coverage_dictionary,
                name=name,
                # It would be nice to have a better way to label these nested elements for traceback purposes
                property_name=property_name,
                property_definition=element
            )
    elif 'anyOf' in property_definition:
        for element in property_definition['anyOf']:
            assess_schema_coverage(
                coverage_dictionary=coverage_dictionary,
                name=name,
                property_name=property_name,
                property_definition=element
            )
    elif '$ref' in property_definition and property_definition['$ref'].endswith('iriReference'):
        return coverage
    elif '$ref' in property_definition:
        coverage_dictionary[property_name] = False
    elif 'type' not in property_definition:
        raise ValueError(f'schema property {name}.{property_name} has no type')
    elif isinstance(property_definition['type'], list):
        coverage_dictionary[property_name] = False
    elif property_definition['type'] in ['array', 'boolean', 'integer', 'number', 'string']:
        coverage_dictionary[property_name] = False
    elif property_definition['type'] == 'object' and property_definition.get('additionalProperties', None) is True:
        coverage_dictionary[property_name] = False
    else:
        raise ValueError(f'schema class property {name}.{property_name}: {property_definition} ({property_definition['type']}) not handled')
    return coverage


for schema_path in paths:
    schema_name = schema_path.name
    schema_content = json.loads(schema_path.read_text())
    schema_uri = schema_path.as_uri()
    schema_content['id'] = schema_uri
    schema_resource = Resource(contents=schema_content, specification=DRAFT202012)
    js_def[schema_path.name] = schema_content
    js_registry = js_registry.with_resources([
        (schema_path.name, schema_resource),
        (schema_uri, schema_resource)
    ])

    # Perform testing against schema
    validator[schema_name] = Draft202012Validator(js_def[schema_name], registry=js_registry)

    # for schema_class, class_definition in js_def.items():
    # schema_class translates to schema_name, class_definitions translates to schema_content
    schema_coverage = dict()
    if 'properties' not in schema_content:
        continue

    for schema_property, schema_property_definition in schema_content['properties'].items():
        # va-spec has some schema properties that have a maturity level associated with them
        # for example: https://github.com/ga4gh/va-spec/blob/7a2bc8bf7e27933dd9d43b4d3b0749d42be800ee/schema/va-spec/base/json/CohortAlleleFrequencyStudyResult#L75-L80
        # cat-vrs does _not_ currently have maturity associated with any properties, but we will
        # leave this check
        if schema_property_definition.get('maturity', '') == 'draft':
            continue

        # Check for coverage of this property
        schema_coverage = assess_schema_coverage(
            coverage_dictionary=schema_coverage,
            name=schema_name,
            property_name=schema_property,
            property_definition=schema_property_definition
        )
    coverage[schema_name] = schema_coverage

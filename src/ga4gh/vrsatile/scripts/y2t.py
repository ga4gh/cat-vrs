#!/usr/bin/env python3
"""convert input .yaml to .rst artifacts"""

import yaml
import os
import sys
import pathlib
from inflector import Inflector
from ga4gh.vrsatile.tools.source_proc import SCHEMA_DEF_KEYWORD_BY_VERSION, \
    YamlSchemaProcessor

source_file = pathlib.Path(sys.argv[1])

defs_path = pathlib.Path.cwd() / 'defs' / str(source_file.stem)[:-7]
os.makedirs(defs_path)  # error expected if directory already exists – clear with Make

with open(source_file, 'r') as f:
    schema = yaml.load(f, Loader=yaml.SafeLoader)

i = Inflector()
proc_schema = YamlSchemaProcessor(schema)
if proc_schema.defs is None:
    exit(0)
schema_def_keyword = SCHEMA_DEF_KEYWORD_BY_VERSION[schema['$schema']]


def resolve_curie(curie):
    namespace, identifier = curie.split(':')
    base_url = schema['namespaces'][namespace]
    return base_url + identifier


def resolve_type(class_property_definition):
    if 'type' in class_property_definition:
        if class_property_definition['type'] == 'array':
            return resolve_type(class_property_definition['items'])
        return class_property_definition['type']
    elif '$ref_curie' in class_property_definition:
        curie = class_property_definition['$ref_curie']
        identifier = curie.split(':')[-1]
        return f'`{identifier} <{resolve_curie(curie)}>`_'
    elif '$ref' in class_property_definition:
        ref = class_property_definition['$ref']
        identifier = ref.split('/')[-1]
        if ref.startswith('#'):
            return f':ref:`{identifier}`'
        else:
            return f'`{identifier} <{ref}>`_'
    elif 'oneOf' in class_property_definition:
        deprecated_types = class_property_definition.get('deprecated', list())
        resolved_deprecated = list()
        resolved_active = list()
        for property_type in class_property_definition['oneOf']:
            resolved_type = resolve_type(property_type)
            if property_type in deprecated_types:
                resolved_deprecated.append(resolved_type + f' (deprecated)')
            else:
                resolved_active.append(resolved_type)
        return ' | '.join(resolved_active + resolved_deprecated)
    else:
        raise ValueError(class_property_definition)


def resolve_cardinality(class_property_name, class_property_attributes, class_definition):
    """Resolve class property cardinality from yaml definition"""
    if class_property_name in class_definition.get('required', []):
        min_count = '1'
    elif class_property_name in class_definition.get('heritable_required', []):
        min_count = '1'
    else:
        min_count = '0'
    if class_property_attributes.get('type') == 'array':
        max_count = class_property_attributes.get('maxItems', 'm')
        min_count = class_property_attributes.get('minItems', 0)
    else:
        max_count = '1'
    return f'{min_count}..{max_count}'


def get_ancestor_with_attributes(class_name):
    if proc_schema.class_is_passthrough(class_name):
        ancestor = list(proc_schema.dependency_map[class_name])[0]
        return get_ancestor_with_attributes(ancestor)
    return class_name


for class_name, class_definition in proc_schema.defs.items():
    with open(defs_path / (class_name + '.rst'), "w") as f:
        print("**Computational Definition**\n", file=f)
        print(class_definition['description'], file=f)
        if proc_schema.class_is_passthrough(class_name):
            continue
        if 'heritable_properties' in class_definition:
            p = 'heritable_properties'
        elif 'properties' in class_definition:
            p = 'properties'
        elif proc_schema.class_is_primitive(class_name):
            continue
        else:
            raise ValueError(class_name, class_definition)
        deps = list(proc_schema.dependency_map[class_name])
        if len(deps) == 1:
            ancestor = get_ancestor_with_attributes(deps[0])
            inheritance = f"\nSome {class_name} attributes are inherited from :ref:`{ancestor}`.\n"
        elif len(deps) == 0:
            inheritance = ""
        else:
            raise ValueError
        print(f"""
**Information Model**
{inheritance}
.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description""", file=f)
        for class_property_name, class_property_attributes in class_definition[p].items():
            print(f"""\
   *  - {class_property_name}
      - {resolve_type(class_property_attributes)}
      - {resolve_cardinality(class_property_name, class_property_attributes, class_definition)}
      - {class_property_attributes.get('description', '')}""", file=f)

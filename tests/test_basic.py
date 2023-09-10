import json

from jsonschema import validate
import yaml
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import catvar_json_path, catvar_yaml_path, catvar_merged_yaml_path, fixtures_path, test_path, get_schema_ref

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(catvar_yaml_path)
j = json.load(open(catvar_json_path))
m = yaml.safe_load(open(catvar_merged_yaml_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


def test_examples():
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)
    for test in test_spec['tests']:
        with open(fixtures_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        schema = get_schema_ref(
            test['schema'],
            test['definition'],
            test.get('kw', '$defs')
        )
        assert validate(data, schema) is None
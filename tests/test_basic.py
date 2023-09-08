import json

import python_jsonschema_objects as pjs
import yaml
from schema.helpers import pjs_filter
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import catvar_json_path, catvar_yaml_path, catvar_merged_yaml_path

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(catvar_yaml_path)
j = json.load(open(catvar_json_path))
m = yaml.safe_load(open(catvar_merged_yaml_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"

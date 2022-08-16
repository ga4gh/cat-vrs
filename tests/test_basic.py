import json

import python_jsonschema_objects as pjs
import yaml
from schema.helpers import pjs_filter
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import vod_json_path, vod_yaml_path, vod_merged_yaml_path

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(vod_yaml_path)
j = json.load(open(vod_json_path))
m = yaml.safe_load(open(vod_merged_yaml_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


# Can pjs handle this schema?
def test_pjs_smoke():
    ob = pjs.ObjectBuilder(pjs_filter(m))
    assert ob.build_classes()              # no exception => okay

#!/usr/bin/env python3

import yaml
import sys
from ga4gh.vrsatile.tools.source_proc import YamlSchemaProcessor

raw_schema = yaml.load(sys.stdin, Loader=yaml.SafeLoader)
p = YamlSchemaProcessor(raw_schema)
p.js_yaml_dump(sys.stdout)

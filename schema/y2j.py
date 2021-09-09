#!/usr/bin/env python3
"""convert yaml on stdin to json on stdout"""
import copy
import json
import sys
import yaml
from collections import defaultdict

raw_schema = yaml.load(sys.stdin, Loader=yaml.SafeLoader)

processed_schema = copy.deepcopy(raw_schema)

del (processed_schema['namespaces'])

dependency_map = defaultdict(set)
defs = processed_schema['$defs']
for schema_class in defs:
    if 'heritable_properties' in defs[schema_class]:
        assert 'oneOf' in defs[schema_class]  # Expected schema pattern
        refs = [item['$ref'].split('/')[-1] for item in defs[schema_class]['oneOf'] if '$ref' in item]
        for ref in refs:
            dependency_map[ref].add(schema_class)


def class_is_abstract(schema_class):
    one_of_items = raw_schema['$defs'][schema_class].get('oneOf', [])
    if len(one_of_items) > 0 and '$ref' in one_of_items[0]:
        return True
    return False


def resolve_curie(curie):
    namespace, identifier = curie.split(':')
    base_url = raw_schema['namespaces'][namespace]
    return base_url + identifier


def process_property_tree(raw_node, processed_node):
    if isinstance(raw_node, dict):
        for k, v in raw_node.items():
            if k.endswith('_curie'):
                new_k = k[:-6]
                processed_node[new_k] = resolve_curie(v)
                del(processed_node[k])
            else:
                process_property_tree(raw_node[k], processed_node[k])
    elif isinstance(raw_node, list):
        for raw_item, processed_item in zip(raw_node, processed_node):
            process_property_tree(raw_item, processed_item)
    return


def process_schema_class(schema_class):
    raw_class_def = raw_schema['$defs'][schema_class]
    if schema_class in processed_classes:
        return
    processed_class_def = processed_schema['$defs'][schema_class]
    inherited_properties = dict()
    inherited_required = set()
    # The below assertion is in place to limit support to single inheritance.
    # This can be changed to multiple inheritance very readily if we add a
    # mechanism for indicating preference for overlapping attributes.
    # That functionality is not needed at this time.
    assert len(dependency_map[schema_class]) <= 1
    for dependency in dependency_map[schema_class]:
        process_schema_class(dependency)
        processed_dependency = processed_schema['$defs'][dependency]
        inherited_properties |= processed_dependency['heritable_properties']
        inherited_required |= set(processed_dependency['heritable_required'])
    if class_is_abstract(schema_class):
        prop_k = 'heritable_properties'
        req_k = 'heritable_required'
    else:
        prop_k = 'properties'
        req_k = 'required'
    raw_class_properties = raw_class_def[prop_k]  # Nested inheritance!
    processed_class_properties = processed_class_def[prop_k]
    processed_class_required = set(processed_class_def.get(req_k, []))
    process_property_tree(raw_class_properties, processed_class_properties)
    # Mix in inherited properties
    processed_class_def[prop_k] = inherited_properties | processed_class_properties
    processed_class_def[req_k] = list(inherited_required | processed_class_required)
    processed_classes.add(schema_class)


processed_classes = set()
heritable_properties = dict()
for schema_class in defs:
    process_schema_class(schema_class)
for schema_class in defs:
    if class_is_abstract(schema_class):
        del defs[schema_class]['heritable_properties']
        del defs[schema_class]['heritable_required']
        del defs[schema_class]['header_level']

json.dump(processed_schema, sys.stdout, indent=3, sort_keys=False)

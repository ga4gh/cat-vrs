#!/usr/bin/env python3
"""convert vrsatile.yaml to .rst artifacts"""

import yaml
import os
import pathlib
from inflector import Inflector

SECTION_DELIMITER = '#'

defs_path = pathlib.Path.cwd() / 'defs'
os.mkdir(defs_path)  # error expected if directory already exists – clear with Make

with open('vrsatile.yaml', 'r') as f:
    schema = yaml.load(f, Loader=yaml.SafeLoader)

i = Inflector()


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
        return f'`{identifier} <{ref}>`_'
    elif 'oneOf' in class_property_definition:
        return ' | '.join([resolve_type(x) for x in class_property_definition['oneOf']])
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
        max_count = 'm'
    else:
        max_count = '1'
    return f'{min_count}..{max_count}'


for class_name, class_definition in schema['$defs'].items():
    with open(defs_path / (class_name + '.rst'), "w") as f:
        header = i.titleize(class_name)
        ref = i.underscore(class_name)
        print(header, file=f)
        print(SECTION_DELIMITER * len(header), file=f)
        print(class_definition['description'], file=f)
        print("""
.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description""", file=f)
        if 'heritable_properties' in class_definition:
            p = 'heritable_properties'
        elif 'properties' in class_definition:
            p = 'properties'
        else:
            raise ValueError(class_name)
        for class_property_name, class_property_attributes in class_definition[p].items():
            print(f"""\
   *  - {class_property_name}
      - {resolve_type(class_property_attributes)}
      - {resolve_cardinality(class_property_name, class_property_attributes, class_definition)}
      - {class_property_attributes['description']}""", file=f)

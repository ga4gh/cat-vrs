**Computational Definition**

A compact class for representing a variation context that is a member of a Categorical Variation. It supports one or more Expressions of a Variation and optionally an associated VRS ID.

**Information Model**

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - type
      - string
      - 0..1
      - MUST be "VariationMember"
   *  - expressions
      - `Expression <Expression>`_
      - 1..m
      - 
   *  - variation_id
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_
      - 0..1
      - 

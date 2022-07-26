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
      - :ref:`Expression`
      - 1..m
      - 
   *  - variation_id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - 

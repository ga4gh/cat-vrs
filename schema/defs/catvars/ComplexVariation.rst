**Computational Definition**

A categorical variation domain jointly characterized by two or more other categorical  variation domains.

**Information Model**

Some ComplexVariation attributes are inherited from :ref:`Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "ComplexVariation".
   *  - operands
      - :ref:`CategoricalVariation`
      - 2..m
      - The :ref:`CategoricalVariation` objects that are being evaluated collectively.
   *  - operator
      - string
      - 1..1
      - The logical operation applied to evaluating the object *operands*. MUST be "AND" or "OR".

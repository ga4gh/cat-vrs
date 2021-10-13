**Computational Definition**

The ComplexVariationRule class constructs objects for defining complex logical relationships between two or more other :ref:`VariationRule` objects.

**Information Model**

Some ComplexVariationRule attributes are inherited from :ref:`VariationRule`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - _id
      - string
      - 0..1
      - A GA4GH computed identifier.
   *  - type
      - string
      - 1..1
      - MUST be "ComplexVariationRule".
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the variation rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the variation rule expression.
   *  - operands
      - :ref:`VariationRule`
      - 2..m
      - The :ref:`VariationRule` objects that are being evaluated collectively.
   *  - operator
      - string
      - 1..1
      - The logical operation applied to evaluating the object *operands*.

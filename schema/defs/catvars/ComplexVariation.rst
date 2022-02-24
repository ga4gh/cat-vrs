**Computational Definition**

A categorical variation domain jointly characterized by two or more other categorical  variation domains.

**Information Model**

Some ComplexVariation attributes are inherited from :ref:`CategoricalVariation`.

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
      - Categorical Variation Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "ComplexVariation".
   *  - complement
      - boolean
      - 1..1
      - This field indicates that a categorical variation is defined to include (false) or exclude (true) variation concepts matching the categorical variation. This is  equivalent to a logical NOT operation on the categorical variation properties.
   *  - operands
      - :ref:`CategoricalVariation`
      - 2..m
      - The :ref:`CategoricalVariation` objects that are being evaluated collectively.
   *  - operator
      - string
      - 1..1
      - The logical operation applied to evaluating the object *operands*. MUST be "AND" or "OR".

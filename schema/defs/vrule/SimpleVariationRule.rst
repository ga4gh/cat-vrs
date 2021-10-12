**Computational Definition**

The SimpleVariationRule abstract class represents the set of :ref:`VariationRule` classes that are used directly by genomic knowledge statements, or as components for defining a :ref:`ComplexVariationRule`.

**Information Model**

Some SimpleVariationRule attributes are inherited from :ref:`VariationRule`.

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
      - 1..1
      - MUST be Variation Rule class name.
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the variation rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the variation rule expression.

**Computational Definition**

A thing!

**Information Model**

Some GeneFunctionalConsequenceRule attributes are inherited from :ref:`SimpleVariationRule`.

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
      - MUST be Variation Rule class name.
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the variation rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the variation rule expression.

**Computational Definition**

The EquivalentVariationRule class constructs objects which indicate that any variation that can be "equivalently mapped" to the indicated *variation* value. The rules by which equivalency mapping is determined are managed at the implementation level, but typically involve operations such as variation projection (e.g. genomic <-> transcript <-> protein) and translation (e.g. GRCh37 genomic <-> GRCh38 genomic).

**Information Model**

Some EquivalentVariationRule attributes are inherited from :ref:`SimpleVariationRule`.

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
      - MUST be "EquivalentVariationRule".
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the variation rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the variation rule expression.
   *  - variation
      - `Variation <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Variation>`_
      - 1..1
      - The `VRS Variation <https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#variation>`_ object to which equivalency must be determined.
   *  - molecular_context
      - string
      - 1..1
      - The molecular context of the *variation* value.

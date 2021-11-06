**Computational Definition**

The CanonicalVariationRule class constructs objects which describe any variation that are congruent with the indicated *variation* value. The rules by which congruency is determined are managed at the implementation level, but typically involve operations such as variation projection (genomic <-> transcript), translation (transcript <-> protein) and liftover (e.g. GRCh37 genomic <-> GRCh38 genomic).

**Information Model**

Some CanonicalVariationRule attributes are inherited from :ref:`SimpleRule`.

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
      - MUST be "CanonicalVariationRule".
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the genomic knowledge rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the genomic knowledge rule expression.
   *  - variation
      - `Variation <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Variation>`_
      - 1..1
      - The `VRS Variation <https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#variation>`_ object to which equivalency must be determined.

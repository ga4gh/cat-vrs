**Computational Definition**

The ConsequenceFeatureRule class constructs objects which describe any variation within a *feature* resulting in the indicated *feature_consequence*.

**Information Model**

Some ConsequenceFeatureRule attributes are inherited from :ref:`SimpleRule`.

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
      - MUST be "ConsequenceFeatureRule".
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the genomic knowledge rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the genomic knowledge rule expression.
   *  - feature
      - `Feature <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Feature>`_
      - 1..1
      - A `VRS Feature <https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#feature>`_ object.
   *  - feature_consequence
      - string
      - 1..1
      - MUST be one of "gain-of-function", "loss-of-function", "oncogenic", "pathogenic".

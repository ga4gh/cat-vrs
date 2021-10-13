**Computational Definition**

The GeneConsequenceRule class constructs objects which describe any variation within a *gene* resulting in the indicated *gene_consequence*.

**Information Model**

Some GeneConsequenceRule attributes are inherited from :ref:`SimpleVariationRule`.

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
      - MUST be "GeneFunctionalConsequenceRule".
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the variation rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the variation rule expression.
   *  - gene
      - `Gene <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Gene>`_
      - 0..1
      - A `VRS Gene <https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#gene>`_ object.
   *  - gene_consequence
      - string
      - 0..1
      - 

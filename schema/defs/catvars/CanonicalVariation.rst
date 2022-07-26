**Computational Definition**

A categorical variation domain characterized by a representative Variation context  to which members lift-over, project, translate, or otherwise directly align.

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
      - 1..1
      - MUST be "CanonicalVariation".
   *  - canonical_context
      - `Variation <vrs.json#/definitions/Variation>`_
      - 0..1
      - The `VRS Variation <https://vrs.ga4gh.org/en/1.2.1/terms_and_model.html#variation>`_ object to which congruency must be determined.

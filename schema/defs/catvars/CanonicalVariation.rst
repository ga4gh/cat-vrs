**Computational Definition**

A categorical variation domain characterized by a representative Variation context  to which members lift-over, project, translate, or otherwise directly align.

**Information Model**

Some CanonicalVariation attributes are inherited from :ref:`Entity`.

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
      - MUST be "CanonicalVariation".
   *  - canonical_context
      - `Variation <vrs.json#/definitions/Variation>`_
      - 1..1
      - The `VRS Variation <https://vrs.ga4gh.org/en/1.2.1/terms_and_model.html#variation>`_ object to which congruency must be determined.

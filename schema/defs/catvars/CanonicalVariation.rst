**Computational Definition**

A categorical variation domain characterized by a representative Variation context  to which members lift-over, project, translate, or otherwise directly align.

**Information Model**

Some CanonicalVariation attributes are inherited from :ref:`CategoricalVariation`.

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
      - MUST be "CanonicalVariation".
   *  - complement
      - boolean
      - 1..1
      - This field indicates that a categorical variation is defined to include (false) or exclude (true) variation concepts matching the categorical variation. This is  equivalent to a logical NOT operation on the categorical variation properties.
   *  - variation
      - `Variation <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/Variation>`_
      - 1..1
      - The `VRS Variation <https://vrs.ga4gh.org/en/1.2.1/terms_and_model.html#variation>`_ object to which congruency must be determined.

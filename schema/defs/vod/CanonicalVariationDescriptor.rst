**Computational Definition**

This descriptor class is used for describing Canonical Variation value objects.

**Information Model**

Some CanonicalVariationDescriptor attributes are inherited from :ref:`Entity`.

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
      - string
      - 1..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
   *  - type
      - string
      - 1..1
      - MUST be "CanonicalVariationDescriptor".
   *  - label
      - string
      - 0..1
      - A primary label for the value object.
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - description
      - string
      - 0..1
      - A free-text description of the value object.
   *  - xrefs
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..m
      - List of CURIEs representing associated concepts.
   *  - alternate_labels
      - string
      - 0..m
      - List of strings representing alternate labels for the value object.
   *  - members
      - :ref:`VariationMember`
      - 0..m
      - VariationMember instances that fall within the functional domain of the Categorical Variation.
   *  - subject_variation_descriptor
      - :ref:`VariationDescriptor`
      - 0..1
      - 
   *  - canonical_variation
      - `CURIE <core.json#/$defs/CURIE>`_ | `CanonicalVariation <catvars.json#/$defs/CanonicalVariation>`_
      - 1..1
      - MUST be a `CategoricalVariation` or a CURIE reference to a `CategoricalVariation`.

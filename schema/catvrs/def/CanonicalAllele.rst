**Computational Definition**

A canonical allele is defined by an `Allele <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#variation>`  that is representative of a collection of congruent Alleles, each of which depict the same nucleic acid  change on different underlying reference sequences. Congruent representations of an Allele often exist across different genome assemblies and associated cDNA transcript representations.

    **Information Model**
    
Some CanonicalAllele attributes are inherited from :ref:`CategoricalVariation`.

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
          - 0..1
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary name for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - alternativeLabels
          - string
          - 0..m
          - Alternative name(s) for the Entity.
       *  - extensions
          - `Extension <../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - mappings
          - `ConceptMapping <../gks-common/common.json#/$defs/ConceptMapping>`_
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - members
          - `Variation <../vrs/vrs.yaml#/$defs/Variation>`_ | `IRI <../gks-common/common.yaml#/$defs/IRI>`_
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
       *  - type
          - string
          - 1..1
          - MUST be "CanonicalAllele"
       *  - definingContext
          - `Allele <../vrs/vrs.yaml#/$defs/Allele>`_ | `IRI <../gks-common/common.yaml#/$defs/IRI>`_
          - 1..1
          - The `VRS Allele <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#allele>`_ object that is congruent with variants on alternate reference sequences.

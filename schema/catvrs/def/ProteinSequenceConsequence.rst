**Computational Definition**

A change that occurs in a protein sequence as a result of genomic changes. Due to the degenerate nature of the genetic code, there are often several genomic changes that can cause a protein sequence consequence. The protein sequence consequence, like a :ref:`CanonicalAllele`, is defined by an `Allele <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#variation>` that is representative of a collection of congruent Protein Alleles that share the same altered codon(s).

    **Information Model**
    
Some ProteinSequenceConsequence attributes are inherited from :ref:`CategoricalVariation`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - mappings
          - `Mapping <../gks-common/core.json#/$defs/Mapping>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - MUST be "ProteinSequenceConsequence"
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate labels for a Domain Entity.
       *  - members
          - `Variation <../vrs/vrs.yaml#/$defs/Variation>`_ | `IRI <../gks-common/core.yaml#/$defs/IRI>`_
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
       *  - definingContext
          - `Allele <../vrs/vrs.yaml#/$defs/Allele>`_ | `IRI <../gks-common/core.yaml#/$defs/IRI>`_
          - 1..1
          - The `VRS Allele <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#allele>`_ object that is congruent with (projects to the same codons) as alleles on other protein reference  sequences.

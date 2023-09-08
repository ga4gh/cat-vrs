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
          - `Extension <core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - mappings
          - `Mapping <core.json#/$defs/Mapping>`_
          - 0..m
          - 
       *  - members
          - `Variation <vrs.json#/$defs/Variation>`_ | :ref:``
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
       *  - type
          - string
          - 1..1
          - 
       *  - definingContext
          - {'$ref': 'vrs.json#/$defs/Variation'}
          - 1..1
          - The `VRS Variation <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#variation>`_ object that is congruent with variants on alternate reference sequences.

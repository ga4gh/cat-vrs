**Computational Definition**

A categorical variation domain is defined first by a sequence derived from a canonical `Location  <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#Location>`_ , which is representative of  a collection of congruent Locations. The change or count of this sequence is also described, either by a numeric value (e.g. "3 or more copies") or categorical representation (e.g. "high-level gain").  Categorical CNVs may optionally be defined by rules specifying the location match characteristics for  member CNVs.

    **Information Model**
    
Some CategoricalCnv attributes are inherited from :ref:`CategoricalVariation`.

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
          - MUST be "CategoricalCnv"
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate labels for a Domain Entity.
       *  - members
          - `Variation <../vrs/vrs.yaml#/$defs/Variation>`_ | `IRI <../gks-common/core.yaml#/$defs/IRI>`_
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
       *  - location
          - {'$ref': '../vrs/vrs.yaml#/$defs/Location'}
          - 1..1
          - A `VRS Location <https://vrs.ga4gh.org/en/2.0/terms_and_model.html#location>`_ object that represents a sequence derived from that location, and is congruent with locations  on alternate reference sequences.
       *  - locationMatchCharacteristic
          - string
          - 0..1
          - The characteristics of a valid match between a contextual CNV location (the query) and the  Categorical CNV location (the domain), when both query and domain are represented on the same  reference sequence. An `exact` match requires the location of the query and domain to be identical.  A `subinterval` match requires the query to be a subinterval of the domain. A `superinterval` match requires the query to be a superinterval of the domain. A `partial` match requires at least 1 residue of overlap between the query and domain.
       *  - copyChange
          - string
          - 0..1
          - A representation of the change in copies of a sequence in a system. MUST be one of "efo:0030069" (complete  genomic loss), "efo:0020073" (high-level loss), "efo:0030068" (low-level loss), "efo:0030067" (loss),  "efo:0030064" (regional base ploidy), "efo:0030070" (gain), "efo:0030071" (low-level gain), "efo:0030072"  (high-level gain).
       *  - copies
          - integer | `Range <../vrs/vrs.yaml#/$defs/Range>`_
          - 0..1
          - The integral number of copies of the subject in a system.

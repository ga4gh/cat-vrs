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
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - mappings
      - `ConceptMapping </ga4gh/schema/gks-common/1.x/data-types/json/ConceptMapping>`_
      - 0..m
      - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
   *  - members
      - `Variation </ga4gh/schema/vrs/2.x/json/Variation>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..m
      - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
   *  - type
      - string
      - 1..1
      - MUST be "CategoricalCnv"
   *  - location
      - `SequenceLocation </ga4gh/schema/vrs/2.x/json/SequenceLocation>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 1..1
      - A `VRS Location <https://vrs.ga4gh.org/en/2.x/concepts/location/SequenceLocation.html>`_ object that represents a sequence derived from that location, and is congruent with locations  on alternate reference sequences.
   *  - locationMatchCharacteristic
      - string
      - 0..1
      - The characteristics of a valid match between a contextual CNV location (the query) and the  Categorical CNV location (the domain), when both query and domain are represented on the same  reference sequence. An `exact` match requires the location of the query and domain to be identical.  A `subinterval` match requires the query to be a subinterval of the domain. A `superinterval` match requires the query to be a superinterval of the domain. A `partial` match requires at least 1 residue of overlap between the query and domain.
   *  - copyChange
      - string
      - 0..1
      - A representation of the change in copies of a sequence in a system. MUST be one of "EFO:0030069" (complete  genomic loss), "EFO:0020073" (high-level loss), "EFO:0030068" (low-level loss), "EFO:0030067" (loss),  "EFO:0030064" (regional base ploidy), "EFO:0030070" (gain), "EFO:0030071" (low-level gain), "EFO:0030072"  (high-level gain).
   *  - copies
      - integer | `Range </ga4gh/schema/vrs/2.x/json/Range>`_
      - 0..1
      - The integral number of copies of the subject in a system.

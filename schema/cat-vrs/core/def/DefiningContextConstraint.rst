**Computational Definition**

The location or location-state, congruent with other reference sequences, about which categorical variation is being described.

**Information Model**

Some DefiningContextConstraint attributes are inherited from :ref:`Constraint`.

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
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - mappings
      - :ref:`ConceptMapping`
      - 0..m
      - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
   *  - description
      - string
      - 0..1
      - A textual description of the domain of variation that should match the categorical  variation entity.
   *  - label
      - string
      - 0..1
      - A primary label for the categorical variation. This required property should provide a  short and descriptive textual representation of the concept.
   *  - type
      - string
      - 1..1
      - MUST be "DefiningContextConstriant"
   *  - definingContext
      - :ref:`Variation` | :ref:`Location`
      - 1..1
      - 
   *  - relations
      - _Not Specified_
      - 0..m
      - Defined relationshis between members of the categorical variant and the defining context. ``sequence_liftover`` refers to variants or locations that represent a congruent concept on a differing assembly of a human genome (e.g. "GRCh37" and "GRCh38") or gene (e.g. Locus Reference Genomic) sequence. ``transcript_projection``  refers to variants or locations that occur on transcripts projected from the defined genomic concept. ``codon_translation``  refers to variants or locations that translate from the codon(s) represented by the defined concept.

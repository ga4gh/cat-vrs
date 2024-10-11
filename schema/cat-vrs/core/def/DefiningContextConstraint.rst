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
   *  - type
      - string
      - 1..1
      - MUST be "DefiningContextConstraint"
   *  - definingContext
      - :ref:`Variation` | :ref:`Location` | :ref:`IRI`
      - 1..1
      - 
   *  - relations
      - string
      - 0..m
      - Defined relationships between members of the categorical variant and the defining context. ``sequence_liftover`` refers to variants or locations that represent a congruent concept on a differing assembly of a human genome (e.g. "GRCh37" and "GRCh38") or gene (e.g. Locus Reference Genomic) sequence. ``transcript_projection`` refers to variants or locations that occur on transcripts projected from the defined genomic concept. ``codon_translation`` refers to variants or locations that translate from the codon(s) represented by the defined concept.

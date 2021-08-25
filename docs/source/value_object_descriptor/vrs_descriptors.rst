.. _VariationDescriptor:

Variation Descriptor
####################
This descriptor is intended as an class for describing `VRS Variation`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Variation Descriptor* has the following attributes:

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
      - MUST be "VariationDescriptor"
   *  - variation_id
      - CURIE_
      - 0..1
      - This SHOULD be provided if `variation` is omitted
   *  - variation
      - `VRS Variation`_
      - 0..1
      - This SHOULD be provided if `variation_id` is omitted
   *  - molecule_context
      - enum
      - 0..1
      - The molecular context of this variant. Must be one of
        "genomic", "transcript", or "protein".
   *  - structural_type
      - CURIE
      - 0..1
      - The structural variant type associated with this variant.
        We RECOMMEND a descendent term of `SO:0001537`_.
   *  - expressions
      - :ref:`Expression`
      - 0..m
      - Typically HGVS or ISCN nomenclature expressions. Other systems
        relevant to the description of variation MAY be used.
   *  - vcf_record
      - :ref:`VcfRecord`
      - 0..1
      - A VCF Record of the variant. This SHOULD be a single allele, the
        the VCF genotype (GT) field should be represented in the
        `allelic_state` attribute.
   *  - gene_context
      - CURIE | :ref:`GeneDescriptor`
      - 0..*
      - A specific gene context that applies to this variant.
   *  - vrs_ref_allele_seq
      - `VRS Sequence`_
      - 0..1
      - A `VRS Sequence`_ corresponding to a "ref allele", describing the
        sequence expected at a `SequenceLocation` reference.
   *  - allelic_state
      - `CURIE`_
      - 0..1
      - We RECOMMEND that the allelic_state of variant be described by terms from
        the Genotype Ontology (GENO). These SHOULD descend from concept `GENO:0000875`_.

.. _VcfRecord:

VCF Record
$$$$$$$$$$

This data class is used when it is desirable to pass data as expected from a VCF record.
The class is only used as an optional attribute within a :ref:`VariationDescriptor`.
The Genotype field from a VCF should be captured by the `allelic_state` attribute in
the Variation Descriptor.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Type
      - Limits
      - Description
   *  - genome_assembly
      - string
      - 1..1
      - Identifier for the genome assembly used to call the allele.
   *  - chrom
      - string
      - 1..1
      - A chromosome or contig identifier.
   *  - pos
      - int
      - 1..1
      - The reference residue-coordinate position, with the first
        residue having position 1.
   *  - id
      - string
      - 0..1
      - A semicolon-separated list of unique identifiers where available.
        For example, dbSNP rsIDs. We RECOMMEND storing this information as
        a list in the :ref:`VariationDescriptor` `xargs` field.
   *  - ref
      - string
      - 1..1
      - Reference base as expected by the VCF specification.
   *  - alt
      - string
      - 1..1
      - Alternate base as expected by the VCF specification.
   *  - qual
      - string
      - 0..1
      - Quality: Phred-scaled quality score for the assertion made in ALT.
   *  - filter
      - string
      - 0..1
      - Filter status: PASS if this position has passed all filters.
   *  - info
      - string
      - 0..1
      - Additional information: Semicolon-separated series of additional
        information fields.

.. _SO:0001537: http://www.sequenceontology.org/browser/current_release/term/SO:0001537
.. _GENO:0000875: http://purl.obolibrary.org/obo/GENO_0000875

.. _LocationDescriptor:

Location Descriptor
###################

This descriptor is intended to reference `VRS Location`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Sequence Location Descriptor* has the following attributes:

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
      - MUST be "LocationDescriptor"
   *  - location_id
      - CURIE_
      - 0..1
      - This MUST be provided if `location` is omitted
   *  - location
      - `VRS Location`_
      - 0..1
      - This MUST be provided if `location_id` is omitted

.. _SequenceDescriptor:

Sequence Descriptor
###################

This descriptor is intended to reference `VRS Sequence`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Sequence Descriptor* has the following attributes:

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
      - MUST be "SequenceDescriptor"
   *  - sequence_id
      - CURIE_
      - 0..1
      - This MUST be provided if `sequence` is omitted
   *  - sequence
      - `VRS Sequence`_
      - 0..1
      - This MUST be provided if `sequence_id` is omitted
   *  - residue_type
      - `CURIE`_
      - 0..1
      - CURIE MUST be `SO:0000348 (nucleic acid)`_, `SO:0001407 (peptidyl)`_,
        or a descendent of one of these concepts.

.. _`SO:0000348 (nucleic acid)`: http://www.sequenceontology.org/browser/current_release/term/SO:0000348
.. _`SO:0001407 (peptidyl)`: http://www.sequenceontology.org/browser/current_release/term/SO:0001407

.. _GeneDescriptor:

Gene Descriptor
###############

This descriptor is intended to reference `VRS Gene`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Gene Descriptor* has the following attributes:

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
      - MUST be "GeneDescriptor"
   *  - gene_id
      - CURIE_
      - 0..1
      - This MUST be provided if `gene` is omitted
   *  - gene
      - `VRS Gene`_
      - 0..1
      - This MUST be provided if `gene_id` is omitted

.. _Gene: https://vrs.ga4gh.org/en/latest/terms_and_model.html#gene

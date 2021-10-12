**Computational Definition**

This data class is used when it is desirable to pass data as expected from a VCF record. The class is only used as an optional attribute within a :ref:`VariationDescriptor`. The Genotype field from a VCF should be captured by the `allelic_state` attribute in the Variation Descriptor.

**Information Model**

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
      - string
      - 1..1
      - The reference residue-coordinate position, with the first residue having position 1.
   *  - id
      - string
      - 0..1
      - A semicolon-separated list of unique identifiers where available. For example, dbSNP rsIDs. We RECOMMEND storing this information as a list in the :ref:`VariationDescriptor` `xrefs` field.
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
      - Additional information: Semicolon-separated series of additional information fields.

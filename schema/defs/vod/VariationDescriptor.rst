**Computational Definition**

This descriptor class is used for describing VRS Variation value objects.

**Information Model**

Some VariationDescriptor attributes are inherited from :ref:`ValueObjectDescriptor`.

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
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_
      - 1..1
      - Descriptor ID; MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be "VariationDescriptor".
   *  - label
      - string
      - 0..1
      - A primary label for the value object.
   *  - description
      - string
      - 0..1
      - A free-text description of the value object.
   *  - xrefs
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_
      - 0..m
      - List of CURIEs representing associated concepts.
   *  - alternate_labels
      - string
      - 0..m
      - List of strings representing alternate labels for the value object.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - List of resource-specific :ref:`Extensions <Extension>` needed to describe the value object.
   *  - variation_id
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_
      - 0..1
      - This SHOULD be provided if *variation* is omitted.
   *  - variation
      - `Variation <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/Variation>`_
      - 0..1
      - This SHOULD be provided if *variation_id* is omitted.
   *  - molecule_context
      - string
      - 0..1
      - The molecular context of this variant. Must be one of "genomic", "transcript", or "protein".
   *  - structural_type
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_
      - 0..1
      - The structural variant type associated with this variant. We RECOMMEND a descendent term of `SO:0001537 <http://www.sequenceontology.org/browser/current_release/term/SO:0001537>`_.
   *  - expressions
      - :ref:`Expression`
      - 0..1
      - Typically HGVS or ISCN nomenclature expressions. Other systems relevant to the description of variation MAY be used.
   *  - vcf_record
      - :ref:`VcfRecord`
      - 0..1
      - A VCF Record of the variant. This SHOULD be a single allele, the VCF genotype (GT) field should be represented in the *allelic_state* attribute.
   *  - gene_context
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_ | :ref:`GeneDescriptor`
      - 0..1
      - A specific gene context that applies to this variant.
   *  - vrs_ref_allele_seq
      - `Sequence <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/Sequence>`_
      - 0..1
      - A `VRS Sequence`_ corresponding to a "ref allele", describing the sequence expected at a `VRS SequenceLocation`_ reference.
   *  - allelic_state
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.1/schema/vrs.json#/definitions/CURIE>`_
      - 0..1
      - We RECOMMEND that the *allelic_state* of a variation be described by terms from the Genotype Ontology (GENO). These SHOULD descend from concept `GENO:0000875 <http://purl.obolibrary.org/obo/GENO_0000875>`.

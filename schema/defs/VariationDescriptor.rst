Variation Descriptor
####################
This descriptor class is used for describing VRS Variation value objects. This is a subclass of :ref:`value_object_descriptor` and inherits all Value Object Descriptor attributes.

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
      - 0..1
      - MUST be "VariationDescriptor".
   *  - variation_id
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_
      - 0..1
      - The SHOULD be provided if *variation* is omitted.
   *  - variation
      - `Variation <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Variation>`_
      - 0..1
      - The SHOULD be provided if *variation_id* is omitted.
   *  - molecule_context
      - string
      - 0..1
      - The molecular context of this variant. Must be one of "genomic", "transcript", or "protein".
   *  - structural_type
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_
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
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_ | :ref:`GeneDescriptor`
      - 0..1
      - A specific gene context that applies to this variant.
   *  - vrs_ref_allele_seq
      - `Sequence <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Sequence>`_
      - 0..1
      - A `VRS Sequence`_ corresponding to a "ref allele", describing the sequence expected at a `VRS SequenceLocation`_ reference.
   *  - allelic_state
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_
      - 0..1
      - We RECOMMEND that the *allelic_state* of a variation be described by terms from the Genotype Ontology (GENO). These SHOULD descend from concept `GENO:0000875 <http://purl.obolibrary.org/obo/GENO_0000875>`.

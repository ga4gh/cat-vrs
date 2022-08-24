**Computational Definition**

This descriptor class is used for describing VRS Variation value objects.

**Information Model**

Some VariationDescriptor attributes are inherited from :ref:`Entity`.

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
      - 1..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
   *  - type
      - string
      - 1..1
      - MUST be "VariationDescriptor".
   *  - label
      - string
      - 0..1
      - A primary label for the value object.
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - description
      - string
      - 0..1
      - A free-text description of the value object.
   *  - xrefs
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..m
      - List of CURIEs representing associated concepts.
   *  - alternate_labels
      - string
      - 0..m
      - List of strings representing alternate labels for the value object.
   *  - variation_id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - This SHOULD be provided if *variation* is omitted.
   *  - variation
      - `Variation <vrs.json#/definitions/Variation>`_
      - 0..1
      - This SHOULD be provided if *variation_id* is omitted.
   *  - molecule_context
      - string
      - 0..1
      - The molecular context of this variant. Must be one of "genomic", "transcript", or "protein".
   *  - structural_type
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The structural variant type associated with this variant. We RECOMMEND a descendent term of `SO:0001537 <http://www.sequenceontology.org/browser/current_release/term/SO:0001537>`_.
   *  - expressions
      - :ref:`Expression`
      - 0..m
      - Typically HGVS or ISCN nomenclature expressions. Other systems relevant to the description of variation MAY be used.
   *  - gene_context
      - `CURIE <core.json#/$defs/CURIE>`_ | :ref:`GeneDescriptor`
      - 0..1
      - A specific gene context that applies to this variant.
   *  - vrs_ref_allele_seq
      - `Sequence <vrs.json#/definitions/Sequence>`_
      - 0..1
      - A `VRS Sequence`_ corresponding to a "ref allele", describing the sequence expected at a `VRS SequenceLocation`_ reference.
   *  - allelic_state
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - We RECOMMEND that the *allelic_state* of a variation be described by terms from the Genotype Ontology (GENO). These SHOULD descend from concept `GENO:0000875 <http://purl.obolibrary.org/obo/GENO_0000875>`.

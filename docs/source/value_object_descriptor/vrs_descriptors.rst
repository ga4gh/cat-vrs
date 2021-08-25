Variation Descriptor
####################
This descriptor is intended as an abstract class for `VRS Variation`_ value objects.
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
   *  - gene_context
      - CURIE | :ref:`GeneDescriptor`
      - 0..*
      - A specific gene context that applies to this variant.
   *  - vrs_ref_allele_seq
      - `Sequence`_
      - 0..1
      - A `Sequence`_ corresponding to a "ref allele", describing the
        sequence expected at a `SequenceLocation` reference.
   *  - location_descriptor
      - :ref:`LocationDescriptor`
      - 0..*
      -
   *  - sequence_descriptor
      - :ref:`SequenceDescriptor`
      - 0..*
      -
   *  - allelic_state
      - `CURIE`_
      - 0..1
      - We RECOMMEND that the allelic_state of variant be described by terms from
        the Genotype Ontology (GENO). These SHOULD descend from concept `GENO:0000875`_.

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
   *  - sequence_descriptor
      - :ref:`SequenceDescriptor`
      - 0..*
      -

.. _SequenceDescriptor:

Sequence Descriptor
###################

This descriptor is intended to reference `Sequence`_ value objects.
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
   *  - residue_type
      - `CURIE`_
      - 0..1
      - CURIE MUST be `SO:0000348 (nucleic acid)`_, `SO:0001407 (peptidyl)`_,
        or a descendent of one of these concepts.

.. _Sequence: https://vrs.ga4gh.org/en/latest/terms_and_model.html#sequence
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

.. _Gene: https://vrs.ga4gh.org/en/latest/terms_and_model.html#gene

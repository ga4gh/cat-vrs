Allele Descriptor
#################

This descriptor is intended to reference `Allele`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Allele Descriptor* has the following attributes:

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
      - MUST be "AlleleDescriptor"
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
   *  - ref_allele_seq
      - `Sequence`_
      - 0..1
      - A `Sequence`_ corresponding to a "ref allele", as used in HGVS,
        SPDI, and VCF variation formats. Useful for validation.
   *  - gene_context
      - CURIE | :ref:`GeneDescriptor`
      - 0..1
      - A specific gene context that applies to this variant.

.. _Allele: https://vrs.ga4gh.org/en/latest/terms_and_model.html#allele
.. _SO:0001537: http://www.sequenceontology.org/browser/current_release/term/SO:0001537

Text Descriptor
###############

This descriptor is intended to reference `Text`_ variation value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Text Descriptor* has the following attributes:

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
      - MUST be "TextDescriptor"

.. _Text: https://vrs.ga4gh.org/en/latest/terms_and_model.html#text

CopyNumber Descriptor
#####################

This descriptor is intended to reference `CopyNumber`_ variation value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *CopyNumber Descriptor* has the following attributes:

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
      - MUST be "CopyNumberDescriptor"

.. _CopyNumber: https://vrs.ga4gh.org/en/latest/terms_and_model.html#copynumber

Variation Set Descriptor
########################

This descriptor is intended to reference `VariationSet`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Variation Set Descriptor* has the following attributes:

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
      - MUST be "VariationSetDescriptor"

.. _VariationSet: https://vrs.ga4gh.org/en/latest/terms_and_model.html#variationset

Haplotype Descriptor
####################

This descriptor is intended to reference `Haplotype`_ variation value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Haplotype Descriptor* has the following attributes:

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
      - MUST be "HaplotypeDescriptor"

.. _Haplotype: https://vrs.ga4gh.org/en/latest/terms_and_model.html#haplotype

Sequence Location Descriptor
############################

This descriptor is intended to reference `SequenceLocation`_ value objects.
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
      - MUST be "SequenceLocationDescriptor"

.. _SequenceLocation: https://vrs.ga4gh.org/en/latest/terms_and_model.html#sequencelocation

Chromosome Location Descriptor
##############################

This descriptor is intended to reference `ChromosomeLocation`_ value objects.
In addition to the attributes inherited from its :ref:`value_object_descriptor`
parent class, the *Chromosome Location Descriptor* has the following attributes:

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
      - MUST be "ChromosomeLocationDescriptor"

.. _ChromosomeLocation: https://vrs.ga4gh.org/en/latest/terms_and_model.html#chromosomelocation

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

.. _Sequence: https://vrs.ga4gh.org/en/latest/terms_and_model.html#sequence

.. _GeneDescriptor:

Gene Descriptor
###############

This descriptor is intended to reference `Gene`_ value objects.
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

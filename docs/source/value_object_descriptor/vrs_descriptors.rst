.. _VariationDescriptor:

Variation Descriptor
####################

.. include:: ../defs/vod/VariationDescriptor.rst

.. _LocationDescriptor:

Location Descriptor
###################

This descriptor is intended to reference `VRS Location`_ value objects.
In addition to the attributes inherited from its :ref:`ValueObjectDescriptor`
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
In addition to the attributes inherited from its :ref:`ValueObjectDescriptor`
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
In addition to the attributes inherited from its :ref:`ValueObjectDescriptor`
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

.. _CategoricalVariationDescriptor:

Categorical Variation Descriptor
################################

.. include:: ../defs/vod/CategoricalVariationDescriptor.rst
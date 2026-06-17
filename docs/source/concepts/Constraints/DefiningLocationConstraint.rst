.. _DefiningLocationConstraint:

Defining Location Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/DefiningLocationConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BRAF V600 <BrafV600>`
- :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count) <CategoricalCnvEx1>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy change) <CategoricalCnvEx2>`
- :ref:`TP53 Loss <Tp53CopyLoss>`

A representative example of this Constraint, from :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count) <CategoricalCnvEx1>`:

.. literalinclude:: ../../../../examples/json/categoricalCnv-ex1.json
  :language: json
  :lines: 44-99

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used to describe a Categorical Variant using a VRS :ref:`Sequence Location <SequenceLocation>` object, such as defining a specific exon or genomic segment.

location
########

The *location* attribute is required and must be a valid VRS :ref:`Sequence Location <SequenceLocation>`.

.. include:: ../../_includes/_guidance_generate_sequence_location_text.rst

.. include:: ../../_includes/_guidance_generate_sequence_location_box.rst

relations
#########

The *relations* attribute is optional and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from a defined ontology. Relation terms describe how *members* of a :ref:`Categorical Variant <CategoricalVariant>` relate to the Defining :ref:`Sequence Location <SequenceLocation>`.

.. include:: ../../_includes/_guidance_relations_requirement.rst

The following relation terms are some to consider using with this Constraint:

.. include:: ../../_includes/_guidance_ga4gh_gks_term_warning.rst

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - How the ``member`` relates to the Categorical Variant
   * - ga4gh-gks-term:allele-relation:self
     - Use when the ``member`` is the Defining ``Sequence Location`` itself.
   * - ga4gh-gks-term:allele-relation:liftover_to
     - Use when the ``member`` represents the equivalent genomic Sequence Location on another reference genome.
   * - ga4gh-gks-term:allele-relation:projection_of
     - Use when the ``member`` represents the equivalent RNA (pre-mRNA), mRNA, or protein Sequence Location on another transcript or protein isoform.

matchCharacteristic
###################

.. include:: ../../_includes/_guidance_match_characteristic_sequence_location.rst

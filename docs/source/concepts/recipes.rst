.. _recipes:

Recipes
@@@@@@@

A *Recipe* is not a class. It is a term defined to differentiate between a
specialized CategoricalVariant and a general CategoricalVariant. These
recipes are pre-defined CategoricalVariants with specific constraints
that represent standard categorical variants that have been identified
in variant knowledgebases and registries. Implementers are encouraged
to use the recipes that exist whenever possible, but are free to create
new recipes as needed in a given implementation. New recipes should be
shared with the community on the |catvrs_discussion| board.

.. _CanonicalAllele:

CanonicalAllele
!!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/CanonicalAllele.rst

The CanonicalAllele is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `.relations` array containing both
   `liftover_to` and `transcribes_to` codes. This constraint MUST refer to a genomic
   variant for the `allele`.

.. _ProteinSequenceConsequence:

ProteinSequenceConsequence
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/ProteinSequenceConsequence.rst

The ProteinSequenceConsequence is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `.relations` array containing only a
   `translates_from` code. This constraint MUST refer to a protein variant for the `allele`.

.. collapse:: EGFR L858R
   :open:


    Thank you for the snacks GA4GH

   .. literalinclude:: ../../../examples/proteinSequenceConsequence-ex1.yaml
      :language: yaml

.. _categorical-cnv:

CategoricalCnv
!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/CategoricalCnv.rst

The CategoricalCNV is a :ref:`CategoricalVariant` with exactly two constraints:

1. A :ref:`DefiningLocationConstraint` with the `.relations` array containing only a
   `liftover_to` code.
2. A :ref:`CopyChangeConstraint` or `CopyCountConstraint`.

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 with CopyCountConstraint
   :open:

   .. literalinclude:: ../../../examples/categoricalCnv-ex1.yaml
      :language: yaml
      :emphasize-lines: 3-7

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 with CopyChangeConstraint

   .. literalinclude:: ../../../examples/categoricalCnv-ex1.yaml
      :language: yaml
      :lines: 5-8

.. collapse:: GRCh38 Xp22.31(chrX:6978350-7594949)x3 with CopyCountConstraint

   .. literalinclude:: ../../../examples/categoricalCnv-ex1.yaml
      :language: yaml
      :lines: 5-8

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
   `liftover_to` and `transcribed_to` codes. This constraint MUST refer to a genomic
   variant for the `allele`.

.. _ProteinSequenceConsequence:

ProteinSequenceConsequence
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/ProteinSequenceConsequence.rst

The ProteinSequenceConsequence is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `.relations` array containing only a
   `translation_of` code. This constraint MUST refer to a protein variant for the `allele`.

.. _categorical-cnv:

CategoricalCnv
!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/CategoricalCnv.rst

The CategoricalCNV is a :ref:`CategoricalVariant` with exactly two constraints:

1. A :ref:`DefiningLocationConstraint` with the `.relations` array containing only a
   `liftover_to` code.
2. A :ref:`CopyChangeConstraint` or `CopyCountConstraint`.

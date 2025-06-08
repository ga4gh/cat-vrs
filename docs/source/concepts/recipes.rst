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

**Examples**

.. collapse:: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_canonicalAllele-ex1
      :language: json

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: NC_000001.11:g.1699974C>G

   .. literalinclude:: ../../../schema/cat-vrs/json/example_canonicalAllele-ex2
      :language: json

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _ProteinSequenceConsequence:

ProteinSequenceConsequence
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/ProteinSequenceConsequence.rst

The ProteinSequenceConsequence is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `.relations` array containing only a
   `translates_from` code. This constraint MUST refer to a protein variant for the `allele`.

**Examples**

.. collapse:: EGFR L858R

   .. literalinclude:: ../../../schema/cat-vrs/json/example_proteinSequenceConsequence-ex1
      :language: json

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_proteinSequenceConsequence-ex2
      :language: json

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: BRAF V600

   .. literalinclude:: ../../../schema/cat-vrs/json/example_proteinSequenceConsequence-ex3
      :language: json

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _categorical-cnv:

CategoricalCnv
!!!!!!!!!!!!!!

.. include:: ../def/cat-vrs/CategoricalCnv.rst

The CategoricalCNV is a :ref:`CategoricalVariant` with exactly two constraints:

1. A :ref:`DefiningLocationConstraint` with the `.relations` array containing only a
   `liftover_to` code.
2. A :ref:`CopyChangeConstraint` or :ref:`CopyCountConstraint`.

**Examples**

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 with CopyCountConstraint

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex1
      :language: json

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 with CopyChangeConstraint

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex2
      :language: json

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: GRCh38 Xp22.31(chrX:6978350-7594949)x3

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex3
      :language: json

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: TP53 Loss

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex4
      :language: json

.. raw:: html

   <div style="margin-top: 1em;"></div>


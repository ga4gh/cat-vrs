.. _ProteinSequenceConsequence:

Protein Sequence Consequence
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/ProteinSequenceConsequence.rst

A ProteinSequenceConsequence is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `.relations` array containing only a
   `translation_of` code. This constraint MUST refer to a protein variant for the `allele`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`EGFR L858R <ProteinSequenceConsequenceEx1>`
- :ref:`NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter) <ProteinSequenceConsequenceEx2>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

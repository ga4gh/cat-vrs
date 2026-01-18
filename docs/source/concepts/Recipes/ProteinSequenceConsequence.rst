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
The following are example implementations of that satisfy the CanonicalAllele recipe:

.. collapse:: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_canonicalAllele-ex1
      :language: json

.. collapse:: NC_000001.11:g.1699974C>G

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_canonicalAllele-ex2
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

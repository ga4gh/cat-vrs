.. _CanonicalAllele:

Canonical Allele
!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CanonicalAllele.rst

A CanonicalAllele is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `relations` array containing both
   `liftover_to` and `transcribed_to` codes. This constraint MUST refer to a genomic
   variant for the `allele`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs) <CanonicalAlleleEx1>`
- :ref:`NC_000001.11:g.1699974C>G <CanonicalAlleleEx2>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

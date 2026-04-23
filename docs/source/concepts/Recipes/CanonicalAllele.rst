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
The following are example implementations of that satisfy the CanonicalAllele recipe:

.. collapse:: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)

   .. literalinclude:: ../../../../examples/json/canonicalAllele-ex1.json
      :language: json

.. collapse:: NC_000001.11:g.1699974C>G

   .. literalinclude:: ../../../../examples/json/canonicalAllele-ex2.json
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

.. _DefiningAlleleConstraint:

Defining Allele Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/DefiningAlleleConstraint.rst

Examples
@@@@@@@@
The following are example implementations of DefiningAlleleConstraint:

.. collapse:: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)

   .. literalinclude:: ../../../../examples/json/canonicalAllele-ex1.json
      :language: json
      :lines: 80-169

.. collapse:: NC_000001.11:g.1699974C>G

   .. literalinclude:: ../../../../examples/json/canonicalAllele-ex2.json
      :language: json
      :lines: 34-109

.. collapse:: EGFR L858R

   .. literalinclude:: ../../../../examples/json/proteinSequenceConsequence-ex1.json
      :language: json
      :lines: 96-147

.. collapse:: NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)

   .. literalinclude:: ../../../../examples/json/proteinSequenceConsequence-ex2.json
      :language: json
      :lines: 66-129

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

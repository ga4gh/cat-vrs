.. _CategoricalCnv:

Categorical CNV
!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CategoricalCnv.rst

A CategoricalCNV is a :ref:`CategoricalVariant` with exactly two constraints:

1. A :ref:`DefiningLocationConstraint` with the `.relations` array containing only a
   `liftover_to` code.
2. A :ref:`CopyChangeConstraint` or :ref:`CopyCountConstraint`.

Examples
@@@@@@@@
The following are example implementations of that satisfy the CanonicalAllele recipe:

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 with CopyCountConstraint

   .. literalinclude:: ../../../../examples/json/categoricalCnv-ex1.json
      :language: json

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 with CopyChangeConstraint

   .. literalinclude:: ../../../../examples/json/categoricalCnv-ex2.json
      :language: json

.. collapse:: GRCh38 Xp22.31(chrX:6978350-7594949)x3

   .. literalinclude:: ../../../../examples/json/categoricalCnv-ex3.json
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

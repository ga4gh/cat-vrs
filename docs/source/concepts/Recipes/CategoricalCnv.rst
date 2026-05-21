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

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <CategoricalCnvEx1>`
  - This example utilizes the :ref:`Copy Count Constraint <CopyCountConstraint>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <CategoricalCnvEx2>`
  - This example utilizes the :ref:`Copy Change Constraint <CopyChangeConstraint>`
- :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

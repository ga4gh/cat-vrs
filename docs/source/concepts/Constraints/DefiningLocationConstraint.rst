.. _DefiningLocationConstraint:

Defining Location Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/DefiningLocationConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BRAF V600 <BrafV600>`
- :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count) <CategoricalCnvEx1>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy change) <CategoricalCnvEx2>`
- :ref:`TP53 Loss <Tp53CopyLoss>`

A representative example of this Constraint, from :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count) <CategoricalCnvEx1>`:

.. literalinclude:: ../../../../examples/json/categoricalCnv-ex1.json
  :language: json
  :lines: 44-99

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

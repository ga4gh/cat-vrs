.. _CopyCountConstraint:

Copy Count Constraint
!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CopyCountConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <CategoricalCnvEx1>`

A representative example of this Constraint, from :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`:

.. literalinclude:: ../../../../examples/json/categoricalCnv-ex3.json
  :language: json
  :lines: 18-21

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used when constructing a :ref:`Categorical Copy Number Variant <CategoricalCnv>` when a copy number variation is expressed as an integer or :ref:`Range`. If looking to express the copy number variation as a category, consider instead applying the :ref:`Copy Change Constraint <CopyChangeConstraint>`.

copies
######

The *copies* attribute is required and can be populated with either an integer or :ref:`Range`. Range supports the use of ``null`` for either bound to represent an indefinite value.

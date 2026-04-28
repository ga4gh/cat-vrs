.. _CopyCountConstraint:

Copy Count Constraint
!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CopyCountConstraint.rst

Examples
@@@@@@@@

The following are example implementations of CopyCountConstraint:

.. collapse:: 3 copies

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_categoricalCnv-ex3
      :language: json
      :lines: 21-24

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used when constructing a :ref:`Categorical Copy Number Variant <CategoricalCnv>` when a copy number variation is expressed as an integer or :ref:`Range`. If looking to express the copy number variation as a category, consider instead applying the :ref:`Copy Change Constraint <CopyChangeConstraint>`.

copies
######

The *copies* attribute is required and can be populated with either an integer or :ref:`Range`. Range supports the use of ``null`` for either bound to represent an indefinite value.

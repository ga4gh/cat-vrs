.. _CategoricalVariantCriterion:

Categorical Variant Criterion
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

A Categorical Variant Criterion is used as an element within a :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` to assert that its subject :ref:`Categorical Variant <CategoricalVariant>` is present or absent.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CategoricalVariantCriterion.rst

Examples
@@@@@@@@

.. literalinclude:: ../../../../examples/json/composite-ex1.json
  :language: json
  :lines: 1-16

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This class must be used whenever constructing a :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` and including individual :ref:`Categorical Variants <CategoricalVariant>`.

subject
#######

The *subject* attribute is required and must be a valid :ref:`Categorical Variant <CategoricalVariant>` object.

presence
########

The *presence* attribute asserts whether the *subject* is required to be ``present`` or ``absent`` for the parent :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` to be satisfied. Either of the following **Name** values can be used to populate this attribute:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - **present**
     - The subject Categorical Variant is present.
   * - **absent**
     - The subject Categorical Variant is not present.

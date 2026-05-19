.. _FunctionVariant:

Function Variant
!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/FunctionVariant.rst

The FunctionVariant is a :ref:`CategoricalVariant` with at least two constraints:

1. A :ref:`FunctionConstraint`.
2. A :ref:`DefiningAlleleConstraint`, :ref:`DefiningLocationConstraint`, or :ref:`FeatureContextConstraint`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`BRCA2 loss of function variants <FunctionVariantEx2>`
- :ref:`NRAS functionally normal variants <FunctionVariantEx1>`
- :ref:`PIK3CA p.R38H <FunctionVariantEx3>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

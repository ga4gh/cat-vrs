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
The following are example implementations of that satisfy the FunctionVariant recipe:

.. collapse:: NRAS functionally normal variants

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex1
      :language: json

.. collapse:: BRCA2 loss of function variants

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex2
      :language: json

.. collapse:: PIK3CA p.R38H

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex3
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

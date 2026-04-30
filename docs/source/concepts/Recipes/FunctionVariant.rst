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

   .. literalinclude:: ../../../../examples/json/functionVariant-ex1.json
      :language: json

.. collapse:: BRCA2 loss of function variants

   .. literalinclude:: ../../../../examples/json/functionVariant-ex2.json
      :language: json

.. collapse:: PIK3CA p.R38H

   .. literalinclude:: ../../../../examples/json/functionVariant-ex3.json
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

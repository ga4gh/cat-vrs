.. _constraint:

Constraint
!!!!!!!!!!

The *Constraint* class is an abstract class that is the parent of all other Constraint subclasses.  A constraint is a rule or set of rules that a variant must satisfy to qualify as a valid member of the :ref:`Categorical Variant <CategoricalVariant>`. Constraint subclasses are only used in Categorical Variant objects.

.. rubric:: Definition and Information Model
   :class: rubric-h2

.. include::  ../../def/cat-vrs/Constraint.rst

.. rubric:: Examples
   :class: rubric-h2

This documentation contains several :ref:`Examples`, organized by Constraint. Each Constraint and :ref:`Recipe <Recipes>` also include representative examples inline with their documentation.

.. rubric:: Implementation Guidance
   :class: rubric-h2

Please refer to specific Constraint subclasses for implementation guidance.

.. toctree::
   :hidden:
   :titlesonly:

   AdjacencyConstraint
   CopyChangeConstraint
   CopyCountConstraint
   DefiningAlleleConstraint
   DefiningLocationConstraint
   FeatureContextConstraint
   FunctionConstraint

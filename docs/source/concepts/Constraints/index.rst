.. _constraints:

.. _constraint:

Constraints
!!!!!!!!!!!

The *Constraint* class is an abstract class that is the parent of all other constraint classes.  A constraint is a rule or set of rules that a variant must satisfy to qualify as a valid member of the CategoricalVariant. Constraint subclasses are only used in CategoricalVariant objects.

.. include::  ../../def/cat-vrs/Constraint.rst

**Subclasses**

.. toctree::
   :titlesonly:

   CopyChangeConstraint
   CopyCountConstraint
   DefiningAlleleConstraint
   DefiningLocationConstraint
   FeatureContextConstraint
   FunctionConstraint

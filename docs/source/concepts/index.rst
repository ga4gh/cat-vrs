.. _data-model:

Data Model
!!!!!!!!!!

At the Cat-VRS top of the Cat-VRS data model is the Categorical Variant class.
The Categorical Variant is composed of one or more constraints that define The
Categorical Variant. The Constraint subclasses are used to define what we refer
to as **Recipes**. Recipes are pre-defined Categorical Variants with specific
constraints that represent standard categorical variants that have been identified.
The following sections describe the Cat-VRS base classes (Categorical Variant and
Constraint subclasses), the standard recipes, and the additional *Imported* data
class and types from VRS 2.0 and GKS Core 1.0 that support the Cat-VRS data model.

- :ref:`Constraints`: models that describe categorical variation and constraints
- :ref:`Recipes`: models that describe categorical variation recipes with specific constraints
- :ref:`imported`: imported data types and classes that support the above models

.. toctree::
    :hidden:

    Recipes/index
    Constraints/index
    imported/index

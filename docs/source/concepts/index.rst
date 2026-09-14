.. _data-model:
.. _classDiagram:

Data Model
!!!!!!!!!!

At the top of the Cat-VRS data model is the :ref:`Categorical Variant <CategoricalVariant>` class. The Categorical Variant is composed of one or more :ref:`Constraints <constraint>` that define the Categorical Variant. The Constraint subclasses are used to define what we refer to as :ref:`Recipes`. Recipes are pre-defined Categorical Variants with specific constraints that represent standard categorical variants that have been identified.

The following sections describe the Cat-VRS base classes (:ref:`Categorical Variant <CategoricalVariant>` and
:ref:`Constraint <constraint>`), Constraint subclasses, the standard :ref:`Recipes`, and the additional :ref:`Imported <imported>` data class and types from VRS and GKM Core that support the Cat-VRS data model.

- :ref:`Constraint`: models that describe categorical variation and constraints
- :ref:`Recipes`: models that describe categorical variation recipes with specific constraints
- :ref:`imported`: imported data types and classes that support the above models
- :ref:`additionalDataTypes`: additional data types that support Constraints and Recipes

.. toctree::
    :hidden:

    CategoricalVariant
    Constraints <Constraints/index>
    Recipes/index
    imported/index
    additional

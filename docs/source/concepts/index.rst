.. _data-model:

Data Model
!!!!!!!!!!

The foundational class of the Cat-VRS data model is the :ref:`Categorical Variant <CategoricalVariant>` class. The Categorical Variant is composed of one or more :ref:`Constraints <constraints>` that define it.

The Constraint subclasses are used to define :ref:`Recipes`, which are pre-defined Categorical Variants with specific Constraints that represent common categories of genomic variation.

Categorical Variants can be specified with a :ref:`Criterion <CategoricalVariantCriterion>`, which asserts whether each is present or absent, in order to combine them into :ref:`Composite Categorical Variants <CompositeCategoricalVariant>`. This supports representing the co-occurrence of multiple Categorical Variants, the negation of a single one, or more complex logical expressions through nesting Composite Categorical Variants.

In addition to the base Cat-VRS classes (:ref:`Categorical Variant <CategoricalVariant>`, :ref:`Composite Categorical Variant <CompositeCategoricalVariant>`, and :ref:`Constraint <constraint>`), the following sections describe models that constitute the specification:

- :ref:`Constraints`: models that describe categorical variation and constraints
- :ref:`Recipes`: models that describe categorical variation recipes with specific constraints
- :ref:`Additional <additional>`: classes that support composing and assertion of Categorical Variants
- :ref:`Imported <imported>`: imported classes and data types that support the specification

.. toctree::
    :hidden:

    CategoricalVariant
    CompositeCategoricalVariant
    Constraint
    Constraints/index
    Recipes/index
    Additional/index
    Imported/index

.. _CompositeCategoricalVariant:

Composite Categorical Variant
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The Composite Categorical Variant class is a logical expression that combines one or more :ref:`Categorical Variant Criteria <CategoricalVariantCriterion>`, or nested Composite Categorical Variants, using a boolean *operator*
(``AND`` / ``OR``). This allows multiple :ref:`Categorical Variant Criteria <CategoricalVariantCriterion>` to be composed into more complex categorical expressions, such as representing the co-occurrence of the underlying :ref:`Categorical Variants <CategoricalVariant>`.

.. rubric:: Definition and Information Model
   :class: rubric-h2

.. include:: ../def/cat-vrs/CompositeCategoricalVariant.rst

.. rubric:: Examples
   :class: rubric-h2

The following examples utilize this class:

- :ref:`BCR::ABL1 and ABL1 p.T315I <CompositeEx1>`
- :ref:`Hormone Receptor Positive <CompositeEx2>`
- :ref:`KIT p.D817V negative <CompositeEx3>`
- :ref:`KRAS and NRAS wild type <CompositeEx4>`
- :ref:`TP53 wild type <CompositeEx5>`
- :ref:`TP53 wild type and MDM2 amplification <CompositeEx6>`

.. rubric:: Implementation Guidance
   :class: rubric-h2

The *elements* attribute is required and may be populated with either :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`, to express an individual :ref:`Categorical Variant <CategoricalVariant>` as being present or absent within the composite, or a nested Composite Categorical Variant.

The *operator* attribute is also required and specifies how the included *elements* are combined to define the Composite Categorical Variant. Either of the following **Name** values can be used to populate this attribute:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - **AND**
     - All elements must be satisfied.
   * - **OR**
     - At least one element must be satisfied.

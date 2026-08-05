.. _CompositeCategoricalVariant:

Composite Categorical Variant
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The Composite Categorical Variant class is a logical expression that combines
one or more :ref:`Categorical Variant Criteria <CategoricalVariantCriterion>`,
or nested Composite Categorical Variants, using a boolean ``operator``
(``AND`` / ``OR``). It allows multiple :ref:`Categorical Variants
<CategoricalVariant>` to be composed into more complex categorical
expressions, such as combined biomarker or fusion+mutation statuses.

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

Each element of a Composite Categorical Variant's ``elements`` list must be either a :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>` or another Composite Categorical Variant, allowing composite expressions to be nested arbitrarily deep. Refer to :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>` for how individual Categorical Variants are asserted present or absent within a composite expression.

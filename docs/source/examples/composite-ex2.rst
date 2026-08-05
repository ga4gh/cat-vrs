:orphan:

.. _CompositeEx2:

:doc:`← Back to Examples </examples/index>`

Hormone Receptor Positive
!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

Many breast cancers are described as Hormone Receptor Positive, meaning that the tumor cells in a tissue express either the estrogen receptor, progesterone receptor, or both.

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Feature Context Constraint <FeatureContextConstraint>`

.. rubric:: Properties

``id``: catvrs.composite.example:1
  This identifier was arbitrarily set for the purposes of this documentation.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: Hormone Receptor Positive
  This field was populated with the name of this Composite Categorical Variant.

``aliases``: HR+
  This field was populated with an example value.

``description``: An optional field to describe this Composite Categorical Variant.
  This field was populated with an example value.

``mappings``: `National Cancer Institute Thesaurus (NCI) C101267 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C101267>`_
  A concept mapping to the NCI Thesaurus' entry for Hormone Receptor Positive was added.

``extensions``: null
  No :ref:`extensions <Extension>` included.

.. rubric:: Elements

The following elements are joined with an **OR** ``operator``:

- Estrogen Receptor Positive, Progesterone Receptor Negative
- Estrogen Receptor Negative, Progesterone Receptor Positive
- Estrogen Receptor Positive, Progesterone Receptor Positive

Each nested Composite Categorical Variant joins the Estrogen receptor (``uniprot:P03372``) and Progesterone receptor* (``uniprot:P06401``) concepts with an **AND** ``operator``, with both markers asserted as either **present** or **absent** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/composite-ex2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/composite-ex2.yaml
  :language: yaml

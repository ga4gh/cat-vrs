:orphan:

.. _CompositeEx6:

:doc:`← Back to Examples </examples/index>`

TP53 wild type and MDM2 amplification
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

.. TODO: no source citation identified yet -- confirm whether one should be added (e.g. a clinical trial or guideline eligibility criterion combining TP53 wild type with MDM2 amplification), or whether this is a synthetic example with no external source.

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Location Constraint <DefiningLocationConstraint>`
- :ref:`Feature Context Constraint <FeatureContextConstraint>`
- :ref:`Copy Change Constraint <CopyChangeConstraint>`

.. rubric:: Properties

``id``: catvrs.composite.example:5
  This identifier was arbitrarily set for the purposes of this documentation.

.. TODO: this ``id`` (``catvrs.composite.example:5``) duplicates the ``id`` used in composite-ex5.yaml. Confirm the intended, non-colliding identifier scheme across these examples (this file, being example 6, likely should use ``catvrs.composite.example:6``).

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: TP53 wild type and MDM2 amplification
his field was populated with the name of this Composite Categorical Variant.

``description``: An optional field to describe this Composite Categorical Variant.
  This field was populated with an example value.

``aliases``: null
  No aliases included.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Elements

The following elements are joined with an **AND** ``operator``:

- :ref:`NC_000017.11:7668420–7687490, the genomic location corresponding to *TP53* <CompositeEx5>`
- copy gain of NC_000012.12:68808177-201368845544, the genomic location corresponding to *MDM2*

These elements are **absent** and **present** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`, respectively.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/composite-ex6.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/composite-ex6.yaml
  :language: yaml

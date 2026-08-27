:orphan:

.. _CompositeEx3:

:doc:`← Back to Examples </examples/index>`

KIT p.D816V negative
!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

This example shows a single, negated Categorical Variant. For example, the US FDA has approved the therapy `imatinib <https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021588s062lbl.pdf>`_ for the "treatment of patients with aggressive systemic mastocytosis without the D816V c-Kit mutation".

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`

.. rubric:: Properties

``id``: catvrs.composite.example:3
  This identifier was arbitrarily set for the purposes of this documentation.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: KIT p.D816V negative
  This field was populated with the name of this Composite Categorical Variant.

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

- `NM_000222.2(KIT):c.2447A>T(p.Asp816Val) <https://civicdb.org/variants/65/summary>`_

This single element is **absent** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/composite-ex3.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/composite-ex3.yaml
  :language: yaml

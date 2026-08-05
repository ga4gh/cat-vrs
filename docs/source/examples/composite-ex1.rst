:orphan:

.. _CompositeEx1:

:doc:`← Back to Examples </examples/index>`

BCR::ABL1 and ABL1 p.T315I
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

The European Medicines Agency has approved `ponatinib <https://www.ema.europa.eu/en/medicines/human/EPAR/iclusig>`_ for the treatment of patients with acute lymphoblastic leukaemia with both the *BCR*::*ABL1* fusion and *ABL1* p.T315I.

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Adjacency Constraint <AdjacencyConstraint>`
- :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`

.. rubric:: Properties

``id``: catvrs.composite.example:1
  This identifier was arbitrarily set for the purposes of this documentation.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: BCR::ABL1 and ABL1 p.T315I
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

- :ref:`BCR(ncbi:613)::ABL1(ncbi:25) <AdjacencyFusionEx1>`
- *ABL1* p.T315I

Both elements are **present** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/composite-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/composite-ex1.yaml
  :language: yaml

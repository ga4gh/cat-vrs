:orphan:

.. _PathogenicityVariantEx1:

:doc:`← Back to Examples </examples/index>`

BRCA1 likely pathogenic variants
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

This is a constructed example and is not sourced from an external knowledgebase.

.. rubric:: :ref:`Recipes` that this example satisfies

This example does not satisfy any :ref:`Recipes`.

.. rubric:: Properties

``id``: example:brca1-likely-pathogenic
  A placeholder identifier for this constructed example.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: BRCA1 likely pathogenic variants
  Representing the set of BRCA1 variants that are classified as likely pathogenic.

``description``: A brief placeholder note.
  This field was populated with an example value.

``aliases``: null
  No aliases included in this example.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Constraints

:ref:`Feature Context Constraint <FeatureContextConstraint>`
  The ``featureContext`` is a :ref:`Mappable Concept <MappableConcept>` for BRCA1 (hgnc:1100), with a primaryCoding linking to its HGNC entry.

:ref:`Pathogenicity Constraint <PathogenicityConstraint>`
  The ``classification`` is a :ref:`Mappable Concept <MappableConcept>` for Likely Pathogenic (ncit:C168800), with a primaryCoding linking to the NCI Thesaurus term Likely Pathogenic Variant.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/pathogenicityVariant-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/pathogenicityVariant-ex1.yaml
  :language: yaml

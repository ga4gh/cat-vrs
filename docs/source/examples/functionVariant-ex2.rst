:orphan:

.. _FunctionVariantEx2:

:doc:`← Back to Examples </examples/index>`

BRCA2 loss of function variants
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC molecular profile id 186: BRCA2 Mutation Loss Of Function <https://civicdb.org/molecular-profiles/186/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Function Variant <FunctionVariant>`

.. rubric:: Properties

``id``: civic.mpid:186
  CIViC Molecular Profile ID, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: BRCA2 loss of function variants
  Representing the set of BRCA2 variants that result in loss of function.

``description``: A brief placeholder note.
  This field was populated with an example value because CIViC does not provide a longform description.

``aliases``: null
  No aliases included in this example.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Constraints

:ref:`Feature Context Constraint <FeatureContextConstraint>`
  The ``featureContext`` is a :ref:`Mappable Concept <ConceptMapping>` for BRCA2 (hgnc:1101), with a primaryCoding linking to its HGNC entry.

:ref:`Function Constraint <FunctionConstraint>`
  The ``functionConsequence`` is a :ref:`Mappable Concept <ConceptMapping>` for loss of function (SO:0002054), with a primaryCoding linking to the Sequence Ontology term loss_of_function_variant.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/functionVariant-ex2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/functionVariant-ex2.yaml
  :language: yaml

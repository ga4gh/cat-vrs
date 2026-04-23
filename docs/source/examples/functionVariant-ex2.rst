:orphan:
.. _FunctionVariantEx2:

BRCA2 loss of function variants
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Source**: `CIViC molecular profile id 186: BRCA2 Mutation Loss Of Function <https://civicdb.org/molecular-profiles/186/summary>`_

**Recipes that this example satisfies**: :ref:`Function Variant <FunctionVariant>`

.. rubric:: Attributes

- ``id``: civic.mpid:186, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: BRCA2 loss of function variants, representing the set of BRCA2 variants that result in loss of function.
- ``description``: A brief placeholder note.
- ``aliases``: No aliases are included in this example.
- ``extensions``: No extensions are included in this example.
- ``mappings``: No mappings are included in this example.

.. rubric:: Constraints

:ref:`Feature Context Constraint <FeatureContextConstraint>`: The ``featureContext`` is a MappableConcept for BRCA2 (hgnc:1101), with a primaryCoding linking to its HGNC entry.

:ref:`Function Constraint <FunctionConstraint>`: The ``functionConsequence`` is a MappableConcept for loss of function (SO:0002054), with a primaryCoding linking to the Sequence Ontology term loss_of_function_variant.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/functionVariant-ex2.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/functionVariant-ex2.yaml
   :language: yaml

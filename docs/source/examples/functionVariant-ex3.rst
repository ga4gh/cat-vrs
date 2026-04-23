:orphan:
.. _FunctionVariantEx3:

PIK3CA p.R38H
!!!!!!!!!!!!!

**Source**: `CIViC molecular profile id 1150: PIK3CA R38H <https://civicdb.org/molecular-profiles/1150/summary>`_

**Recipes that this example satisfies**: :ref:`Function Variant <FunctionVariant>`

.. rubric:: Attributes

- ``id``: civic.mpid:1150, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: PIK3CA p.R38H, following the naming convention used by CIViC.
- ``description``: A brief placeholder note.
- ``aliases``: No aliases are included in this example.
- ``extensions``: No extensions are included in this example.
- ``mappings``: No mappings are included in this example.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`: The ``allele`` field is populated with the VRS Allele for NM_006218.4:c.113G>A, as included within ``members``.

:ref:`Feature Context Constraint <FeatureContextConstraint>`: The ``featureContext`` is a MappableConcept for PIK3CA (hgnc:8975), with a primaryCoding linking to its HGNC entry.

:ref:`Function Constraint <FunctionConstraint>`: The ``functionConsequence`` is a MappableConcept for gain of function (SO:0002053), with a primaryCoding linking to the Sequence Ontology term gain_of_function.

.. rubric:: Members

The ``members`` field includes one VRS Allele object generated using the VICC Variation Normalizer for NM_006218.4:c.113G>A, on the MANE Select coding transcript for PIK3CA (refseq:NM_006218.4).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/functionVariant-ex3.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/functionVariant-ex3.yaml
   :language: yaml

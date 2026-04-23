:orphan:
.. _FunctionVariantEx1:

NRAS functionally normal variants
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Source**: `CIViC molecular profile id 4428: NRAS Wild type <https://civicdb.org/molecular-profiles/4428/summary>`_

**Recipes that this example satisfies**: :ref:`Function Variant <FunctionVariant>`

.. rubric:: Attributes

- ``id``: civic.mpid:4428, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: NRAS functionally normal variants, chosen to represent the set of NRAS variants that are likely neutral rather than using CIViC's "Wild type" framing.
- ``description``: A brief placeholder note.
- ``aliases``: No aliases are included in this example.
- ``extensions``: No extensions are included in this example.
- ``mappings``: No mappings are included in this example.

.. rubric:: Constraints

:ref:`Feature Context Constraint <FeatureContextConstraint>`: The ``featureContext`` is a MappableConcept for NRAS (hgnc:7989), with a primaryCoding linking to its HGNC entry.

:ref:`Function Constraint <FunctionConstraint>`: The ``functionConsequence`` is a MappableConcept for functionally normal (SO:0002219), with a primaryCoding linking to the Sequence Ontology term functionally_normal.

.. rubric:: Members

The ``members`` field includes one VRS Allele object generated using the VICC Variation Normalizer for NM_002524.5(NRAS):c.170A>C (p.D57A), a variant categorized as Likely Neutral by OncoKB, on the MANE Select coding transcript for NRAS (refseq:NM_002524.5).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/functionVariant-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/functionVariant-ex1.yaml
   :language: yaml

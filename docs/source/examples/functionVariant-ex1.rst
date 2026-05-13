:orphan:

.. _FunctionVariantEx1:

:doc:`← Back to Examples </examples/index>`

NRAS functionally normal variants
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC molecular profile id 4428: NRAS Wild type <https://civicdb.org/molecular-profiles/4428/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Function Variant <FunctionVariant>`

.. rubric:: Properties

``id``: civic.mpid:4428
  CIViC Molecular Profile ID, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: NRAS functionally normal variants
  Chosen to represent the set of NRAS variants that are likely neutral rather than using CIViC's "Wild type" framing.

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
  The ``featureContext`` is a :ref:`Mappable Concept <ConceptMapping>` for NRAS (hgnc:7989), with a primaryCoding linking to its HGNC entry.

:ref:`Function Constraint <FunctionConstraint>`
  The ``functionConsequence`` is a :ref:`Mappable Concept <ConceptMapping>` for functionally normal (SO:0002219), with a primaryCoding linking to the Sequence Ontology term functionally_normal.

.. rubric:: Members

The ``members`` field includes one VRS Allele object generated using the VICC Variation Normalizer for NM_002524.5(NRAS):c.170A>C (p.D57A), a variant categorized as Likely Neutral by OncoKB, on the MANE Select coding transcript for *NRAS* (refseq:NM_002524.5).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/functionVariant-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/functionVariant-ex1.yaml
  :language: yaml

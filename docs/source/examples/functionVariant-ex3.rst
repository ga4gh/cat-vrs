:orphan:

.. _FunctionVariantEx3:

:doc:`← Back to Examples </examples/index>`

PIK3CA p.R38H
!!!!!!!!!!!!!

.. rubric:: Source

`CIViC molecular profile id 1150: PIK3CA R38H <https://civicdb.org/molecular-profiles/1150/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Function Variant <FunctionVariant>`

.. rubric:: Properties

``id``: civic.mpid:1150
  CIViC Molecular Profile ID, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: PIK3CA p.R38H
  Following the naming convention used by CIViC.

``description``: A brief placeholder note.
  This field was populated with an example value because CIViC does not provide a longform description.

``aliases``: null
  No aliases included in this example.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`
  The ``allele`` field is populated with the VRS Allele for NM_006218.4:c.113G>A, as included within ``members``.

:ref:`Feature Context Constraint <FeatureContextConstraint>`
  The ``featureContext`` is a :ref:`Mappable Concept <ConceptMapping>` for PIK3CA (hgnc:8975), with a primaryCoding linking to its HGNC entry.

:ref:`Function Constraint <FunctionConstraint>`
  The ``functionConsequence`` is a :ref:`Mappable Concept <ConceptMapping>` for gain of function (SO:0002053), with a primaryCoding linking to the Sequence Ontology term gain_of_function.

.. rubric:: Members

The ``members`` field includes one VRS Allele object generated using the VICC Variation Normalizer for NM_006218.4:c.113G>A, on the MANE Select coding transcript for *PIK3CA* (refseq:NM_006218.4).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/functionVariant-ex3.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/functionVariant-ex3.yaml
  :language: yaml

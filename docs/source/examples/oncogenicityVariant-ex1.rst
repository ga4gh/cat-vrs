:orphan:

.. _OncogenicityVariantEx1:

:doc:`← Back to Examples </examples/index>`

KRAS oncogenic variants
!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC molecular profile 332: KRAS Mutation <https://civicdb.org/molecular-profiles/332/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

This example does not satisfy any :ref:`Recipes`.

.. rubric:: Properties

``id``: civic.mpid:332
  A placeholder identifier for this constructed example.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: KRAS oncogenic variants
  Representing the set of KRAS variants that are classified as oncogenic.

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
  The ``featureContext`` is a :ref:`Mappable Concept <MappableConcept>` for KRAS (hgnc:6407), with a primaryCoding linking to its HGNC entry.

:ref:`Oncogenicity Constraint <OncogenicityConstraint>`
  The ``classification`` is a :ref:`Mappable Concept <MappableConcept>` for Oncogenic (ncit:C229176), with a primaryCoding linking to the NCI Thesaurus term Oncogenic Variant.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/oncogenicityVariant-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/oncogenicityVariant-ex1.yaml
  :language: yaml

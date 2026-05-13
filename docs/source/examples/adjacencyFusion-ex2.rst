:orphan:

.. _AdjacencyFusionEx2:

:doc:`← Back to Examples </examples/index>`

v::NTRK1(hgnc:8031)
!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC feature id 62026: v::NTRK1 Fusion <https://civicdb.org/features/62026/summary>`_

.. rubric:: :ref:`Recipes` that example satisfies

:ref:`Gene Fusion <GeneFusion>`

.. rubric:: Properties

``id``: civic.fid:62026
  CIViC variant id, where fid stands for Feature ID, derived from the Feature ID contained within the CIViC URL for this genomic alteration

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: v::NTRK1(hgnc:8031)
  Human-readable label given to the fusion by CIViC, with gene identifiers per the VICC Fusion representation recommendation. CIViC did not provide identifiers for the genes, so HGNC identifiers were used.

``description``: An optional field to describe this Categorical Variant.
  This field was populated with an example value because CIViC does not provide a longform description.

``aliases``: v::NTRK1, NTRK1 fusion
  CIViC does not provide aliases for this fusion; these were added as examples

``extensions``:  `Known Gene Elements <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_.
  Known Gene Elements as a :ref:`Concept Set <ConceptSet>` of :ref:`Mappable Concepts <ConceptMapping>` for *LMNA*, *TFG*, *TP53*, *TPM3*, and *TPR*.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: :ref:`Constraints`

:ref:`Adjacency Constraint <AdjacencyConstraint>`
  The ``adjoinedElements`` array specifies an ``UnspecifiedElement`` for the uncharacterized fusion partner and *NTRK1* (hgnc:8031) as a mappable concept for the known partner. The ``orderKnown`` field is set to false to reflect that the 5'-to-3' orientation between the partners has not been established.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex2.yaml
  :language: yaml

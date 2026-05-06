:orphan:

.. _AdjacencyFusionEx2:

v::NTRK1(hgnc:8031)
!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC feature id 62026: v::NTRK1 Fusion <https://civicdb.org/features/62026/summary>`_

.. rubric:: :ref:`Recipes` that example satisfies

None

.. rubric:: Properties

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Field
     - Value
     - Description
   * - ``id``
     - civic.fid:62026
     - where fid stands for Feature ID, derived from the Feature ID contained within the CIViC URL for this genomic alteration
   * - ``type``
     - CategoricalVariant
     - as required by the specification
   * - ``name``
     - v::NTRK1(hgnc:8031)
     - Human-readable label given to the fusion by CIViC, with gene identifiers per the VICC Fusion representation recommendation. CIViC did not provide identifiers for the genes, so HGNC identifiers were used
   * - ``description``
     - An optional field to describe v::NTRK1(hgnc:8031)
     - a placeholder since CIViC does not provide a longform description for this fusion
   * - ``aliases``
     - v::NTRK1, NTRK1 fusion
     - CIViC does not provide aliases for this fusion; these were added as examples
   * - ``extensions``
     - Known Gene Elements extension (ConceptSet of LMNA, TFG, TP53, TPM3, TPR)
     - captures a ConceptSet of known possible fusion partners from COSMIC Fusion data with an OR membership operator
   * - ``mappings``
     - --
     - No mappings are included in this example

.. rubric:: :ref:`Constraints`

:ref:`Adjacency Constraint <AdjacencyConstraint>`
   The ``adjoinedElements`` array specifies an ``UnspecifiedElement`` for the uncharacterized fusion partner and NTRK1 (hgnc:8031) as a mappable concept for the known partner. The ``orderKnown`` field is set to false to reflect that the 5'-to-3' orientation between the partners has not been established.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex2.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex2.yaml
   :language: yaml

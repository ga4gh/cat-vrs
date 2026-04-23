:orphan:
.. _AdjacencyFusionEx1:

BCR(ncbi:613)::ABL1(ncbi:25)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Source**: `CIViC variant id 1: BCR::ABL1 Fusion <https://civicdb.org/variants/1/summary>`_

**Recipes that this example satisfies**: :ref:`Gene Fusion <GeneFusion>`

.. rubric:: Attributes

- ``id``: "civic.vid:1", where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.
- ``type``: "CategoricalVariant", as required by the specification.
- ``name``: "BCR(ncbi:613)::ABL1(ncbi:25)", which is the human-readable label given to the fusion by CIViC, with gene identifiers per the VICC Fusion representation recommendation. CIViC provided NCBI identifiers for both genes, so those were used.
- ``description``: "An optional field to describe BCR::ABL1" was used as a placeholder since CIViC does not provide a longform description for this fusion.
- ``aliases``: All aliases for BCR::ABL1 were provided as aliases, as provided by CIViC.
- ``extensions``: The 5' and 3' Partner Representative Genomic Coordinates for BCR::ABL1, as provided by CIViC.
- ``mappings``: No mappings are included in this example.

.. rubric:: Constraints

:ref:`Adjacency Constraint <AdjacencyConstraint>`: Both BCR and ABL1 are modeled as mappable concepts within the ``adjoinedElements`` array, using the NCBI gene identifiers provided by CIViC (ncbi:613 for BCR and ncbi:25 for ABL1). The ``orderKnown`` field is set to true to indicate that the 5'-to-3' orientation of the fusion partners is known.

.. rubric:: Members

The ``members`` field includes a VRS Adjacency object representing the BCR::ABL1 gene fusion using illustrative transcript breakpoint coordinates. Specifically, it encodes NM_004327.4:r.1_3533::NM_005157.6:r.461_5766, using the MANE Select transcripts for BCR (NM_004327.4) and ABL1 (NM_005157.6).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex1.yaml
   :language: yaml

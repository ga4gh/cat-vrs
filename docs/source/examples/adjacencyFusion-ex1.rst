:orphan:

.. _AdjacencyFusionEx1:

:doc:`← Back to Examples </examples/index>`

BCR(ncbi:613)::ABL1(ncbi:25)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC variant id 1: BCR::ABL1 Fusion <https://civicdb.org/variants/1/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Gene Fusion <GeneFusion>`

.. rubric:: Properties

``id``: civic.vid:1
  CIViC Variant ID, where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: BCR(ncbi:613)::ABL1(ncbi:25)
  Human-readable label given to the fusion by CIViC, with gene identifiers per the VICC Fusion representation recommendation. CIViC provided NCBI identifiers for both genes, so those were used.

``description``: An optional field to describe this Categorical Variant.
  This field was populated with an example value because CIViC does not provide a longform description.

``aliases``: BCR::ABL1, t(9;22)(q34;q11), BCR-ABL1, BCR--ABL1, BCR-ABL, BCR(hgnc:1014)::ABL1(hgnc:76)
  All aliases, as provided by CIViC, were included.

``extensions``: CIViC 5' and 3' Partner Representative Genomic Coordinates for BCR::ABL1
  CIViC provided these values within the variant object, so we included them here as :ref:`extensions <Extension>` to because the :ref:`data model <data-model>` does not explicitly support them.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: :ref:`Constraints`

:ref:`Adjacency Constraint <AdjacencyConstraint>`
  Both *BCR* and *ABL1* are modeled as mappable concepts within the ``adjoinedElements`` array, using the NCBI gene identifiers provided by CIViC (ncbi:613 for *BCR* and ncbi:25 for *ABL1*). The ``orderKnown`` field is set to true to indicate that the 5'-to-3' orientation of the fusion partners is known.

.. rubric:: Members

The ``members`` field includes a :ref:`VRS Adjacency <Adjacency>` object representing the BCR::ABL1 gene fusion using illustrative transcript breakpoint coordinates. Specifically, it encodes NM_004327.4:r.1_3533::NM_005157.6:r.461_5766, using the MANE Select transcripts for *BCR* (NM_004327.4) and *ABL1* (NM_005157.6).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex1.yaml
  :language: yaml

:orphan:
.. _AdjacencyFusionEx3:

?::ZNF384(ncbi:171017)
!!!!!!!!!!!!!!!!!!!!!!

**Source**: `CIViC variant id 5186: ?::ZNF384 Fusion <https://civicdb.org/variants/5186/summary>`_

**Recipes that this example satisfies**: None

.. rubric:: Attributes

- ``id``: civic.vid:5186, where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: ?::ZNF384(ncbi:171017), the human-readable label given to the fusion by CIViC, with gene identifiers per the VICC Fusion representation recommendation. CIViC provided NCBI identifiers for the genes, so those were used.
- ``description``: "An optional field to describe ?::ZNF384(ncbi:171017)", a placeholder since CIViC does not provide a longform description for this fusion.
- ``aliases``: CIViC provides "ZNF384 Fusion" as an alias for this fusion; ?::ZNF384 was also added as an example alias.
- ``extensions``: No extensions are included in this example.
- ``mappings``: No mappings are included in this example.

.. rubric:: Constraints

:ref:`Adjacency Constraint <AdjacencyConstraint>`: The ``adjoinedElements`` array specifies an ``UnspecifiedElement`` for the unknown 5' partner and ZNF384 (ncbi:171017) as a mappable concept for the 3' partner. The ``orderKnown`` field is set to true to indicate that ZNF384 is the known 3' partner in this fusion.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex3.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex3.yaml
   :language: yaml

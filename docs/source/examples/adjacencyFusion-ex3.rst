:orphan:

.. _AdjacencyFusionEx3:

:doc:`← Back to Examples </examples/index>`

?::ZNF384(ncbi:171017)
!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC variant id 5186: ?::ZNF384 Fusion <https://civicdb.org/variants/5186/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

None

.. rubric:: Properties

``id``: civic.vid:5186
   CIViC Variant ID from the source URL.

``type``: CategoricalVariant
   This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: ?::ZNF384(ncbi:171017)
   Human-readable label; NCBI identifiers used per VICC Fusion recommendation.

``description``: null
   No description text included.

``aliases``: ZNF384 Fusion, ?::ZNF384
   CIViC provides "ZNF384 Fusion" as an alias.

``extensions``: null
   No :ref:`extensions <Extension>` included.

``mappings``: null
   No :ref:`mappings <ConceptMapping>` included.

.. rubric:: :ref:`Constraints`

:ref:`Adjacency Constraint <AdjacencyConstraint>`
   The ``adjoinedElements`` array specifies an :ref:`Unspecified Element <UnspecifiedElement>` for the unknown 5' partner and ZNF384 (ncbi:171017) as a mappable concept for the 3' partner. The ``orderKnown`` field is set to true to indicate that ZNF384 is the known 3' partner in this fusion.

.. rubric:: Members

This example does not include :ref:`Members <CategoricalVariant>` .

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex3.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex3.yaml
   :language: yaml

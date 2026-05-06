:orphan:

.. _AdjacencyFusionEx3:

?::ZNF384(ncbi:171017)
!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC variant id 5186: ?::ZNF384 Fusion <https://civicdb.org/variants/5186/summary>`_

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
     - civic.vid:5186
     - CIViC Variant ID from the source URL
   * - ``type``
     - CategoricalVariant
     - Required by the specification
   * - ``name``
     - ?::ZNF384(ncbi:171017)
     - Human-readable label; NCBI identifiers used per VICC Fusion recommendation
   * - ``description``
     - --
     - No description text included
   * - ``aliases``
     - ZNF384 Fusion, ?::ZNF384
     - CIViC provides "ZNF384 Fusion" as an alias
   * - ``extensions``
     - --
     - No :ref:`extensions <Extension>` included
   * - ``mappings``
     - --
     - No :ref:`mappings <ConceptMapping>` included

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

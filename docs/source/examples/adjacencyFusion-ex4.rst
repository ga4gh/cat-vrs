:orphan:

.. _AdjacencyFusionEx4:

:doc:`← Back to Examples </examples/index>`

FGFR2(hgnc:3689)::v
!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`CIViC variant id 2202: FGFR2::v Fusion <https://civicdb.org/variants/2202/summary>`_

.. rubric:: :ref:`Recipes` that example satisfies

:ref:`Gene Fusion <GeneFusion>`

.. rubric:: Properties

``id``: civic.vid:2202
  CIViC Variant ID, where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: FGFR2(hgnc:3689)::v
  Human-readable label given to the fusion by CIViC, with gene identifiers per the VICC Fusion representation recommendation.

``description``: An FGFR2 gene fusion, where the FGFR2 kinase domain is required to remain intact to satisfy the constraints of this categorical variant.
  This field was populated with the description provided by CIViC.

``aliases``: FGFR2::v, FGFR2 fusion
  An alias provided by CIViC the ``name`` without HGNC ids were included as example aliases.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: :ref:`Constraints`

:ref:`Adjacency Constraint <AdjacencyConstraint>`
  *FGFR2* (hgnc:3689) is modeled as a mappable concept as the 5' partner within the ``adjoinedElements`` array, with an :ref:`Unspecified Element <UnspecifiedElement>` serving as the unknown 3' partner. The ``orderKnown`` field is set to true. Additionally, the ``functionalDomains`` field specifies two domains that must carry a preserved status: the FGFR2 protein tyrosine kinase domain (amino acids 456–768 of the protein product NP_000132.3), and the kinase domain on the MANE Select coding transcript (positions 1999–2937 of NM_000141.5). Any variant satisfying this categorical variant must leave both of these domains intact.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex4.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex4.yaml
  :language: yaml

:orphan:
.. _AdjacencyFusionEx4:

FGFR2(hgnc:3689)::v
!!!!!!!!!!!!!!!!!!!

**Source**: `CIViC variant id 2202: FGFR2::v Fusion <https://civicdb.org/variants/2202/summary>`_

**Recipes that this example satisfies**: None

.. rubric:: Attributes

- ``id``: civic.vid:2202, where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: FGFR2(hgnc:3689)::v, with the FGFR2 gene identifier per the VICC Fusion representation recommendation using the HGNC identifier.
- ``description``: "An FGFR2 gene fusion, where the FGFR2 kinase domain is required to remain intact to satisfy the constraints of this categorical variant."
- ``aliases``: FGFR2::v and FGFR2 fusion are included as aliases.
- ``extensions``: No extensions are included in this example.
- ``mappings``: No mappings are included in this example.

.. rubric:: Constraints

:ref:`Adjacency Constraint <AdjacencyConstraint>`: FGFR2 (hgnc:3689) is modeled as a mappable concept as the 5' partner within the ``adjoinedElements`` array, with an ``UnspecifiedElement`` serving as the unknown 3' partner. The ``orderKnown`` field is set to true. Additionally, the ``functionalDomains`` field specifies two domains that must carry a preserved status: the FGFR2 protein tyrosine kinase domain (amino acids 456–768 of the protein product NP_000132.3) and the kinase domain on the MANE Select coding transcript (positions 1999–2937 of NM_000141.5). Any variant satisfying this categorical variant must leave both of these domains intact.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/adjacencyFusion-ex4.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/adjacencyFusion-ex4.yaml
   :language: yaml

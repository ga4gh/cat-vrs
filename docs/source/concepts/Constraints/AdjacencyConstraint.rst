.. _AdjacencyConstraint:

Adjacency Constraint
!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/AdjacencyConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BCR(ncbi:613)::ABL1(ncbi:25) <AdjacencyFusionEx1>`
- :ref:`v::NTRK1(hgnc:8031) <AdjacencyFusionEx2>`
- :ref:`?::ZNF384(ncbi:171017) <AdjacencyFusionEx3>`
- :ref:`FGFR2(hgnc:3689)::v <AdjacencyFusionEx4>`

A representative example of this Constraint, from :ref:`BCR(ncbi:613)::ABL1(ncbi:25) <AdjacencyFusionEx1>`:

.. literalinclude:: ../../../../examples/json/adjacencyFusion-ex1.json
  :language: json
  :lines: 39-72

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

The Adjacency Constraint is similar to `VRS' Adjacency class <https://vrs.ga4gh.org/en/stable/concepts/MolecularVariation/Adjacency.html>`_, except that the `adjoinedElements` field supports data types in addition to :ref:`iriReference` and :ref:`Location`. Specifically:

* :ref:`MappableConcept` to include an element that represents a Gene.
* :ref:`Terminus` to include an element that represents the end of a molecule.
* :ref:`UnspecifiedElement` to include an element that is otherwise unspecified. For example, if an assay is unable to determine a fusion partner.

Genes
#####

.. include:: ../../_includes/_guidance_feature_context_genes.rst

VRS Sequence Locations
######################

.. include:: ../../_includes/_guidance_generate_sequence_location_text.rst

.. include:: ../../_includes/_guidance_generate_sequence_location_box.rst

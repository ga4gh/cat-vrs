.. _GeneFusion:

Gene Fusion
!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/GeneFusion.rst

A GeneFusion is a :ref:`CategoricalVariant` with at least one constraint:

1. An :ref:`AdjacencyConstraint` with the `adjoinedElements` array containing either an :ref:`iriReference`, :ref:`MappableConcept`, :ref:`Location`, or an :ref:`UnspecifiedElement` as elements.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`?::ZNF384(ncbi:171017) <AdjacencyFusionEx3>`
- :ref:`BCR(ncbi:613)::ABL1(ncbi:25) <AdjacencyFusionEx1>`
- :ref:`FGFR2(hgnc:3689)::v <AdjacencyFusionEx4>`
- :ref:`v::NTRK1(hgnc:8031) <AdjacencyFusionEx2>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

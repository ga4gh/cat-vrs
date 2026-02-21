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
The following are example implementations of that satisfy the Gene Fusion recipe:

.. collapse:: BCR(ncbi:613)::ABL1(ncbi:25)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex1
      :language: json

.. collapse:: v::NTRK1(hgnc:8031)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex2
      :language: json

.. collapse:: ?::ZNF384(ncbi:171017)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex3
      :language: json

.. collapse:: FGFR2(hgnc:3689)::v

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex4
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

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

   .. literalinclude:: ../../../../examples/json/adjacencyFusion-ex1.json
      :language: json

.. collapse:: v::NTRK1(hgnc:8031)

   .. literalinclude:: ../../../../examples/json/adjacencyFusion-ex2.json
      :language: json

.. collapse:: ?::ZNF384(ncbi:171017)

   .. literalinclude:: ../../../../examples/json/adjacencyFusion-ex3.json
      :language: json

.. collapse:: FGFR2(hgnc:3689)::v

   .. literalinclude:: ../../../../examples/json/adjacencyFusion-ex4.json
      :language: json

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

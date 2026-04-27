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

We recommend following the `Variant Interpretation for Cancer Consortium's Gene Fusion Specification <https://fusions.cancervariants.org/en/latest/>`_ when modeling a Gene Fusion with the :ref:`Adjacency Constraint<AdjacencyConstraint>`. Specifically by:

* Representing `Named Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#named-gene-component>`_ as a :ref:`MappableConcept` with the `conceptType` field set to "Gene"; the `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ can help.
* Representing `Multiple Possible Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ as a :ref:`UnspecifiedElement` within the Adjacency Constraint. An exhaustive or non-exhaustive list of possible elements can be included as an :ref:`Extension`. We recommend setting the value to be a :ref:`ConceptSet` with the `membershipOperator` field set to "OR".
* Representing an `Unknown Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#unknown-gene-component>`_ as a :ref:`UnspecifiedElement`.

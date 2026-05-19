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
The Adjacency Constraint is similar to `VRS' Adjacency class <https://vrs.ga4gh.org/en/stable/concepts/MolecularVariation/Adjacency.html>`_, except that the `adjoinedElements` field supports data types in addition to :ref:`iriReference` and :ref:`Location`.

We recommend following the `Variant Interpretation for Cancer Consortium's Gene Fusion Specification <https://fusions.cancervariants.org/en/latest/>`_ when modeling a :ref:`GeneFusion` using this constraint. Specifically by:

* Representing `Named Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#named-gene-component>`_ as a :ref:`MappableConcept` with the `conceptType` field set to "Gene"; the `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ can help.
* Representing `Multiple Possible Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ as a :ref:`UnspecifiedElement` within the Adjacency Constraint. An exhaustive or non-exhaustive list of possible elements can be included as an :ref:`Extension`. We recommend setting the value to be a :ref:`ConceptSet` with the `membershipOperator` field set to "OR".
* Representing an `Unknown Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#unknown-gene-component>`_ as a :ref:`UnspecifiedElement`.

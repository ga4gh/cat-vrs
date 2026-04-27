.. _AdjacencyConstraint:

Adjacency Constraint
!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/AdjacencyConstraint.rst

Examples
@@@@@@@@
The following are example implementations of AdjacencyConstraint:

.. collapse:: BCR(ncbi:613)::ABL1(ncbi:25)

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_adjacencyFusion-ex1
      :language: json
      :lines: 42-75

.. collapse:: v::NTRK1(hgnc:8031)

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_adjacencyFusion-ex2
      :language: json
      :lines: 15-37

.. collapse:: ?::ZNF384(ncbi:171017)

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_adjacencyFusion-ex3
      :language: json
      :lines: 15-37

.. collapse:: FGFR2(hgnc:3689)::v

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_adjacencyFusion-ex4
      :language: json
      :lines: 15-88

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@
The Adjacency Constraint is similar to `VRS' Adjacency class <https://vrs.ga4gh.org/en/stable/concepts/MolecularVariation/Adjacency.html>`_, except that the `adjoinedElements` field supports data types in addition to :ref:`iriReference` and :ref:`Location`. Specifically:

* :ref:`MappableConcept` to include an element that represents as Gene.
* :ref:`Terminus` to include an element that represents the end of a molecule.
* :ref:`UnspecifiedElement` to include an element that is otherwise unspecified. For example, if an assay is unable to determine a fusion partner.

Genes
#####

We recommend specifying *conceptType* as "Gene" and using a symbol from the `HUGO Gene Nomenclature Committee (HGNC) <https://www.genenames.org>`_ as a :ref:`primaryCoding <Coding>`.

The `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ is Python package and public REST instance that can be used to obtain :ref:`Codings <Coding>` and :ref:`Concept Mappings <ConceptMapping>` of gene concepts based on `Ensembl, NCBI Gene, HGNC, and other data sources <https://gene-normalizer.readthedocs.io/latest/normalizing_data/sources.html>`_.

VRS Sequence Locations
######################



We recommend following the `Variant Interpretation for Cancer Consortium's Gene Fusion Specification <https://fusions.cancervariants.org/en/latest/>`_ when modeling a :ref:`GeneFusion` using this constraint. Specifically by:

* Representing `Named Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#named-gene-component>`_ as a :ref:`MappableConcept` with the `conceptType` field set to "Gene"; the `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ can help.
* Representing `Multiple Possible Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ as a :ref:`UnspecifiedElement` within the Adjacency Constraint. An exhaustive or non-exhaustive list of possible elements can be included as an :ref:`Extension`. We recommend setting the value to be a :ref:`ConceptSet` with the `membershipOperator` field set to "OR".
* Representing an `Unknown Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#unknown-gene-component>`_ as a :ref:`UnspecifiedElement`.

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

Constraints
###########

We recommend following the `Variant Interpretation for Cancer Consortium (VICC)'s Gene Fusion Specification <https://fusions.cancervariants.org/en/latest/>`_ when modeling a Gene Fusion with the :ref:`Adjacency Constraint<AdjacencyConstraint>`. Specifically by:

* Representing `Named Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#named-gene-component>`_ as a :ref:`MappableConcept` with the `conceptType` field set to "Gene"; the `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ can help.
* Representing `Multiple Possible Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ as an :ref:`UnspecifiedElement` within the Adjacency Constraint. An exhaustive or non-exhaustive list of possible elements can be included as an :ref:`Extension`. We recommend setting the value to be a :ref:`ConceptSet` with the `membershipOperator` field set to "OR".
* Representing an `Unknown Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#unknown-gene-component>`_ as an :ref:`UnspecifiedElement`.

While they do not currently utilize Cat-VRS, the VICC `FUSOR <https://github.com/cancervariants/fusor>` and `FUSOR-Builder <https://github.com/cancervariants/fusion-builder>` tools can assist with representing Gene Fusions according to the VICC Gene Fusion Specification.

Members
#######

When modeling a Gene Fusion, *members* may be populated with VRS :ref:`Adjacency` objects, where the *adjoinedSequences* property can be populated with two VRS objects that are either:

- :ref:`iriReferences <iriReference>`
- :ref:`Sequence Locations <Location>`

VRS' `Implementation Guidance for Adjacency objects <https://vrs.ga4gh.org/en/latest/concepts/MolecularVariation/Adjacency.html>`_ contains guidance on sequence locations and directionality, normalization, and linker sequences.

.. include:: ../../_includes/_guidance_generate_sequence_location_text.rst

.. include:: ../../_includes/_guidance_generate_sequence_location_box.rst

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

* :ref:`MappableConcept` to include an element that represents as Gene.
* :ref:`Terminus` to include an element that represents the end of a molecule.
* :ref:`UnspecifiedElement` to include an element that is otherwise unspecified. For example, if an assay is unable to determine a fusion partner.

Genes
#####

We recommend specifying *conceptType* as "Gene" and using a symbol from the `HUGO Gene Nomenclature Committee (HGNC) <https://www.genenames.org>`_ as a :ref:`primaryCoding <Coding>`.

The `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ is Python package and public REST instance that can be used to obtain :ref:`Codings <Coding>` and :ref:`Concept Mappings <ConceptMapping>` of gene concepts based on `Ensembl, NCBI Gene, HGNC, and other data sources <https://gene-normalizer.readthedocs.io/latest/normalizing_data/sources.html>`_.

VRS Sequence Locations
######################

We recommend the following resources for constructing :ref:`Sequence Location <SequenceLocation>` objects:

- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate a VRS digest for a given sequence location.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Allele objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Location`` exists upon. Consider the following values, depending on the type of ``Location`` expressed:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Location type
     - moleculeType
     - residueAlphabet
   * - Nucleotide
     - genomic
     - na
   * - RNA
     - RNA
     - na
   * - mRNA
     - mRNA
     - na
   * - Protein
     - protein
     - aa

For additional Implementation Guidance, please visit `VRS' page for the Sequence Location concept <https://vrs.ga4gh.org/en/latest/concepts/LocationAndReference/SequenceLocation.html>`_.

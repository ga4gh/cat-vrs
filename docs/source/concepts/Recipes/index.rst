.. _Recipes:

Recipes
!!!!!!!

A *Recipe* is not a class. It is a term defined to differentiate between a
specialized CategoricalVariant and a general CategoricalVariant. These
recipes are pre-defined CategoricalVariants with specific constraints
that represent standard categorical variants that have been identified
in variant knowledgebases and registries. Implementers are encouraged
to use the recipes that exist whenever possible, but are free to create
new recipes as needed in a given implementation. New recipes should be
shared with the community on the |catvrs_discussion| board.

.. toctree::
   :titlesonly:
   :hidden:

   CanonicalAllele
   CategoricalCnv
   CompoundHeterozygote
   Diplotype
   FunctionVariant
   GeneFusion
   ProteinSequenceConsequence
   StarAllele

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Recipe
     - Used to represent
     - :ref:`Representative example <Examples>`
   * - :ref:`Canonical Allele <CanonicalAllele>`
     - Genomic sequence variants
     - :ref:`NC_000001.11:g.1699974C>G <CanonicalAlleleEx2>`
   * - :ref:`Categorical CNV <CategoricalCnv>`
     - Copy number variants
     - :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <CategoricalCnvEx1>`
   * - :ref:`Compound Heterozygote <CompoundHeterozygote>`
     - Two different variant haplotypes of a gene in trans
     - :ref:`NM_000094.4(COL7A1):c.[425A>G];[4333G>A] <CompoundHetEx1>`
   * - :ref:`Diplotype <Diplotype>`
     - Two star alleles of a gene in trans
     - :ref:`CYP2C19*1/*17 <DiplotypeEx1>`
   * - :ref:`Function Variant <FunctionVariant>`
     - Functional impact categories
     - :ref:`BRCA2 loss of function variants <FunctionVariantEx2>`
   * - :ref:`Gene Fusion <GeneFusion>`
     - Gene fusions
     - :ref:`BCR(ncbi:613)::ABL1(ncbi:25) <AdjacencyFusionEx1>`
   * - :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`
     - Amino acid sequence variants
     - :ref:`NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter) <ProteinSequenceConsequenceEx2>`
   * - :ref:`Star Allele <StarAllele>`
     - Haplotypes defined by variants in cis
     - :ref:`CYP2C9*2 <StarAlleleEx1>`

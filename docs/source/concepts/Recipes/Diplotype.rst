.. _Diplotype:

Diplotype
!!!!!!!!!

Description
@@@@@@@@@@@

A diplotype is the pair of star alleles of a gene that an individual carries, one on each homologous chromosome (in trans). Diplotypes are written as two star alleles separated by a slash, such as *CYP2C19*\*1/\*17, and are commonly used to assign pharmacogenomic phenotypes such as metabolizer status. Either star allele may be the reference \*1 allele, and the two star alleles may be the same (e.g. \*17/\*17).

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/Diplotype.rst

A Diplotype is a :ref:`CompositeCategoricalVariant` with:

1. An `operator` of `AND` and a `phaseRelation` of `trans`.
2. Exactly two `elements`, each of which satisfies the :ref:`StarAllele` Recipe: a :ref:`CompositeCategoricalVariant` with an `operator` of `AND`, a `phaseRelation` of `cis`, and one or more :ref:`CategoricalVariantCriterion` `elements` with a `presence` of `present`.

Examples
@@@@@@@@

The following :ref:`example Composite Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`CYP2C19*1/*17 <DiplotypeEx1>`

  - The \*1 star allele is represented by the reference base at the \*17 defining position.

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Elements
########

Each of the two `elements` is a :ref:`Star Allele <StarAllele>`, represented as a :ref:`CompositeCategoricalVariant` with a `phaseRelation` of `cis` even when it is defined by a single variant. Both star alleles must be of the same gene. This requirement cannot be expressed in JSON Schema and is therefore not enforced by validation; implementers are responsible for ensuring it.

Reference alleles
#################

When one of the star alleles is \*1, represent it by the reference state at the defining positions of the other star allele, or of all positions that were assessed. See :ref:`Star Allele <StarAllele>` for details.

Diplotypes and compound heterozygotes
#####################################

A :ref:`Compound Heterozygote <CompoundHeterozygote>` and a Diplotype both join two haplotypes in trans, but they differ:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * -
     - Diplotype
     - Compound Heterozygote
   * - Haplotypes may be reference (e.g. \*1)
     - Yes
     - No
   * - Haplotypes may be identical (e.g. \*17/\*17)
     - Yes
     - No
   * - Single-variant haplotype
     - :ref:`Star Allele <StarAllele>` with one element
     - :ref:`CategoricalVariantCriterion`

A Diplotype in which both star alleles carry variants and differ from each other describes a compound heterozygous genotype. It may be represented with either Recipe, but the two representations differ in shape when a haplotype is defined by a single variant, so a single object will generally satisfy only one of them.

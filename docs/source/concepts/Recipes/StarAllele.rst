.. _StarAllele:

Star Allele
!!!!!!!!!!!

Description
@@@@@@@@@@@

A star allele is a named haplotype of a single gene, most commonly a pharmacogene, defined by one or more variants that occur together on the same chromosome (in cis). Star alleles are named with the gene symbol followed by an asterisk and a number, such as *CYP2C9*\*2, and are catalogued, along with their clinical function, by resources such as `ClinPGx <https://www.clinpgx.org>`_. Some star alleles are defined by a single core variant, such as *CYP2C9*\*2 (c.430C>T), while others are defined by several variants, such as *CYP2C19*\*2 (c.[332-23A>G;681G>A]). The \*1 allele is conventionally the reference haplotype.

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/StarAllele.rst

A StarAllele is a :ref:`CompositeCategoricalVariant` with:

1. An `operator` of `AND` and a `phaseRelation` of `cis`.
2. One or more `elements`, each of which is a :ref:`CategoricalVariantCriterion` with a `presence` of `present`.

Examples
@@@@@@@@

The following :ref:`example Composite Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`CYP2C9*2 <StarAlleleEx1>`

  - A star allele defined by a single core variant.

Each of the two elements of the :ref:`CYP2C19*1/*17 <DiplotypeEx1>` :ref:`Diplotype` example also satisfies this Recipe.

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Elements
########

Represent a star allele as a :ref:`CompositeCategoricalVariant` with a `phaseRelation` of `cis` even when it is defined by a single variant, so that every star allele has the same structure. Each element is a :ref:`CategoricalVariantCriterion` whose subject defines one of the star allele's variants; elements may not be further nested.

Core and sub-allele definitions
###############################

A star allele is defined by its *core* variants, which change function, while its sub-alleles (e.g. \*2.001, \*2.002) carry additional variants. Resources such as `ClinPGx <https://www.clinpgx.org>`_ provide star allele definitions. Include the variants that match the definition being represented, and document that choice in the `description`. Definitions vary between resources; for example, ClinVar's `CYP2C9*2 <https://www.ncbi.nlm.nih.gov/clinvar/variation/177709/>`_ haplotype also asserts the reference base at the \*3 position.

Reference alleles
#################

The \*1 allele is defined by the absence of the variants that define other star alleles, which cannot be enumerated in general. Represent \*1 by the reference state at the defining positions that were assessed, using VRS ``Allele`` objects with a reference state (e.g. ``NC_000010.11:g.94761900=``), as shown in the :ref:`CYP2C19*1/*17 <DiplotypeEx1>` example. Each criterion asserts that the reference base is **present**, rather than that a variant is absent.

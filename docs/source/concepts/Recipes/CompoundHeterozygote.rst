.. _CompoundHeterozygote:

Compound Heterozygote
!!!!!!!!!!!!!!!!!!!!!

Description
@@@@@@@@@@@

A compound heterozygote is the presence of two different variant haplotypes of the same gene, one on each homologous chromosome (in trans). Each haplotype is either a single Categorical Variant or, when a haplotype is defined by more than one variant, a nested Composite Categorical Variant whose elements are in cis. The two haplotypes are expected to differ; if they are identical, the genotype is homozygous rather than compound heterozygous. Variants are not restricted by type (e.g. SNVs, indels, and copy number changes are all permitted).

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CompoundHeterozygote.rst

A CompoundHeterozygote is a :ref:`CompositeCategoricalVariant` with:

1. An `operator` of `AND` and a `phaseRelation` of `trans`.
2. Exactly two `elements`, each of which is one of:

   a. A :ref:`CategoricalVariantCriterion` with a `presence` of `present`, for a haplotype defined by a single variant.
   b. A :ref:`CompositeCategoricalVariant` with an `operator` of `AND`, a `phaseRelation` of `cis`, and two or more :ref:`CategoricalVariantCriterion` `elements` with a `presence` of `present`, for a haplotype defined by more than one variant.

Examples
@@@@@@@@

The following :ref:`example Composite Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`NM_000094.4(COL7A1):c.[425A>G];[4333G>A] <CompoundHetEx1>`

  - Each haplotype is defined by a single variant, so both elements are Categorical Variant Criteria.
- :ref:`NM_003661.3:c.[1024A>G;1152T>G];[1164_1169delTTATAA] <CompoundHetEx2>`

  - The APOL1 G1 haplotype is defined by two variants in cis, so it is a nested Composite Categorical Variant. The APOL1 G2 haplotype is a single deletion.

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Elements
########

Each of the two `elements` represents one haplotype. Represent a haplotype defined by a single variant directly as a :ref:`CategoricalVariantCriterion`, rather than wrapping it in a :ref:`CompositeCategoricalVariant` with one element. Represent a haplotype defined by more than one variant as a :ref:`CompositeCategoricalVariant` with a `phaseRelation` of `cis`; its `elements` must be :ref:`Categorical Variant Criteria <CategoricalVariantCriterion>` and may not be further nested.

Every :ref:`CategoricalVariantCriterion` within a Compound Heterozygote must have a `presence` of `present`. Any type of :ref:`CategoricalVariant` may be the subject of a criterion, including those that satisfy other :ref:`Recipes`, such as a :ref:`Canonical Allele <CanonicalAllele>` or :ref:`Categorical CNV <CategoricalCnv>`.

The two `elements` must represent different haplotypes. If both elements represent the same haplotype, the genotype is homozygous, not compound heterozygous. This requirement cannot be expressed in JSON Schema and is therefore not enforced by validation; implementers are responsible for ensuring it.

Phase
#####

A `phaseRelation` of `trans` asserts that the two haplotypes occur on different molecules. Only use this Recipe when phase has been established or asserted by the source, for example by a ClinVar record using the ``c.[A];[B]`` HGVS notation. When the phase of two variants is not known, use a :ref:`CompositeCategoricalVariant` with a `phaseRelation` of `unknown` instead.

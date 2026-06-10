.. _FunctionVariant:

Function Variant
!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/FunctionVariant.rst

The FunctionVariant is a :ref:`CategoricalVariant` with at least two constraints:

1. A :ref:`FunctionConstraint`.
2. A :ref:`DefiningAlleleConstraint`, :ref:`DefiningLocationConstraint`, or :ref:`FeatureContextConstraint`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`BRCA2 loss of function variants <FunctionVariantEx2>`
- :ref:`NRAS functionally normal variants <FunctionVariantEx1>`
- :ref:`PIK3CA p.R38H <FunctionVariantEx3>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Constraints
###########

Categorical Variants that are intended to represent Function Variants must contain **at least** two constraints. First, a :ref:`FunctionConstraint` is **required** to associate a Categorical Variant with a known functional impact.

.. note:: If your implementation also uses the `Variant Annotation Specification <https://va-spec.ga4gh.org/en/stable/#>`_, consider associating the Categorical Variant with a Genomic Knowledge Statement based on an `Experimental Variant Functional Impact <https://va-spec.ga4gh.org/en/stable/va-standard-profiles/base-profiles/proposition-profiles.html#experimental-variant-functional-impact-proposition>`_.

.. include:: ../../_includes/_guidance_function_consequence.rst

Second, a :ref:`VRS Allele <Allele>` or :ref:`Sequence Location <SequenceLocation>` can be associated with the Categorical Variant using a :ref:`Defining Allele <DefiningAlleleConstraint>` or :ref:`Defining Location <DefiningLocationConstraint>` Constraint, respectively. We recommend the following resources for constructing VRS objects:

- The `Variant Normalizer <https://variation-normalizer.readthedocs.io>`_ is a Python package and
  public REST instance that translates plain-text HGVS expressions into `Normalized VRS Allele
  objects <https://vrs.ga4gh.org/en/latest/conventions/normalization.html#allele-normalization>`_. Genomic coordinates default to GRCh38 unless otherwise specified.
- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate a VRS digest for an Allele, Sequence Location, and Sequence Reference, and other VRS concepts.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Sequence Reference objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Allele`` exists on. Consider the following values, depending on the type of ``Allele`` expressed:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Allele type
     - moleculeType
     - residueAlphabet
   * - Genomic DNA
     - genomic
     - na
   * - RNA (pre-mRNA)
     - RNA
     - na
   * - mRNA
     - mRNA
     - na
   * - Protein
     - protein
     - aa

Alternatively or in addition to a :ref:`Defining Allele <DefiningAlleleConstraint>` or :ref:`Defining Location <DefiningLocationConstraint>`, a :ref:`Feature Context Constraint <FeatureContextConstraint>` can be applied to associate a Gene with a Categorical Variant. Within the Feature Context Constraint, the *featureContext* attribute is required and is a :ref:`MappableConcept`, meaning that it should be represented using a term from an externally defined ontology.

.. include:: ../../_includes/_guidance_feature_context_genes.rst

.. note:: Implementers use this constraint to represent genes, but it can also be used to represent protein markers, variant consequences, and other genomic features. If you are using this constraint for uses other than to represent genes, please `let us know <https://github.com/ga4gh/cat-vrs/discussions/new?category=show-and-tell>`_!

Members
#######

When modeling a Function Variant, *members* may be populated with VRS :ref:`Alleles <Allele>` or :ref:`Sequence Location <SequenceLocation>` objects that satisfy:

- The :ref:`Allele <Allele>` specified within the :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`.
- The :ref:`Sequence Location <SequenceLocation>` specified within the :ref:`Defining Location Constraint <DefiningLocationConstraint>`, and the associated *matchCharacteristic*.

As is the case with constructing VRS objects for usage within Constraints, we recommend the `Variant Normalizer <https://variation-normalizer.readthedocs.io>`_, `vrs-python <https://github.com/ga4gh/vrs-python>`_, and `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ as resources for constructing VRS objects. Likewise, we recommend populating both the *molecularType* and *residueAlphabet* attributes of the :ref:`Sequence Reference <SequenceReference>` for any ``Allele`` or ``Location`` listed as a member.

.. warning:: If representing a Function Variant with only a Feature Context Constraint to represent a gene, *members* may also be added based on the gene's associated Sequence Location. Gene representation is an area of discussion amongst Genomic Knowledge Standards broadly.

.. _PathogenicityConstraint:

Pathogenicity Constraint
!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/PathogenicityConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BRCA1 likely pathogenic variants <PathogenicityVariantEx1>`
- :ref:`NM_004985.5(KRAS):c.34G>T (p.Gly12Cys) <OncogenicityPathogenicityVariantEx1>`
- :ref:`NM_007294.4(BRCA1):c.5503C>T (p.Arg1835Ter) <PathogenicityVariantEx2>`

A representative example of this Constraint, from :ref:`BRCA1 likely pathogenic variants <PathogenicityVariantEx1>`:

.. literalinclude:: ../../../../examples/json/pathogenicityVariant-ex1.json
  :language: json
  :lines: 25-47

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used in two circumstances:

1. To define a Categorical Variant, such as a :ref:`Canonical Allele <CanonicalAllele>` or :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`, with a known pathogenicity classification. For example, :ref:`NM_007294.4(BRCA1):c.5503C>T (p.Arg1835Ter) <PathogenicityVariantEx2>`, as classified by ClinVar.

   .. note:: If your implementation also uses the `Variant Annotation Specification <https://va-spec.ga4gh.org/en/stable/#>`_, consider associating the Categorical Variant with a Genomic Knowledge Statement based on a `Variant Pathogenicity Proposition <https://va-spec.ga4gh.org/en/stable/va-standard-profiles/base-profiles/proposition-profiles.html#variant-pathogenicity-proposition>`_.

2. When broadly defining a Categorical Variant that can be satisfied by many possible variants, as long as they are described using this Constraint and the same associated classification. For example, *BRCA1* likely pathogenic variants, as :ref:`shown in the Examples <PathogenicityVariantEx1>`.

This Constraint may be used alongside an :ref:`Oncogenicity Constraint <OncogenicityConstraint>` when a variant has both a pathogenicity and an oncogenicity classification, as in :ref:`NM_004985.5(KRAS):c.34G>T (p.Gly12Cys) <OncogenicityPathogenicityVariantEx1>`.

classification
##############

.. include:: ../../_includes/_guidance_classification_pathogenicity.rst

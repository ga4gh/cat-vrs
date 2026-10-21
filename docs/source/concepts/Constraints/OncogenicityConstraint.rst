.. _OncogenicityConstraint:

Oncogenicity Constraint
!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/OncogenicityConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`KRAS oncogenic variants <OncogenicityVariantEx1>`
- :ref:`NM_004985.5(KRAS):c.34G>T (p.Gly12Cys) <OncogenicityPathogenicityVariantEx1>`

A representative example of this Constraint, from :ref:`KRAS oncogenic variants <OncogenicityVariantEx1>`:

.. literalinclude:: ../../../../examples/json/oncogenicityVariant-ex1.json
  :language: json
  :lines: 25-44

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used in two circumstances:

1. To define a Categorical Variant, such as a :ref:`Canonical Allele <CanonicalAllele>` or :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`, with a known oncogenicity classification. For example, :ref:`NM_004985.5(KRAS):c.34G>T (p.Gly12Cys) <OncogenicityPathogenicityVariantEx1>`, as classified by ClinVar.

   .. note:: If your implementation also uses the `Variant Annotation Specification <https://va-spec.ga4gh.org/en/stable/#>`_, consider associating the Categorical Variant with a Genomic Knowledge Statement based on a `Variant Oncogenicity Proposition <https://va-spec.ga4gh.org/en/stable/va-standard-profiles/base-profiles/proposition-profiles.html#variant-oncogenicity-proposition>`_.

2. When broadly defining a Categorical Variant that can be satisfied by many possible variants, as long as they are described using this Constraint and the same associated classification. For example, *KRAS* oncogenic variants, as :ref:`shown in the Examples <OncogenicityVariantEx1>`.

This Constraint may be used alongside a :ref:`Pathogenicity Constraint <PathogenicityConstraint>` when a variant has both an oncogenicity and a pathogenicity classification, as in :ref:`NM_004985.5(KRAS):c.34G>T (p.Gly12Cys) <OncogenicityPathogenicityVariantEx1>`.

classification
##############

.. include:: ../../_includes/_guidance_classification_oncogenicity.rst

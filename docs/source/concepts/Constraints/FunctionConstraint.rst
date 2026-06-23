.. _FunctionConstraint:

Function Constraint
!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/FunctionConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BRCA2 loss of function variants <FunctionVariantEx2>`
- :ref:`NRAS functionally normal variants <FunctionVariantEx1>`
- :ref:`PIK3CA p.R38H <FunctionVariantEx3>`

A representative example of this Constraint, from :ref:`NRAS functionally normal variants <FunctionVariantEx1>`:

.. literalinclude:: ../../../../examples/json/functionVariant-ex1.json
  :language: json
  :lines: 24-40

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used in two circumstances:

1. To define a :ref:`Canonical Allele <CanonicalAllele>`, :ref:`Categorical Copy Number Variant <CategoricalCnv>`, :ref:`Gene Fusion <GeneFusion>`, or :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>` Categorical Variant with a known functional impact.

   .. note:: If your implementation also uses the `Variant Annotation Specification <https://va-spec.ga4gh.org/en/stable/#>`_, consider associating the Categorical Variant with a Genomic Knowledge Statement based on an `Experimental Variant Functional Impact <https://va-spec.ga4gh.org/en/stable/va-standard-profiles/base-profiles/proposition-profiles.html#experimental-variant-functional-impact-proposition>`_.

2. When broadly defining a Categorical Variant that can be satisfied by many possible variants, as long as they are described using this Constraint and the same associated definition. For example, *BRCA2* loss of function variants, as :ref:`shown in the Examples <FunctionVariantEx2>`.

functionConsequence
###################

.. include:: ../../_includes/_guidance_function_consequence.rst

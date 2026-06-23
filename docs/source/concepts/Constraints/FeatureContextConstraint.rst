.. _FeatureContextConstraint:

Feature Context Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/FeatureContextConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BRCA2 loss of function variants <FunctionVariantEx2>`
- :ref:`NRAS functionally normal variants <FunctionVariantEx1>`
- :ref:`PIK3CA p.R38H <FunctionVariantEx3>`
- :ref:`TP53 Loss <Tp53CopyLoss>`

A representative example of this Constraint, from :ref:`TP53 Loss <Tp53CopyLoss>`:

.. literalinclude:: ../../../../examples/json/tp53-copy-loss.json
  :language: json
  :lines: 71-92

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

The *featureContext* attribute is required and is a :ref:`MappableConcept`, meaning that it should be represented using a term from an externally defined ontology. Specifically, we recommend using :ref:`Codings <Coding>` based on the `HUGO Gene Nomenclature Committee <https://www.genenames.org>`_, as we have done within our Examples of this Constraint.

.. note:: Implementers use this constraint to represent genes, but it can also be used to represent protein markers, variant consequences, and other genomic features. If you are using this constraint for uses other than to represent genes, please `let us know <https://github.com/ga4gh/cat-vrs/discussions/new?category=show-and-tell>`_!

Genes
#####

.. include:: ../../_includes/_guidance_feature_context_genes.rst

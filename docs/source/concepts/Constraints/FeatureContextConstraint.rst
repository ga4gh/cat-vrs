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

The `featureContext` attribute is required and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from an externally defined ontology.

.. note:: Implementers use this constraint to represent genes, but it can also be used to represent protein markers, variant consequences, and other genomic features. If you are using this constraint for uses other than to represent genes, please `let us know <https://github.com/ga4gh/cat-vrs/discussions/new?category=show-and-tell>`_!

Genes
#####

We recommend specifying *conceptType* as "Gene" and using a symbol from the `HUGO Gene Nomenclature Committee (HGNC) <https://www.genenames.org>`_ as a :ref:`primaryCoding <Coding>`.

The `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ is Python package and public REST instance that can be used to obtain :ref:`Codings <Coding>` and :ref:`Concept Mappings <ConceptMapping>` of gene concepts based on `Ensembl, NCBI Gene, HGNC, and other data sources <https://gene-normalizer.readthedocs.io/latest/normalizing_data/sources.html>`_.

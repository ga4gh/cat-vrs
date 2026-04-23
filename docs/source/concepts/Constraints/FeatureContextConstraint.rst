.. _FeatureContextConstraint:

Feature Context Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/FeatureContextConstraint.rst

Examples
@@@@@@@@

The following are example implementations of FeatureContextConstraint:

.. collapse:: Gene: TP53

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_tp53-copy-loss
      :language: json
      :lines: 74-98

.. collapse:: Gene: NRAS

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex1
      :language: json
      :lines: 10-26

.. collapse:: Gene: BRCA2

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex2
      :language: json
      :lines: 10-26

.. collapse:: Gene: PIK3CA

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex3
      :language: json
      :lines: 68-83

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

The `featureContext` attribute is required and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from an externally defined ontology. Implementers use this constraint to represent genes, but it can also be used to represent protein markers, variant consequences, and other genomic features.

Genes
#####

We recommend specifying *conceptType* as "Gene" and using a symbol from the `HUGO Gene Nomenclature Committee (HGNC) <https://www.genenames.org>`_ as a :ref:`primaryCoding <Coding>`.

The `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ is Python package and public REST instance that can be used to obtain :ref:`Codings <Coding>` and :ref:`Concept Mappings <ConceptMapping>` of gene concepts based on `Ensembl, NCBI Gene, HGNC, and other data sources <https://gene-normalizer.readthedocs.io/latest/normalizing_data/sources.html>`_.

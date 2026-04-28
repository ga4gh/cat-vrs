.. _FunctionConstraint:

Function Constraint
!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/FunctionConstraint.rst

Examples
@@@@@@@@
The following are example implementations of FunctionConstraint:

.. collapse:: NRAS functionally normal variants

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex1
      :language: json
      :lines: 27-43

.. collapse:: BRCA2 loss of function variants

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex2
      :language: json
      :lines: 27-43

.. collapse:: PIK3CA p.R38H

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_functionVariant-ex3
      :language: json
      :lines: 84-100

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used in two circumstances:

1. To annotate a :ref:`Canonical Allele <CanonicalAllele>`, :ref:`Categorical Copy Number Variant <CategoricalCnv>`, :ref:`Gene Fusion <GeneFusion>`, or :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>` Categorical Variant with a known functional impact.

.. note:: If your implementation also uses the `Variant Annotation Specification <https://va-spec.ga4gh.org/en/stable/#>`_, consider associating the Categorical Variant with a Genomic Knowledge Statement based on an `Experimental Variant Functional Impact <https://va-spec.ga4gh.org/en/stable/va-standard-profiles/base-profiles/proposition-profiles.html#experimental-variant-functional-impact-proposition>`_.

2. When broadly defining a Categorical Variant that can be satisfied by many possible variants, as long as they are described using this Constraint and the same associated definition. For example, *BRCA2* loss of function variants, as shown in the Examples.

functionConsequence
###################

The *functionConsequence* attribute is required and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from an externally defined ontology. We recommend using one of the following
defined terms from the `Sequence Ontology <http://www.sequenceontology.org>`_, with definitions
reproduced from SO:

.. list-table::
   :header-rows: 1
   :widths: 20 15 45 20

   * - Name
     - SO ID
     - SO Definition
     - SO Name
   * - **dominant negative variant**
     - `SO:0002052 <http://www.sequenceontology.org/browser/current_release/term/SO:0002052>`_
     - A variant where the mutated gene product adversely affects the other (wild type) gene product.
     - dominant_negative_variant
   * - **functionally normal**
     - `SO:0002219 <http://www.sequenceontology.org/browser/current_release/term/SO:0002219>`_
     - A sequence variant in which the function of a gene product is retained with respect to a reference.
     - functionally_normal
   * - **gain of function**
     - `SO:0002053 <http://www.sequenceontology.org/browser/current_release/term/SO:0002053>`_
     - A sequence variant whereby new or enhanced function is conferred on the gene product.
     - gain_of_function_variant
   * - **loss of function**
     - `SO:0002054 <http://www.sequenceontology.org/browser/current_release/term/SO:0002054>`_
     - A sequence variant whereby the gene product has diminished or abolished function.
     - loss_of_function_variant
   * - **loss of heterozygosity**
     - `SO:0001786 <http://www.sequenceontology.org/browser/current_release/term/SO:0001786>`_
     - A functional variant whereby the sequence alteration causes a loss of function of one allele of a gene.
     - loss_of_heterozygosity
   * - **polypeptide partial loss of function**
     - `SO:0001561 <http://www.sequenceontology.org/browser/current_release/term/SO:0001561>`_
     - A sequence variant that causes some but not all loss of polypeptide function with respect to a reference sequence.
     - polypeptide_partial_loss_of_function

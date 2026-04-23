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

   .. literalinclude:: ../../../../examples/json/functionVariant-ex1.json
      :language: json
      :lines: 24-40

.. collapse:: BRCA2 loss of function variants

   .. literalinclude:: ../../../../examples/json/functionVariant-ex2.json
      :language: json
      :lines: 24-40

.. collapse:: PIK3CA p.R38H

   .. literalinclude:: ../../../../examples/json/functionVariant-ex3.json
      :language: json
      :lines: 81-97

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@
The `functionConsequence` attribute is a :ref:`MappableConcept`, meaning that it should be represented using an externally defined ontology term. We recommend using one of the following defined terms from `The Sequence Ontology <http://www.sequenceontology.org>`_:

* **dominant negative variant** (`SO:0002052 <http://www.sequenceontology.org/browser/current_release/term/SO:0002052>`_ - dominant_negative_variant): A variant where the mutated gene product adversely affects the other (wild type) gene product.
* **functionally normal** (`SO:0002219 <http://www.sequenceontology.org/browser/current_release/term/SO:0002219>`_ - functionally_normal): A sequence variant in which the function of a gene product is retained with respect to a reference.
* **gain of function** (`SO:0002053 <http://www.sequenceontology.org/browser/current_release/term/SO:0002053>`_ - gain_of_function_variant): A sequence variant whereby new or enhanced function is conferred on the gene product.
* **loss of function** (`SO:0002054 <http://www.sequenceontology.org/browser/current_release/term/SO:0002054>`_ - loss_of_function_variant): A sequence variant whereby the gene product has diminished or abolished function.
* **loss of heterozygosity** (`SO:0001786 <http://www.sequenceontology.org/browser/current_release/term/SO:0001786>`_ - loss_of_heterozygosity): A functional variant whereby the sequence alteration causes a loss of function of one allele of a gene.
* **polypeptide partial loss of function** (`SO:0001561 <http://www.sequenceontology.org/browser/current_release/term/SO:0001561>`_ - polypeptide_partial_loss_of_function): A sequence variant that causes some but not all loss of polypeptide function with respect to a reference sequence.

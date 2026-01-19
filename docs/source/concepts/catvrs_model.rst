.. _catvrs_model:

Cat-VRS Model
@@@@@@@@@@@@@

The following data types classes are used by Cat-VRS but maintained by either the VRS subgroup
or across the GKS Work Stream as core data classes.

.. _CategoricalVariant:

Categorical Variant
###################

The Categorical Variant class is the primary class in Cat-VRS. It
depends on one or more Constraint elements to create a complete
description of a categorical variant.

.. include:: ../def/cat-vrs/CategoricalVariant.rst

.. _constraint:

Constraint
##########

The *Constraint* class is an abstract class that is the parent of all other constraint classes.  A constraint is a rule or set of rules that a variant must satisfy to qualify as a valid member of the CategoricalVariant. Constraint subclasses are only used in CategoricalVariant objects.

.. _DefiningAlleleConstraint:

DefiningAlleleConstraint
########################

.. include:: ../def/cat-vrs/DefiningAlleleConstraint.rst

**Examples**

The following are example implementations of DefiningAlleleConstraint:

.. collapse:: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_canonicalAllele-ex1
      :language: json
      :lines: 83-172

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: NC_000001.11:g.1699974C>G

   .. literalinclude:: ../../../schema/cat-vrs/json/example_canonicalAllele-ex2
      :language: json
      :lines: 37-112

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: EGFR L858R

   .. literalinclude:: ../../../schema/cat-vrs/json/example_proteinSequenceConsequence-ex1
      :language: json
      :lines: 99-150

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_proteinSequenceConsequence-ex2
      :language: json
      :lines: 69-132

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _DefiningLocationConstraint:

DefiningLocationConstraint
##########################

.. include:: ../def/cat-vrs/DefiningLocationConstraint.rst

**Examples**

The following are example implementations of DefiningLocationConstraint:

.. collapse:: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex1
      :language: json
      :lines: 47-102

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: GRCh38 Xp22.31(chrX:6978350-7594949)x3

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex3
      :language: json
      :lines: 25-79

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: BRAF V600

   .. literalinclude:: ../../../schema/cat-vrs/json/example_braf-v600
      :language: json
      :lines: 29-68

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _AdjacencyConstraint:

AdjacencyConstraint
###################

.. include:: ../def/cat-vrs/AdjacencyConstraint.rst

**Examples**

The following are example implementations of AdjacencyConstraint:

.. collapse:: BCR(ncbi:613)::ABL1(ncbi:25)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex1
      :language: json
      :lines: 42-75

.. collapse:: v::NTRK1(hgnc:8031)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex2
      :language: json
      :lines: 15-109

.. collapse:: ?::ZNF384(ncbi:171017)

   .. literalinclude:: ../../../schema/cat-vrs/json/example_adjacencyFusion-ex3
      :language: json
      :lines: 15-37

.. raw:: html

   <div style="margin-top: 1em;"></div>

**Implementation Guidance**

The Adjacency Constraint is similar to `VRS' Adjacency class <https://vrs.ga4gh.org/en/stable/concepts/MolecularVariation/Adjacency.html>`_, except that the `adjoinedElements` field supports data types in addition to :ref:`iriReference` and :ref:`Location`.

We recommend following the `Variant Interpretation for Cancer Consortium's Gene Fusion Specification <https://fusions.cancervariants.org/en/latest/>`_ when modeling a :ref:`GeneFusion` using this constraint. Specifically by:

* Representing `Named Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#named-gene-component>`_ as a :ref:`MappableConcept` with the `conceptType` field set to "Gene"; the `Gene Normalizer <https://gene-normalizer.readthedocs.io>`_ can help.
* Representing `Multiple Possible Gene Components <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ as a :ref:`ConceptSet` with the `membershipOperator` field set to "OR".
* Representing an `Unknown Gene Component` as a :ref:`UnknownGeneElement`.

.. _CopyCountConstraint:

CopyCountConstraint
###################

.. include:: ../def/cat-vrs/CopyCountConstraint.rst

**Examples**

The following are example implementations of CopyCountConstraint:

.. collapse:: 3 copies

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex3
      :language: json
      :lines: 21-24

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _CopyChangeConstraint:

CopyChangeConstraint
####################

.. include:: ../def/cat-vrs/CopyChangeConstraint.rst

**Examples**

The following are example implementations of CopyChangeConstraint:

.. collapse:: Gain

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex2
      :language: json
      :lines: 43-46

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: Loss

   .. literalinclude:: ../../../schema/cat-vrs/json/example_tp53-copy-loss
      :language: json
      :lines: 99-102

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _FeatureContextConstraint:

FeatureContextConstraint
########################

.. include:: ../def/cat-vrs/FeatureContextConstraint.rst

**Examples**

The following are example implementations of FeatureContextConstraint:

.. collapse:: Gene: TP53

   .. literalinclude:: ../../../schema/cat-vrs/json/example_tp53-copy-loss
      :language: json
      :lines: 74-98

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: Gene: NRAS

   .. literalinclude:: ../../../schema/cat-vrs/json/example_functionVariant-ex1
      :language: json
      :lines: 10-26

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: Gene: BRCA2

   .. literalinclude:: ../../../schema/cat-vrs/json/example_functionVariant-ex2
      :language: json
      :lines: 10-26

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: Gene: PIK3CA

   .. literalinclude:: ../../../schema/cat-vrs/json/example_functionVariant-ex3
      :language: json
      :lines: 68-83

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _FunctionConstraint:

FunctionConstraint
########################

.. include:: ../def/cat-vrs/FunctionConstraint.rst

**Examples**

The following are example implementations of FunctionConstraint:

.. collapse:: NRAS functionally normal variants

   .. literalinclude:: ../../../schema/cat-vrs/json/example_functionVariant-ex1
      :language: json
      :lines: 27-43

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: BRCA2 loss of function variants

   .. literalinclude:: ../../../schema/cat-vrs/json/example_functionVariant-ex2
      :language: json
      :lines: 27-43

.. raw:: html

   <div style="margin-top: 0.5em;"></div>

.. collapse:: PIK3CA p.R38H

   .. literalinclude:: ../../../schema/cat-vrs/json/example_functionVariant-ex3
      :language: json
      :lines: 84-100

.. raw:: html

   <div style="margin-top: 1em;"></div>

**Implementation Guidance**

The `functionConsequence` attribute is a :ref:`MappableConcept`, meaning that it should be represented using an externally defined ontology term. We recommend using one of the following defined terms from `The Sequence Ontology <http://www.sequenceontology.org>`_:

* **dominant negative variant** (`SO:0002052 <http://www.sequenceontology.org/browser/current_release/term/SO:0002052>`_ - dominant_negative_variant): A variant where the mutated gene product adversely affects the other (wild type) gene product.
* **functionally normal** (`SO:0002219 <http://www.sequenceontology.org/browser/current_release/term/SO:0002219>`_ - functionally_normal): A sequence variant in which the function of a gene product is retained with respect to a reference.
* **gain of function** (`SO:0002053 <http://www.sequenceontology.org/browser/current_release/term/SO:0002053>`_ - gain_of_function_variant): A sequence variant whereby new or enhanced function is conferred on the gene product.
* **loss of function** (`SO:0002054 <http://www.sequenceontology.org/browser/current_release/term/SO:0002054>`_ - loss_of_function_variant): A sequence variant whereby the gene product has diminished or abolished function.
* **loss of heterozygosity** (`SO:0001786 <http://www.sequenceontology.org/browser/current_release/term/SO:0001786>`_ - loss_of_heterozygosity): A functional variant whereby the sequence alteration causes a loss of function of one allele of a gene.
* **polypeptide partial loss of function** (`SO:0001561 <http://www.sequenceontology.org/browser/current_release/term/SO:0001561>`_ - polypeptide_partial_loss_of_function): A sequence variant that causes some but not all loss of polypeptide function with respect to a reference sequence.

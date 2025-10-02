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

The *Constraint* class is an abstract class that is the parent of all other constraint classes.  A constraint is a rule or set of rules that must be satisfied for a variant to be considered valid member of the CategoricalVariant. Constraint sub classes are only used in CategoricalVariant objects.

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
      :lines: 29-67

.. raw:: html

   <div style="margin-top: 1em;"></div>

.. _CopyCountConstraint:

CopyCountConstraint
###################

.. include:: ../def/cat-vrs/CopyCountConstraint.rst

**Examples**

The following are example implementations of CopyCountConstraint:

.. collapse:: 3 copies

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex3
      :language: json
      :lines: 21-23

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

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex4
      :language: json
      :lines: 44-47

.. raw:: html

   <div style="margin-top: 1em;"></div>

FeatureContextConstraint
########################

.. include:: ../def/cat-vrs/FeatureContextConstraint.rst

**Examples**

The following are example implementations of FeatureContextConstraint:

.. collapse:: Gene: TP53

   .. literalinclude:: ../../../schema/cat-vrs/json/example_categoricalCnv-ex4
      :language: json
      :lines: 19-43

.. raw:: html

   <div style="margin-top: 1em;"></div>

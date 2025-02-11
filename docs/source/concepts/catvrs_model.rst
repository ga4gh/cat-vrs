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

The *Constraint* class is an abstract class that is the parent of all
other constraint classes.  A constraint is a rule or set of rules that
must be satisfied for a CategoricalVariant to be considered valid.
Constraint sub classes are only used in CategoricalVariant objects.

.. _DefiningAlleleConstraint:

DefiningAlleleConstraint
########################

.. include:: ../def/cat-vrs/DefiningAlleleConstraint.rst

.. _DefiningLocationConstraint:

DefiningLocationConstraint
##########################

.. include:: ../def/cat-vrs/DefiningLocationConstraint.rst

.. _CopyCountConstraint:

CopyCountConstraint
###################

.. include:: ../def/cat-vrs/CopyCountConstraint.rst

.. _CopyChangeConstraint:

CopyChangeConstraint
####################

.. include:: ../def/cat-vrs/CopyChangeConstraint.rst

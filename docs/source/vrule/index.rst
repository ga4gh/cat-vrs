Variation Rule Specification
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To facilitate search of observed biomolecular variation, contemporary biomolecular
knowledgebases routinely "flatten" variation concepts to a specific context that
facilitates computable matching to observed variation, and typically provide related
contexts to help characterize the intended biological concept. For example, the
variant "BRAF V600E" at the `CIViC`_ resource describes a protein
change, but is flattened to a *representative genomic change* (GRCh37 chr7:g.140453136A>T)
and contextualized with corresponding transcript (NM_004333.4:c.1799T>A) and protein
(NP_004324.2:p.Val600Glu) descriptions. The representative change is linked to its
ClinGen Allele Registry identifier (CAID; `CA123643`_) to facilitate CAID matching
from other resources.

However, CA123643 is likewise a collection of variation contexts, including many
contexts that would typically not be considered equivalent to BRAF V600E:
ENST00000497784.1:n.1834T>A, ENST00000647434.1:n.738-3918T>A, and ENST00000642228.1:c.*877T>A,
for example, are all associated contexts with CA123643 but none result in an altered
protein product. Similarly, `CA16602531`_ can *also* serve as a linked representative
genomic change (through NC_000007.14:g.140753335_140753336delinsTT), but again this
concept contains several contexts describing the role of the variant that are not
applicable to the V600E mutation.

In addition, more complex cases of variation also exist, where the closest approximation of
a variation amounts to a simple genomic range. Examples of these types of variations include:
`BRAF V600 mutations`_, `TP53 truncating mutations`_, `EGFR exon 19 deletions`_. The concepts
associated with these variations (any protein mutation at a codon, any truncating mutation in
a gene, and any in-frame deletion in an exon) are not clearly definable using a variation
description framework such as VRS or HGVS.

To address these shortfalls, we introduce Variation Rules (VRules). VRules capture the semantics
that are missing or implied in genomic knowledge resources, providing a framework for expressing
how genomic knowledge may match to assayed variation. Much like the VRS objects used in this
specification, Variation Rule classes are designed to represent value objects that are readily
usable by genomic knowledge search engines. Also see the :ref:`VariationRuleDescriptor` class for
describing Variation Rules under a consistent paradigm with the :ref:`VariationDescriptor` class.

.. _VariationRule:

Variation Rule
@@@@@@@@@@@@@@

.. include:: ../defs/vrule/VariationRule.rst

.. _SimpleVariationRule:

Simple Variation Rule
#####################

.. include:: ../defs/vrule/SimpleVariationRule.rst

.. _EquivalentVariationRule:

Equivalent Variation Rule
$$$$$$$$$$$$$$$$$$$$$$$$$

.. include:: ../defs/vrule/EquivalentVariationRule.rst

.. _LocatedMolecularConsequenceRule:

Located Molecular Consequence Rule
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

.. include:: ../defs/vrule/LocatedMolecularConsequenceRule.rst

.. _GeneFunctionalConsequenceRule:

Gene Functional Consequence Rule
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

.. include:: ../defs/vrule/GeneConsequenceRule.rst

.. _ComplexVariationRule:

Complex Variation Rule
######################

.. include:: ../defs/vrule/ComplexVariationRule.rst

.. _CA123643: https://reg.genome.network/redmine/projects/registry/genboree_registry/by_caid?caid=CA123643
.. _CA16602531: http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA16602531
.. _BRAF V600 mutations: https://civicdb.org/events/genes/5/summary/variants/17/summary
.. _EGFR exon 19 deletions: https://civicdb.org/events/genes/19/summary/variants/133/summary
.. _TP53 truncating mutations: https://civicdb.org/events/genes/45/summary/variants/223/summary
:orphan:

.. _DiplotypeEx1:

:doc:`← Back to Examples </examples/index>`

CYP2C19\*1/\*17
!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 633878: CYP2C19*1/*17 <https://www.ncbi.nlm.nih.gov/clinvar/variation/633878/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Diplotype <Diplotype>`

Each of its two elements satisfies the :ref:`Star Allele <StarAllele>` Recipe.

.. rubric:: :ref:`Constraints <Constraint>`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`

.. rubric:: Properties

``id``: clinvar:633878
  The Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: CYP2C19\*1/\*17
  The human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: The CYP2C19\*1/\*17 diplotype, with the CYP2C19\*1 and CYP2C19\*17 star alleles occurring on different haplotypes (in trans).
  This field was populated with a description of this example because ClinVar does not provide a longform description.

``aliases``: null
  No aliases included.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: ClinVar
  A mapping to ClinVar's page for the diplotype is included.

``phaseRelation``: trans
  The two star alleles occur on different haplotypes.

.. rubric:: Elements

The following elements are joined with an **AND** ``operator`` and a **trans** ``phaseRelation``. Each is a :ref:`Star Allele <StarAllele>`, a nested :ref:`CompositeCategoricalVariant` whose single element is joined with an **AND** ``operator`` and a **cis** ``phaseRelation``:

- *CYP2C19*\*1, represented by the reference base at the \*17 defining position:

  - NC_000010.11:g.94761900=

- *CYP2C19*\*17:

  - `NM_000769.1(CYP2C19):c.-806C>T <https://www.ncbi.nlm.nih.gov/clinvar/variation/39357/>`_

Both variants are **present** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`.

ClinVar defines `CYP2C19*1 <https://www.ncbi.nlm.nih.gov/clinvar/variation/633855/>`_ as the reference sequence across the gene, NC_000010.11:g.94762681_94853205=. Because \*1 is defined by the absence of the variants that define other star alleles, this example instead represents it by the reference state at the position that distinguishes it from the other star allele in the diplotype. The VRS ``Allele`` for this position uses a :ref:`ReferenceLengthExpression` state.

The \*17 core variant, c.-806C>T, lies upstream of the NM_000769.4 transcript, so both VRS ``Allele`` objects were generated on GRCh38 chromosome 10 (NC_000010.11) with the `Variation Normalizer <https://variation-normalizer.readthedocs.io>`_.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/diplotype-1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/diplotype-1.yaml
  :language: yaml

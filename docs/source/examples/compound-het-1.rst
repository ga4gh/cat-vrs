:orphan:

.. _CompoundHetEx1:

:doc:`← Back to Examples </examples/index>`

NM_000094.4(COL7A1):c.[425A>G];[4333G>A]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 4891237: NM_000094.4(COL7A1):c.[425A>G];[4333G>A] <https://www.ncbi.nlm.nih.gov/clinvar/variation/4891237/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Compound Heterozygote <CompoundHeterozygote>`

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`

.. rubric:: Properties

``id``: clinvar:4891237
  The Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: NM_000094.4(COL7A1):c.[425A>G];[4333G>A]
  The human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: Compound heterozygous COL7A1 variants, with NM_000094.4(COL7A1):c.425A>G and NM_000094.4(COL7A1):c.4333G>A occurring on different haplotypes (in trans).
  This field was populated with a description of this example because ClinVar does not provide a longform description.

``aliases``: null
  No aliases included.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: ClinVar
  A mapping to ClinVar's page for the compound heterozygote is included.

``phaseRelation``: trans
  The two elements occur on different haplotypes, as asserted by ClinVar's ``c.[A];[B]`` HGVS notation.

.. rubric:: Elements

The following elements are joined with an **AND** ``operator`` and a **trans** ``phaseRelation``:

- `NM_000094.4(COL7A1):c.425A>G (p.Lys142Arg) <https://www.ncbi.nlm.nih.gov/clinvar/variation/29636/>`_
- `NM_000094.4(COL7A1):c.4333G>A (p.Gly1445Arg) <https://www.ncbi.nlm.nih.gov/clinvar/variation/4891236/>`_

Each haplotype is defined by a single variant, so both elements are **present** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`. The VRS ``Allele`` for each was generated on NM_000094.4, the COL7A1 MANE Select transcript, with the `Variation Normalizer <https://variation-normalizer.readthedocs.io>`_.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/compound-het-1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/compound-het-1.yaml
  :language: yaml

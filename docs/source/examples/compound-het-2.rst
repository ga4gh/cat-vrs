:orphan:

.. _CompoundHetEx2:

:doc:`← Back to Examples </examples/index>`

NM_003661.3:c.[1024A>G;1152T>G];[1164_1169delTTATAA]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 1120175: NM_003661.3:c.[1024A>G;1152T>G];[1164_1169delTTATAA] <https://www.ncbi.nlm.nih.gov/clinvar/variation/1120175/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Compound Heterozygote <CompoundHeterozygote>`

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`

.. rubric:: Properties

``id``: clinvar:1120175
  The Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: NM_003661.3:c.[1024A>G;1152T>G];[1164_1169delTTATAA]
  The human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: Compound heterozygous APOL1 G1/G2 genotype. The G1 haplotype, NM_003661.3(APOL1):c.[1024A>G;1152T>G], occurs in trans with the G2 deletion, NM_003661.3(APOL1):c.1164_1169del.
  This field was populated with a description of this example because ClinVar does not provide a longform description.

``aliases``: APOL1 G1/G2
  The common name for this genotype.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: ClinVar
  A mapping to ClinVar's page for the compound heterozygote is included.

``phaseRelation``: trans
  The two elements occur on different haplotypes, as asserted by ClinVar's ``c.[A];[B]`` HGVS notation.

.. rubric:: Elements

The following elements are joined with an **AND** ``operator`` and a **trans** ``phaseRelation``:

- `APOL1 G1, NM_003661.3(APOL1):c.[1024A>G;1152T>G] <https://www.ncbi.nlm.nih.gov/clinvar/variation/6080/>`_, a nested :ref:`CompositeCategoricalVariant` whose elements are joined with an **AND** ``operator`` and a **cis** ``phaseRelation``:

  - `NM_003661.4(APOL1):c.1024A>G (p.Ser342Gly) <https://www.ncbi.nlm.nih.gov/clinvar/variation/277678/>`_
  - `NM_003661.4(APOL1):c.1152T>G (p.Ile384Met) <https://www.ncbi.nlm.nih.gov/clinvar/variation/127198/>`_

- `APOL1 G2, NM_003661.4(APOL1):c.1164_1169del (p.Asn388_Tyr389del) <https://www.ncbi.nlm.nih.gov/clinvar/variation/6081/>`_

All variants are **present** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`. The G1 haplotype is defined by two variants, so it is represented as a nested Composite Categorical Variant; the G2 haplotype is defined by a single variant, so it is represented directly as a Categorical Variant Criterion.

The VRS ``Allele`` for each variant was generated on NM_003661.3, the transcript used by the ClinVar compound heterozygote record, with the `Variation Normalizer <https://variation-normalizer.readthedocs.io>`_. The single-variant ClinVar records are named on NM_003661.4. Because the G2 deletion falls within a repeat, its ``Allele`` is fully justified across the repeat and uses a :ref:`ReferenceLengthExpression` state.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/compound-het-2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/compound-het-2.yaml
  :language: yaml

:orphan:

.. _ProteinSequenceConsequenceEx2:

:doc:`← Back to Examples </examples/index>`

NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 55628: NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter) <https://www.ncbi.nlm.nih.gov/clinvar/variation/55628/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`

.. rubric:: Properties

``id``: clinvar:55628
  ClinVar Variation ID, where 55628 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)
  Human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: A brief placeholder note.
  This field was populated with an example value because ClinVar does not contain a longform description of this variant.

``aliases``: A subset of HGVS representations
  A subset of HGVS representations from ClinVar's Variant Details, including the MANE Select nucleotide coding (NM_007294.4:c.5558dup) and protein expressions (NP_009225.1:p.Tyr1853Ter and NP_009225.1:p.Y1853*), the full HGVS name with single-letter amino acid abbreviation, and both GRCh38 and GRCh37 hgvs.g variants, as well as the Canonical SPDI representation provided by ClinVar.

``extensions``: cytogenetic location, clinvar variation type, and hgvs list
  The cytogenetic location (17q21.31) and ClinVar variation type (Duplication) are obtained from ClinVar's Variant Details. The hgvs list extension includes GRCh38 genomic, GRCh37 genomic, MANE Select coding, and protein HGVS representations.

``mappings``: ClinVar, ClinGen, and dbSNP
  Mappings to ClinVar's page for the variant, ClinGen, and dbSNP are included from the Links section of ClinVar's Variant Details.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`
  The ``allele`` field is populated with the VRS Allele corresponding to the MANE Select protein representation NP_009225.1:p.Tyr1853Ter, as included within ``members``. The constraint includes a translation_of relation linking the protein allele to its coding DNA representation.

.. rubric:: Members

The ``members`` field includes three VRS Allele objects generated using the `VICC Variation Normalizer <https://github.com/cancervariants/variation-normalization>`_:

- NC_000017.11:g.43045712dup (GRCh38 genomic, on refseq:NC_000017.11)
- NC_000017.10:g.41197729dup (GRCh37 genomic, on refseq:NC_000017.10)
- NP_009225.1:p.Tyr1853Ter (protein, on the MANE Select protein product for BRCA1 refseq:NP_009225.1)

The variant normalization service was unable to generate a VRS Allele for the MANE Select coding representation NM_007294.4:c.5558dup.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/proteinSequenceConsequence-ex2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/proteinSequenceConsequence-ex2.yaml
  :language: yaml

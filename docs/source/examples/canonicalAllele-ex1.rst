:orphan:

.. _CanonicalAlleleEx1:

:doc:`← Back to Examples </examples/index>`

NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 662001: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs) <https://www.ncbi.nlm.nih.gov/clinvar/variation/662001/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Canonical Allele <CanonicalAllele>`

.. rubric:: Properties

``id``: clinvar:662001
  The Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)
  The human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: An example canonical allele.
  This field was populated with an example value because ClinVar does not provide a longform description.

``aliases``: 7 HGVS expressions.
  All listed HGVS representations within ClinVar's Variant Details for the variant, including genomic, coding, protein, LRG, and RefSeqGene representations.

``extensions``: cytogenetic location, clinvar variation type, and hgvs list
  The cytogenetic location (1p36.22) and ClinVar variation type (Deletion) are obtained from the Location and Type and length sections of ClinVar's Variant Details. The hgvs list extension includes HGVS representations from ClinVar's HGVS section, annotated with nucleotide type, MANE Select status, protein expression, and molecular consequence where applicable.

``mappings``: ClinVar, VarSome, and dbSNP
  Mappings to ClinVar's page for the variant, ClinGen, VarSome, and dbSNP are included from the Links section of ClinVar's Variant Details.

.. rubric:: :ref:`Constraints`

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`
  The ``allele`` field is populated with the VRS Allele corresponding to the MANE Select coding representation NM_004958.4:c.5992_5993del, as included within ``members``. The constraint includes relations specifying liftover and transcription relationships between the alleles.n.

.. rubric:: Members

The ``members`` field includes two VRS Allele objects generated using the VICC Variation Normalizer from the hgvs.g and hgvs.c MANE Select representations of this variant: NC_000001.11:g.11128044_11128045del (GRCh38 genomic) and NM_004958.4:c.5992_5993del (MANE Select coding, on the MTOR MANE Select transcript refseq:NM_004958.4).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/canonicalAllele-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/canonicalAllele-ex1.yaml
  :language: yaml

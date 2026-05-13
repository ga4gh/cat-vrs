:orphan:

.. _CanonicalAlleleEx2:

:doc:`← Back to Examples </examples/index>`

NC_000001.11:g.1699974C>G
!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinGen CA415424538 <https://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA415424538>`_

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Canonical Allele <CanonicalAllele>`

.. rubric:: Properties

``id``: clingen:CA415424538
  CA415424538 is the Canonical Allele Identifier listed by ClinGen.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: NC_000001.11:g.1699974C>G
  The GRCh38 HGVS Genomic Allele listed for the variant by ClinGen.

``description``: An example canonical allele.
  This field was populated with an example value because ClinGen does not provide a longform description.

``aliases``: 2 HGVS expressions.
  The HGVS representations of genomic alleles for GRCh38 (NC_000001.11:g.1699974C>G) and GRCh37 (NC_000001.10:g.1631413C>G), as provided by ClinGen.

``extensions``: cytogenetic location and hgvs list
  The cytogenetic location (1p36.33) was obtained from the HGNC pages for MMP23A (HGNC:7170) and MMP23B (HGNC:7171), the genes listed for this Canonical Allele. The hgvs list extension includes the hgvs.g representations for GRCh38 and GRCh37.

``mappings``: ClinGen, dbSNP, gnomAD (v2, v3, and v4)
  Mappings to ClinGen's webpage, dbSNP, and gnomAD v2, v3, and v4 are included from the Linked Data section of ClinGen's page for this Canonical Allele.

.. rubric:: :ref:`Constraints`

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`
  The ``allele`` field is populated with the VRS Allele corresponding to the GRCh38 genomic representation NC_000001.11:g.1699974C>G, as included within ``members``. The constraint includes relations specifying liftover and transcription relationships between the alleles.

.. rubric:: Members

The ``members`` field includes two VRS Allele objects generated using the `VICC Variation Normalizer <https://github.com/cancervariants/variation-normalization>`_ from the hgvs.g representations of this variant on GRCh38 (NC_000001.11:g.1699974C>G) and GRCh37 (NC_000001.10:g.1631413C>G), respectively.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/canonicalAllele-ex2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/canonicalAllele-ex2.yaml
  :language: yaml

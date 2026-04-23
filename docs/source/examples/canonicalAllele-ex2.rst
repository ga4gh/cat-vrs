:orphan:
.. _CanonicalAlleleEx2:

NC_000001.11:g.1699974C>G
!!!!!!!!!!!!!!!!!!!!!!!!!

**Source**: `ClinGen CA415424538 <https://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA415424538>`_

**Recipes that this example satisfies**: :ref:`Canonical Allele <CanonicalAllele>`

.. rubric:: Attributes

- ``id``: clingen:CA415424538, where CA415424538 is the Canonical Allele Identifier listed by ClinGen.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: NC_000001.11:g.1699974C>G, the GRCh38 HGVS Genomic Allele listed for the variant by ClinGen.
- ``description``: A brief placeholder note, as ClinGen does not contain a longform description of this variant.
- ``aliases``: The HGVS representations of genomic alleles for GRCh38 (NC_000001.11:g.1699974C>G) and GRCh37 (NC_000001.10:g.1631413C>G), as provided by ClinGen.
- ``extensions``: The cytogenetic location (1p36.33) was obtained from the HGNC pages for MMP23A (HGNC:7170) and MMP23B (HGNC:7171), the genes listed for this Canonical Allele. The hgvs list extension includes the hgvs.g representations for GRCh38 and GRCh37.
- ``mappings``: Mappings to ClinGen's webpage, dbSNP, and gnomAD v2, v3, and v4 are included from the Linked Data section of ClinGen's page for this Canonical Allele.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`: The ``allele`` field is populated with the VRS Allele corresponding to the GRCh38 genomic representation NC_000001.11:g.1699974C>G, as included within ``members``. The constraint includes relations specifying liftover and transcription relationships between the alleles.

.. rubric:: Members

The ``members`` field includes two VRS Allele objects generated using the VICC Variation Normalizer from the hgvs.g representations of this variant on GRCh38 (NC_000001.11:g.1699974C>G) and GRCh37 (NC_000001.10:g.1631413C>G), respectively.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/canonicalAllele-ex2.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/canonicalAllele-ex2.yaml
   :language: yaml

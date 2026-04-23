:orphan:
.. _ProteinSequenceConsequenceEx1:

EGFR L858R
!!!!!!!!!!

**Source**: `CIViC variant id 33: EGFR L858R <https://civicdb.org/variants/33/summary>`_

**Recipes that this example satisfies**: :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`

.. rubric:: Attributes

- ``id``: civic.mpid:33, where mpid stands for Molecular Profile ID, derived from the Molecular Profile ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: EGFR L858R, the human-readable label given to the genomic alteration by CIViC.
- ``description``: The longform description of EGFR L858R as provided by CIViC, noting that this mutation is one of the most prevalent single mutations in lung cancer and confers sensitivity to TKI therapies.
- ``aliases``: All aliases, HGVS descriptions, and the MANE Select transcript listed for EGFR L858R within the Summary section of CIViC's variant page, including LEU858ARG, rs121434568, genomic and coding HGVS representations, and the protein representation NP_005219.2:p.Leu858Arg.
- ``extensions``: The CIViC Representative Variant Coordinates and CIViC Variant Type (missense_variant, SO:0001583) are sourced from the Representative Variant Coordinates and Variant Type sections of CIViC's Variant Summary. The hgvs list extension contains the HGVS descriptions and MANE Select transcript representations from CIViC. A CIViC Molecular Profile Score extension is also included.
- ``mappings``: Mappings to CIViC's variant and molecular profile pages, ClinGen, ClinVar entries for multiple nucleotide change representations, and dbSNP are included.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`: The ``allele`` field is populated with the VRS Allele corresponding to the hgvs.p representation NP_005219.2:p.Leu858Arg, as included within ``members``. The constraint includes a translation_of relation to link the protein allele to the coding DNA representation.

.. rubric:: Members

The ``members`` field includes three VRS Allele objects generated using the VICC Variation Normalizer: NC_000007.13:g.55259515T>G (hgvs.g, GRCh37), NM_005228.5:c.2573T>G (hgvs.c, on the MANE Select transcript for EGFR refseq:NM_005228.5), and NP_005219.2:p.Leu858Arg (hgvs.p, on the protein product of the MANE Select transcript refseq:NP_005219.2).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/proteinSequenceConsequence-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/proteinSequenceConsequence-ex1.yaml
   :language: yaml

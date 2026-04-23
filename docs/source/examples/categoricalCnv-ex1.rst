:orphan:
.. _CategoricalCnvEx1:

GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Source**: `ClinVar variation 151061: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <https://www.ncbi.nlm.nih.gov/clinvar/variation/151061/>`_

**Recipes that this example satisfies**: :ref:`Categorical CNV <CategoricalCnv>`

.. rubric:: Attributes

- ``id``: clinvar:151061, where 151061 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3, the human-readable label listed within the Identifiers section of ClinVar's Variant Details.
- ``description``: A brief placeholder note, as ClinVar does not contain a longform description of this variant.
- ``aliases``: All listed HGVS representations within ClinVar's Variant Details for the variant: the GRCh38 (NC_000007.14) and GRCh37 (NC_000007.13) genomic representations.
- ``extensions``: The cytogenetic location (7p22.1) and ClinVar variation type (copy number gain) are obtained from ClinVar's Variant Details. The hgvs list extension includes the GRCh38 and GRCh37 HGVS genomic representations.
- ``mappings``: Mappings to ClinVar's page for the variant and dbVar are included from the Links section of ClinVar's Variant Details.

.. rubric:: Constraints

:ref:`Copy Count Constraint <CopyCountConstraint>`: The ``copies`` field is set to 3, reflecting the "x3" copy count specified in the variant name as provided by ClinVar.

:ref:`Defining Location Constraint <DefiningLocationConstraint>`: The defining location is a VRS Sequence Location on chromosome 7 (refseq:NC_000007.14, GRCh38) spanning positions 5,905,831 to 6,014,161, extracted from the GRCh38 CopyNumberCount included within ``members``. The ``matchCharacteristic`` is set to is_within, and a liftover relation is included to link the GRCh38 and GRCh37 representations.

.. rubric:: Members

The ``members`` field includes two VRS CopyNumberCount objects generated using the VICC Variation Normalizer from the HGVS representations of this variant: NC_000007.14:g.(?_5905831)_(6014161_?)dup (GRCh38) and NC_000007.13:g.(?_5945462)_(6053792_?)dup (GRCh37). Both members have a copies value of 3.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/categoricalCnv-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/categoricalCnv-ex1.yaml
   :language: yaml

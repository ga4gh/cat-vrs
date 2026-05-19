:orphan:

.. _CategoricalCnvEx1:

:doc:`← Back to Examples </examples/index>`

GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 151061: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <https://www.ncbi.nlm.nih.gov/clinvar/variation/151061/>`_

**Recipes that this example satisfies**:

:ref:`Categorical CNV <CategoricalCnv>`

.. rubric:: Properties

``id``: clinvar:151061
  ClinVar Variation ID, 151061 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3
  Human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: An optional field to describe this Categorical Variant.
  This field was populated with an example value because ClinVar does not provide a longform description.

``aliases``: 2 HGVS expressions
  All listed HGVS representations within ClinVar's Variant Details for the variant, including the GRCh38 (NC_000007.14) and GRCh37 (NC_000007.13) genomic representations.

``extensions``: cytogenetic location, clinvar variation type, and hgvs list
  The cytogenetic location (7p22.1) and ClinVar variation type (copy number gain) are obtained from ClinVar's Variant Details. The hgvs list extension includes the GRCh38 and GRCh37 HGVS genomic representations.

``mappings``: ClinVar and dbVar
  Mappings to ClinVar's page for the variant and dbVar are included from the Links section of ClinVar's Variant Details.

.. rubric:: Constraints

:ref:`Copy Count Constraint <CopyCountConstraint>`
  The ``copies`` field is set to 3, reflecting the "x3" copy count specified in the variant name as provided by ClinVar.

:ref:`Defining Location Constraint <DefiningLocationConstraint>`
  The defining location is a VRS Sequence Location on chromosome 7 (refseq:NC_000007.14, GRCh38) spanning positions 5,905,831 to 6,014,161, extracted from the GRCh38 CopyNumberCount included within ``members``. The ``matchCharacteristic`` is set to is_within, and a liftover relation is included to link the GRCh38 and GRCh37 representations.

.. rubric:: Members

The ``members`` field includes two VRS CopyNumberCount objects generated using the VICC Variation Normalizer from the HGVS representations of this variant:

- NC_000007.14:g.(?_5905831)_(6014161\_?)dup (GRCh38)
- NC_000007.13:g.(?_5945462)_(6053792\_?)dup (GRCh37)

Both members have a copies value of 3.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/categoricalCnv-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/categoricalCnv-ex1.yaml
   :language: yaml

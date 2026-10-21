:orphan:

.. _PathogenicityVariantEx2:

:doc:`← Back to Examples </examples/index>`

NM_007294.4(BRCA1):c.5503C>T (p.Arg1835Ter)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 55601: NM_007294.4(BRCA1):c.5503C>T (p.Arg1835Ter) <https://www.ncbi.nlm.nih.gov/clinvar/variation/55601/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

This example does not satisfy any :ref:`Recipes`.

.. rubric:: Properties

``id``: clinvar:55601
  ClinVar Variation ID, where 55601 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: NM_007294.4(BRCA1):c.5503C>T (p.Arg1835Ter)
  Human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: A brief placeholder note.
  This field was populated with an example value because ClinVar does not contain a longform description of this variant.

``aliases``: A subset of HGVS representations
  A subset of HGVS representations from ClinVar's Variant Details, including the MANE Select nucleotide coding (NM_007294.4:c.5503C>T) and protein expressions (NP_009225.1:p.Arg1835Ter and NP_009225.1:p.R1835*), both GRCh38 and GRCh37 hgvs.g variants, and the Canonical SPDI representation provided by ClinVar.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`
  The ``allele`` field is populated with the VRS Allele corresponding to the MANE Select coding representation NM_007294.4:c.5503C>T, generated with the VICC Variation Normalizer.

:ref:`Pathogenicity Constraint <PathogenicityConstraint>`
  The ``classification`` is a :ref:`Mappable Concept <MappableConcept>` for Pathogenic (ncit:C168799), with a primaryCoding linking to the NCI Thesaurus term Pathogenic Variant. This reflects ClinVar's germline classification of this variant.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/pathogenicityVariant-ex2.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/pathogenicityVariant-ex2.yaml
  :language: yaml

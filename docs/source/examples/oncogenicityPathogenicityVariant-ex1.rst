:orphan:

.. _OncogenicityPathogenicityVariantEx1:

:doc:`← Back to Examples </examples/index>`

NM_004985.5(KRAS):c.34G>T (p.Gly12Cys)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 12578: NM_004985.5(KRAS):c.34G>T (p.Gly12Cys) <https://www.ncbi.nlm.nih.gov/clinvar/variation/12578/>`_

.. rubric:: :ref:`Recipes` that this example satisfies

This example does not satisfy any :ref:`Recipes`.

.. rubric:: Properties

``id``: clinvar:12578
  ClinVar Variation ID, where 12578 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: NM_004985.5(KRAS):c.34G>T (p.Gly12Cys)
  Human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: A brief placeholder note.
  This field was populated with an example value because ClinVar does not contain a longform description of this variant.

``aliases``: A subset of HGVS representations
  A subset of HGVS representations from ClinVar's Variant Details, including the MANE Select nucleotide coding (NM_004985.5:c.34G>T) and protein expressions (NP_004976.2:p.Gly12Cys and NP_004976.2:p.G12C), a short gene-level name (KRAS G12C), both GRCh38 and GRCh37 hgvs.g variants, and the Canonical SPDI representation provided by ClinVar.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Constraints

:ref:`Defining Allele Constraint <DefiningAlleleConstraint>`
  The ``allele`` field is populated with the VRS Allele corresponding to the MANE Select coding representation NM_004985.5:c.34G>T, generated with the VICC Variation Normalizer.

:ref:`Pathogenicity Constraint <PathogenicityConstraint>`
  The ``classification`` is a :ref:`Mappable Concept <MappableConcept>` for Likely Pathogenic (ncit:C168800), with a primaryCoding linking to the NCI Thesaurus term Likely Pathogenic Variant. This reflects ClinVar's germline classification of this variant.

:ref:`Oncogenicity Constraint <OncogenicityConstraint>`
  The ``classification`` is a :ref:`Mappable Concept <MappableConcept>` for Oncogenic (ncit:C183322), with a primaryCoding linking to the NCI Thesaurus term Oncogenic. This reflects ClinVar's somatic oncogenicity classification of this variant.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/oncogenicityPathogenicityVariant-ex1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/oncogenicityPathogenicityVariant-ex1.yaml
  :language: yaml

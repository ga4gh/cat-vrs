:orphan:

.. _StarAlleleEx1:

:doc:`← Back to Examples </examples/index>`

CYP2C9*2
!!!!!!!!

.. rubric:: Source

`ClinVar variation 8409: CYP2C9*2 <https://www.ncbi.nlm.nih.gov/clinvar/variation/8409/>`_, the core variant of the *CYP2C9*\*2 star allele.

.. rubric:: :ref:`Recipes` that this example satisfies

:ref:`Star Allele <StarAllele>`

.. rubric:: :ref:`Constraints <Constraint>`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`

.. rubric:: Properties

``id``: catvrs.star.example:1
  This identifier was arbitrarily set for the purposes of this documentation.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: CYP2C9*2
  The star allele name.

``description``: The CYP2C9*2 star allele, a CYP2C9 haplotype defined by its core variant NM_000771.4(CYP2C9):c.430C>T (p.Arg144Cys).
  This field was populated with a description of this example.

``aliases``: null
  No aliases included.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: ClinVar
  A **closeMatch** mapping to ClinVar's `CYP2C9*2 haplotype <https://www.ncbi.nlm.nih.gov/clinvar/variation/177709/>`_, NM_000771.3(CYP2C9):c.[430C>T;1075A=]. It is not an exact match because ClinVar's definition also asserts the reference base at the *CYP2C9*\*3 position (c.1075).

``phaseRelation``: cis
  All elements occur on the same haplotype.

.. rubric:: Elements

The following element is joined with an **AND** ``operator`` and a **cis** ``phaseRelation``:

- `NM_000771.4(CYP2C9):c.430C>T (p.Arg144Cys) <https://www.ncbi.nlm.nih.gov/clinvar/variation/8409/>`_

The element is **present** within its :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`. Although *CYP2C9*\*2 is defined by a single core variant, it is represented as a :ref:`CompositeCategoricalVariant` so that it has the same structure as star alleles defined by several variants. The VRS ``Allele`` was generated on NM_000771.4, the CYP2C9 MANE Select transcript, with the `Variation Normalizer <https://variation-normalizer.readthedocs.io>`_.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/star-allele-1.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/star-allele-1.yaml
  :language: yaml

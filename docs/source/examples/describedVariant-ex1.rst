:orphan:
.. _DescribedVariantEx1:

t(2;15)(q23.1;q25.3)
!!!!!!!!!!!!!!!!!!!!

**Source**: `ClinVar variation 1177130: t(2;15)(q23.1;q25.3) <https://www.ncbi.nlm.nih.gov/clinvar/variation/1177130/>`_

**Recipes that this example satisfies**: None

.. rubric:: Attributes

- ``id``: clinvar:1177130, where 1177130 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: t(2;15)(q23.1;q25.3), the human-readable label listed within the Identifiers section of ClinVar's Variant Details.
- ``description``: A note that this described variant is an example of a categorical variant being modeled without constraints, which may be useful while awaiting specification support for the necessary constraint type.
- ``aliases``: ClinVar does not provide any alternative representations of this variant, so this field is left empty.
- ``extensions``: The cytogenetic location (2q23.1-23.2) and ClinVar variation type (Translocation) are obtained from the Location and Type and length sections of ClinVar's Variant Details.
- ``mappings``: ClinVar does not provide any mappings within the Links section of this variant's Variant Details, so this field is left empty.

.. rubric:: Constraints

This example does not apply any constraints. Implementers may choose to represent Categorical Variants in this way while waiting for the specification to support a means to model them.

.. rubric:: Members

This example does not include members, as VRS does not yet support translocations.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/describedVariant-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/describedVariant-ex1.yaml
   :language: yaml

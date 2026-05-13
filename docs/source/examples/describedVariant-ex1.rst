:orphan:

.. _DescribedVariantEx1:

:doc:`← Back to Examples </examples/index>`

t(2;15)(q23.1;q25.3)
!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

`ClinVar variation 1177130: t(2;15)(q23.1;q25.3) <https://www.ncbi.nlm.nih.gov/clinvar/variation/1177130/>`_

.. rubric:: :ref:`Recipes` that example satisfies

None

.. rubric:: Properties

``id``: clinvar:1177130
  ClinVar Variation ID, where 1177130 is the Variation ID listed within the Identifiers section of ClinVar's Variant Details.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: t(2;15)(q23.1;q25.3)
  Human-readable label listed within the Identifiers section of ClinVar's Variant Details.

``description``: This described variant is an example of a categorical variant being modeled without constraints. This may be useful to model types of categorical variants as necessary constraints are still being developed.
  This note was provided to state why this example does not have any Constraints.

``aliases``: null
  No aliases included.

``extensions``: cytogenetic location and ClinVar variant details
  The cytogenetic location (2q23.1-23.2) and ClinVar variation type (Translocation) are obtained from the Location and Type and length sections of ClinVar's Variant Details.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Constraints

This example does not apply any constraints. Implementers may choose to represent Categorical Variants in this way while waiting for the specification to support a means to model them.

.. rubric:: Members

This example does not include members.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/describedVariant-ex1.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/describedVariant-ex1.yaml
   :language: yaml

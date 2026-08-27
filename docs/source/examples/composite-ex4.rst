:orphan:

.. _CompositeEx4:

:doc:`← Back to Examples </examples/index>`

KRAS and NRAS wild type
!!!!!!!!!!!!!!!!!!!!!!!

.. rubric:: Source

The US Food and Drug Administration defines RAS wild type for eligibility criteria of `panitumumab <https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/125147s210lbl.pdf>`_ as "the absence of a RAS mutation in exon 2 (codons 12 and 13), exon 3 (codons 59 and 61), and exon 4 (codons 117 and 146) of both KRAS and NRAS".

.. rubric:: :ref:`Constraints`

This :ref:`CompositeCategoricalVariant` utilizes the following Constraints:

- :ref:`Defining Location Constraint <DefiningLocationConstraint>`

.. rubric:: Properties

``id``: catvrs.composite.example:4
  This identifier was arbitrarily set for the purposes of this documentation.

``type``: CompositeCategoricalVariant
  This value is required by the specification for all :ref:`Composite Categorical Variant <CompositeCategoricalVariant>` objects.

``name``: KRAS and NRAS wild type
  This field was populated with an example value.

``description``: The US Food and Drug Administration defines RAS wild type for eligibility criteria of Vectibix as "the absence of a RAS mutation in exon 2 (codons 12 and 13), exon 3 (codons 59 and 61), and exon 4 (codons 117 and 146) of both KRAS and NRAS". We model this Composite Categorical Variant as the Sequence Location for all of these specified codons being absent.
  This field was populated with a rationale for this example Composite Categorical Variant.

``aliases``: null
  No aliases included.

``extensions``: null
  No :ref:`extensions <Extension>` included.

``mappings``: null
  No :ref:`mappings <ConceptMapping>` included.

.. rubric:: Elements

The following elements are joined with an **AND** ``operator``

- *KRAS* exon 2 codon 12
- *KRAS* exon 2 codon 13
- *KRAS* exon 3 codon 59
- *KRAS* exon 3 codon 61
- *KRAS* exon 4 codon 117
- *KRAS* exon 4 codon 146
- *NRAS* exon 2 codon 12
- *NRAS* exon 2 codon 13
- *NRAS* exon 3 codon 59
- *NRAS* exon 3 codon 61
- *NRAS* exon 4 codon 117
- *NRAS* exon 4 codon 146

All elements are **absent** within their :ref:`Categorical Variant Criterion <CategoricalVariantCriterion>`.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/composite-ex4.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/composite-ex4.yaml
  :language: yaml

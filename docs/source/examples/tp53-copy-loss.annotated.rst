:orphan:
.. _Tp53CopyLossAnnotated:

TP53 Loss
!!!!!!!!!

**Source**: `CIViC variant id 4452: TP53 Loss <https://civicdb.org/variants/4452/summary>`_ (annotated)

**Recipes that this example satisfies**: None

This is the annotated version of :ref:`TP53 Loss <Tp53CopyLoss>`. It is structurally equivalent to that example and includes inline YAML comments throughout the source file explaining the role and rationale of each field. This version is intended for readers learning to work with the Cat-VRS specification.

.. rubric:: Attributes

- ``id``: civic.id:4452, derived from the Variant ID provided by CIViC.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: TP53 Loss, the name of the variant as provided by CIViC.
- ``description``: A plain text description of the variant noting that TP53 Copy Number Loss is a categorical copy-number variant resulting from the deletion of one copy of the TP53 gene.
- ``aliases``: TP53 Copy Number Loss and P53 Copy Number Loss are included to clearly specify that this is a copy number event.
- ``extensions``: The cytogenetic location (17p13) was obtained from HGNC for TP53.
- ``mappings``: Mappings to CIViC's page for TP53 Loss (exactMatch) and the related CIViC molecular profile for TP53 Deletion (relatedMatch) are included.

.. rubric:: Constraints

:ref:`Defining Location Constraint <DefiningLocationConstraint>`: The defining location is a VRS Sequence Location on chromosome 17 (refseq:NC_000017.11, GRCh38) spanning the genomic region of the TP53 gene (positions 7,668,420 to 7,687,490). The ``matchCharacteristic`` is set to is_within, and a liftover relation is included.

:ref:`Feature Context Constraint <FeatureContextConstraint>`: The ``featureContext`` is a MappableConcept for TP53, with a primaryCoding linking to HGNC:11998 and a cytogenetic location extension of 17p13.1.

:ref:`Copy Change Constraint <CopyChangeConstraint>`: The ``copyChange`` field is set to loss to specify the category of copy change.

.. rubric:: Members

This example does not include members, as VRS does not support large-scale copy-number events of this type.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/tp53-copy-loss.annotated.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/tp53-copy-loss.annotated.yaml
   :language: yaml

:orphan:
.. _BrafV600Annotated:

BRAF V600
!!!!!!!!!

**Source**: `CIViC variant id 17: BRAF V600 <https://civicdb.org/variants/17/summary>`_ (annotated)

**Recipes that this example satisfies**: None

This is the annotated version of :ref:`BRAF V600 <BrafV600>`. It is structurally equivalent to that example and includes inline YAML comments throughout the source file explaining the role and rationale of each field. This version is intended for readers learning to work with the Cat-VRS specification.

.. rubric:: Attributes

- ``id``: civic.vid:17, where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: BRAF V600, the human-readable name for this variant.
- ``description``: A summary of the categorical variant noting that BRAF V600 variants are missense amino acid substitutions that result in a change at valine 600, with V600E being the most common and V600K, V600M, V600R, and V600G also observed.
- ``aliases``: Representations with the MANE Select transcript for BRAF: NM_004333.6(BRAF) V600 and NM_004333.6 V600.
- ``extensions``: The CIViC Representative Variant Coordinates are included, specifying GRCh37 genomic coordinates on chromosome 7.
- ``mappings``: A set of ClinVar variants corresponding to amino acid substitutions at BRAF V600 are included as relatedMatch mappings: V600E (c.1799T>A), V600R (c.1798_1799delinsAG), V600K (c.1798_1799delinsAA), V600G (c.1799T>G), and V600M (c.1798G>A).

.. rubric:: Constraints

:ref:`Defining Location Constraint <DefiningLocationConstraint>`: The defining location is amino acid position 600 within the BRAF protein (refseq:NP_004324.2), the protein product of the MANE Select coding transcript for BRAF (refseq:NM_004333.6), corresponding to valine in the reference sequence. The ``matchCharacteristic`` is set to is_within, meaning any variant whose affected residue falls within this position satisfies the constraint.

.. rubric:: Members

The ``members`` field includes five VRS Allele objects generated using the VICC Variation Normalizer from the hgvs.c representations of BRAF V600E (NM_004333.6:c.1799T>A), V600K (NM_004333.6:c.1798_1799delinsAA), V600G (NM_004333.6:c.1799T>G), V600M (NM_004333.6:c.1798G>A), and V600R (NM_004333.6:c.1798_1799delinsAG).

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/braf-v600.annotated.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/braf-v600.annotated.yaml
   :language: yaml

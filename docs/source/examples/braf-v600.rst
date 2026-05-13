:orphan:

.. _BrafV600:

:doc:`← Back to Examples </examples/index>`

BRAF V600
!!!!!!!!!

.. rubric:: Source

`CIViC variant id 17: BRAF V600 <https://civicdb.org/variants/17/summary>`_

.. rubric:: :ref:`Recipes` that this example satisfies

None

.. rubric:: Properties

``id``: civic.vid:17
  CIViC Variant ID, where vid stands for Variant ID, derived from the Variant ID contained within the CIViC URL for this genomic alteration.

``type``: CategoricalVariant
  This value is required by the specification for all :ref:`Categorical Variant <CategoricalVariant>` objects.

``name``: BRAF V600
  Human-readable name for this variant.

``description``: BRAF V600 variants are missense amino acid substitutions that result in a change at valine 600, with V600E being the most common and V600K, V600M, V600R, and V600G also observed.
  This field was populated with an example value because CIViC does not provide a longform description.

``aliases``: NM_004333.6(BRAF) V600, NM_004333.6 V600
  Example aliases that include the MANE Select transcript for BRAF were included.

``extensions``: CIViC Representative Variant Coordinates
  GRCh37 genomic coordinates on chromosome 7.

``mappings``: V600E (c.1799T>A), V600R (c.1798_1799delinsAG), V600K (c.1798_1799delinsAA), V600G (c.1799T>G), V600M (c.1798G>A)
  ClinVar variants corresponding to amino acid substitutions at BRAF V600 were included as relatedMatch mappings.

.. rubric:: :ref:`Constraints`

:ref:`Defining Location Constraint <DefiningLocationConstraint>`
  The defining location is amino acid position 600 within the *BRAF* protein (refseq:NP_004324.2), the protein product of the MANE Select coding transcript for *BRAF* (refseq:NM_004333.6), corresponding to valine in the reference sequence.

  The ``matchCharacteristic`` is set to "is_within", meaning any variant whose affected residue falls within this position satisfies the constraint.

.. rubric:: Members

The ``members`` field includes five VRS Allele objects generated using the VICC Variation Normalizer from the hgvs.c representations of *BRAF*:

- V600E (NM_004333.6:c.1799T>A)
- V600K (NM_004333.6:c.1798_1799delinsAA)
- V600G (NM_004333.6:c.1799T>G)
- V600M (NM_004333.6:c.1798G>A)
- V600R (NM_004333.6:c.1798_1799delinsAG)

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/braf-v600.json
  :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/braf-v600.yaml
  :language: yaml

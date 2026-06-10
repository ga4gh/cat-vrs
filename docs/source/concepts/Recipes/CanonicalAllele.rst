.. _CanonicalAllele:

Canonical Allele
!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CanonicalAllele.rst

A CanonicalAllele is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`DefiningAlleleConstraint` with the `relations` array containing both
   `liftover_to` and `transcribed_to` codes. This constraint MUST refer to a genomic
   variant for the `allele`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs) <CanonicalAlleleEx1>`
- :ref:`NC_000001.11:g.1699974C>G <CanonicalAlleleEx2>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Constraints
###########

Categorical Variants that are intended to represent Canonical Alleles must **only** contain the :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`, with an ``Allele`` on a genomic :ref:`Sequence Reference` and the following **required** :ref:`codings <Coding>` specified as *relations*:

.. list-table::
    :header-rows: 1
    :widths: 25 25 50

    * - Code
      - System
      - Rationale
    * - liftover_to
      - gks-gks-term:allele-relation
      - To specify that VRS :ref:`Alleles` that are listed as *members* may be a liftover of the Defining ``Allele``.
    * - transcribed_to
      - `http://www.sequenceontology.org <https://www.ebi.ac.uk/ols4/ontologies/so>`_
      - To specify that VRS :ref:`Alleles` that are listed as *members* may be transcribed from the Defining Allele.

We recommend the following resources for constructing VRS Allele objects:

- The `Variant Normalizer <https://variation-normalizer.readthedocs.io>`_ is a Python package and
  public REST instance that translates plain-text HGVS expressions into `Normalized VRS Allele
  objects <https://vrs.ga4gh.org/en/latest/conventions/normalization.html#allele-normalization>`_. Genomic coordinates default to GRCh38 unless otherwise specified.
- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate a VRS digest for an Allele, Sequence Location, and Sequence Reference.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Allele objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Allele`` exists on. Consider the following values to the Defining ``Allele`` that is intended to be represented as a Canonical Allele:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Sequence reference type
     - moleculeType
     - residueAlphabet
   * - Genomic
     - genomic
     - na

Members
#######

When modeling a Canonical Allele, *members* may be populated with VRS ``Allele`` objects that are:

- The Defining Allele **itself**
- A **liftover of** the Defining Allele on another reference genome
- An RNA (pre-mRNA) or RNA ``Allele`` **transcribed from** the Defining Allele
- A protein ``Allele`` that is a **translation of** the Defining Allele.

As is the case with constructing VRS ``Allele`` objects for the Defining Allele, we recommend the `Variant Normalizer <https://variation-normalizer.readthedocs.io>`_, `vrs-python <https://github.com/ga4gh/vrs-python>`_, and `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ as resources for constructing VRS Allele objects. Likewise, we recommend populating both the *molecularType* and *residueAlphabet* attributes of the :ref:`Sequence Reference <SequenceReference>` for any ``Allele`` listed as a member.

.. include:: ../../_includes/_guidance_generate_sequence_location_box.rst

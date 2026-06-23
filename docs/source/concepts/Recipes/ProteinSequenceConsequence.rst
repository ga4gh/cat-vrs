.. _ProteinSequenceConsequence:

Protein Sequence Consequence
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/ProteinSequenceConsequence.rst

A ProteinSequenceConsequence is a :ref:`CategoricalVariant` with exactly one constraint:

1. A :ref:`Defining Allele Constraint <DefiningAlleleConstraint>` with the `.relations` array containing only a
   `translation_of` code. This constraint MUST refer to a protein variant for the `allele`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`EGFR L858R <ProteinSequenceConsequenceEx1>`
- :ref:`NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter) <ProteinSequenceConsequenceEx2>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Constraints
###########

Categorical Variants that are intended to represent Protein Sequence Consequences must **only** contain the :ref:`Defining Allele Constraint <DefiningAlleleConstraint>`, with an ``Allele`` on a protein :ref:`Sequence Reference <SequenceReference>` and the following **required** :ref:`codings <Coding>` specified as *relations*:

.. include:: ../../_includes/_guidance_ga4gh_gks_term_warning.rst

.. list-table::
    :header-rows: 1
    :widths: 25 25 50

    * - Code
      - System
      - Rationale
    * - translation_of
      - `http://www.sequenceontology.org <https://www.ebi.ac.uk/ols4/ontologies/so>`_
      - To specify that VRS :ref:`Alleles <Allele>` that are listed as *members* may be a translation of the Defining ``Allele``.

.. include:: ../../_includes/_guidance_construct_allele_objects.rst

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Allele`` exists on. Consider the following values for the Defining ``Allele`` that is intended to be represented as a Protein Sequence Consequence:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Sequence reference type
     - moleculeType
     - residueAlphabet
   * - Protein
     - protein
     - aa

Members
#######

When modeling a Protein Sequence Consequence, *members* may be populated with VRS ``Allele`` objects that are:

- The Defining Allele **itself**
- A **projection of** the Defining Allele on another protein isoform.
- A genomic ``Allele`` that is **transcribed to** the Defining Allele.
- An RNA (pre-mRNA) or mRNA ``Allele`` that **translates to** the Defining Allele.

As is the case with constructing VRS ``Allele`` objects for the Defining Allele, we recommend the `Variation Normalizer <https://variation-normalizer.readthedocs.io>`_, `vrs-python <https://github.com/ga4gh/vrs-python>`_, and `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ as resources for constructing VRS Allele objects. Likewise, we recommend populating both the *moleculeType* and *residueAlphabet* attributes of the :ref:`Sequence Reference <SequenceReference>` for any ``Allele`` listed as a member.

.. include:: ../../_includes/_guidance_generate_sequence_location_box.rst

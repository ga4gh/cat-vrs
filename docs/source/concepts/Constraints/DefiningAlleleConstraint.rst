.. _DefiningAlleleConstraint:

Defining Allele Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/DefiningAlleleConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs) <CanonicalAlleleEx1>`
- :ref:`NC_000001.11:g.1699974C>G <CanonicalAlleleEx2>`
- :ref:`EGFR L858R <ProteinSequenceConsequenceEx1>`
- :ref:`NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter) <ProteinSequenceConsequenceEx2>`
- :ref:`PIK3CA p.R38H <FunctionVariantEx3>`

A representative example of this Constraint, from :ref:`NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs) <CanonicalAlleleEx1>`:

.. literalinclude:: ../../../../examples/json/canonicalAllele-ex1.json
  :language: json
  :lines: 80-169

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used to describe a Categorical Variant using a VRS :ref:`Allele` object, such as defining a :ref:`Canonical Allele <CanonicalAllele>` or :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`.

allele
######

The *allele* attribute is required and must be a valid VRS :ref:`Allele` object. Constructing a VRS Allele requires a :ref:`SequenceLocation` and a sequence state. We recommend the following resources for constructing VRS Allele objects:

- The `Variant Normalizer <https://variation-normalizer.readthedocs.io>`_ is a Python package and
  public REST instance that translates plain-text HGVS expressions into `Normalized VRS Allele
  objects <https://vrs.ga4gh.org/en/latest/conventions/normalization.html#allele-normalization>`_. Genomic coordinates default to GRCh38 unless otherwise specified.
- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate a VRS digest for an Allele, Sequence Location, and Sequence Reference, and other VRS concepts.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Sequence Reference objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Allele`` exists on. Consider the following values, depending on the type of ``Allele`` expressed:

.. list-table::
   :header-rows: 1
   :widths: 20 30 25 25

   * - Allele type
     - Recipe
     - moleculeType
     - residueAlphabet
   * - Genomic DNA
     - :ref:`Canonical Allele <CanonicalAllele>`
     - genomic
     - na
   * - RNA
     -
     - RNA
     - na
   * - mRNA
     -
     - mRNA
     - na
   * - Protein
     - :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`
     - protein
     - aa

relations
#########

The *relations* attribute is optional and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from a defined ontology. Relation terms describe how *members* of a :ref:`Categorical Variant <CategoricalVariant>` relate to the Defining :ref:`Allele`.

.. note:: *relations* are **not** definitional and thus do not alter the scope of the Categorical Variant's definition. In other words, they do not restrict or expand which variants satisfy the Categorical Variant's constraints. However, they **are** definitional for some :ref:`Recipes <Recipes>`.

The following relation terms are some to consider using with this Constraint, depending on the ``Allele`` molecule type represented and which :ref:`Recipe(s) <Recipes>` you intend to satisfy:

.. warning:: Some relation-terms are based on the system ``ga4gh-gks-term``. This is an internally controlled ontology for use specifically with the Categorical Variant Representation Specification.

genomic
=======

If you are modeling a genomic ``Allele``, members may be **the Defining Allele itself**, a **liftover of** the Defining Allele on another reference genome, an RNA or mRNA ``Allele`` **transcribed from** the Defining Allele, or a protein ``Allele`` that is a **translation of** the Defining Allele.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - How the ``member`` relates to the Categorical Variant
   * - ga4gh-gks-term:allele-relation:self
     - Use when the ``member`` is the Defining ``Allele`` itself.
   * - ga4gh-gks-term:allele-relation:liftover_to
     - Use when the ``member`` is the "same" genomic DNA variant, as represented on another reference genome.
   * - `SO:transcribed_from <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523transcribed_from>`_
     - Use when the ``member`` is an RNA (pre-mRNA) or mRNA ``Allele`` that is transcribed from the Defining Allele.
   * - `SO:translation_of <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523translation_of>`_
     - Use when the ``member`` is a protein ``Allele`` that is a translation of the Defining Allele.

.. warning:: The specification currently incorrectly lists the directionality of the liftover term in the :ref:`Canonical Allele <CanonicalAllele>` Recipe.

RNA (pre-mRNA)
==============

If you are modeling an RNA (pre-mRNA) ``Allele``, members may be **the Defining Allele itself**, a **projection of** the Defining Allele on another RNA (pre-mRNA) transcript, a genomic ``Allele`` that is **transcribed to** the Defining Allele, a mRNA ``Allele`` that is **processed from** the Defining Allele, or a protein ``Allele`` that is a **translation of** the Defining Allele.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - How the ``member`` relates to the Categorical Variant
   * - ga4gh-gks-term:self
     - Use when the ``member`` is the Defining ``Allele`` itself.
   * - ga4gh-gks-term:projection_of
     - Use when the ``member`` is the "same" RNA (pre-mRNA) variant, as represented on another RNA (pre-mRNA) transcript.
   * - `SO:transcribed_to <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523transcribed_to>`_
     - Use when the ``member`` is a genomic ``Allele`` that is transcribed to the Defining Allele.
   * - `SO:processed_from <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523processed_from>`_
     - Use when the ``member`` is an mRNA ``Allele`` that is processed from the RNA (pre-mRNA) Allele.
   * - `SO:translation_of <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523translation_of>`_
     - Use when the ``member`` is a protein ``Allele`` that is a translation of the Defining Allele.

mRNA
====

If you are modeling an mRNA ``Allele``, members may be **the Defining Allele itself**, a **projection of** the Defining Allele on another mRNA transcript, a genomic ``Allele`` that is **transcribed to** the Defining Allele, an RNA (pre-mRNA) ``Allele`` that is **processed into** the Defining Allele, or a protein ``Allele`` that is a **translation of** the Defining Allele.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - How the ``member`` relates to the Categorical Variant
   * - ga4gh-gks-term:self
     - Use when the ``member`` is the Defining ``Allele`` itself.
   * - ga4gh-gks-term:projection_of
     - Use when the ``member`` is the "same" mRNA variant, as represented on another mRNA transcript.
   * - `SO:transcribed_to <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523transcribed_to>`_
     - Use when the ``member`` is a genomic ``Allele`` that is transcribed to the Defining Allele.
   * - `SO:processed_into <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523processed_into>`_
     - Use when the ``member`` is an RNA (pre-mRNA) ``Allele`` that is processed into the Defining Allele.
   * - `SO:translation_of <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523translation_of>`_
     - Use when the ``member`` is a protein ``Allele`` that is a translation of the Defining Allele.

protein
=======

If you are modeling a protein sequence ``Allele``, members may be **the Defining Allele itself**, a **projection of** the Defining ``Allele`` on another protein isoform, a genomic ``Allele`` that is **transcribed to** the Defining Allele, or an RNA or mRNA ``Allele`` that is **translates to** the Defining Allele.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - How the ``member`` relates to the Defining Allele
   * - ga4gh-gks-term:self
     - Use when the ``member`` is the Defining ``Allele`` itself.
   * - ga4gh-gks-term:projection_of
     - Use when the ``member`` is the "same" protein sequence variant, as represented on another protein isoform.
   * - `SO:transcribed_to <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523transcribed_to>`_
     - Use when the ``member`` is a genomic ``Allele`` that is transcribed to the Defining Allele.
   * - `SO:translates_to <https://www.ebi.ac.uk/ols4/ontologies/so/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252Fso%2523translates_to>`_
     - Use when the ``member`` is an RNA or mRNA ``Allele`` that translates to the Defining Allele.

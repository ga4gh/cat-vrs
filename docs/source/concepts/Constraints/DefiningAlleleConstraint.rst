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

This Constraint is used when wanting to describe a Categorical Variant using a VRS :ref:`Allele` object, such as defining a :ref:`Canonical Allele <CanonicalAllele>` or :ref:`Protein Sequence Consequence <ProteinSequenceConsequence>`.

allele
######

The *allele* attribute is required and must be a valid VRS :ref:`Allele` object. Constructing a VRS Allele requires a :ref:`SequenceLocation` and a sequence state. We recommend the following resources for constructing VRS Allele objects:

- The `Variant Normalizer <https://variation-normalizer.readthedocs.io>`_ is a Python package and
  public REST instance that translates plain-text HGVS expressions into `Normalized VRS Allele
  objects <https://vrs.ga4gh.org/en/latest/conventions/normalization.html#allele-normalization>`_. Genomic coordinates default to GRCh38 unless otherwise specified.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Allele objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Allele`` exists upon. Consider the following values, depending on the type of ``Allele`` expressed:

.. list-table::
   :header-rows: 1
   :widths: 20 30 25 25

   * - Allele type
     - Recipe
     - moleculeType
     - residueAlphabet
   * - Nucleotide
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
represented using a term from an externally defined ontology. Relation terms describe how *members* of a :ref:`Categorical Variant <CategoricalVariant>` relate to the defining :ref:`Allele`. They are **not** definitional and thus do not alter the definitional scope of the Categorical Variant; in other words, they do not restrict or expand which variants satisfy the Categorical Variant's constraints.

The following relation terms are some to consider using with this Constraint, depending on the ``Allele`` molecule type represented:

genomic
=======

RNA
===

mRNA
====

protein
=======

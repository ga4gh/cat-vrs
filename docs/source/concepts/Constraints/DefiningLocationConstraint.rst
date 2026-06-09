.. _DefiningLocationConstraint:

Defining Location Constraint
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/DefiningLocationConstraint.rst

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` utilize this :ref:`Constraint`:

- :ref:`BRAF V600 <BrafV600>`
- :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count) <CategoricalCnvEx1>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy change) <CategoricalCnvEx2>`
- :ref:`TP53 Loss <Tp53CopyLoss>`

A representative example of this Constraint, from :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count) <CategoricalCnvEx1>`:

.. literalinclude:: ../../../../examples/json/categoricalCnv-ex1.json
  :language: json
  :lines: 44-99

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used to describe a Categorical Variant using a VRS :ref:`Sequence Location <SequenceLocation>` object, such as defining a specific exon or genomic segment.

location
########

The *location* attribute is required and must be a valid VRS :ref:`Sequence Location <SequenceLocation>`. We recommend the following resources for constructing :ref:`Sequence Location <SequenceLocation>` objects:

- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate a VRS digest for a given sequence location.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Allele objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Location`` exists upon. Consider the following values, depending on the type of ``Location`` expressed:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Location type
     - moleculeType
     - residueAlphabet
   * - Nucleotide
     - genomic
     - na
   * - RNA
     - RNA
     - na
   * - mRNA
     - mRNA
     - na
   * - Protein
     - protein
     - aa

For additional Implementation Guidance, please visit `VRS' page for the Sequence Location concept <https://vrs.ga4gh.org/en/latest/concepts/LocationAndReference/SequenceLocation.html>`_.

relations
#########

The *relations* attribute is optional and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from a defined ontology. Relation terms describe how *members* of a :ref:`Categorical Variant <CategoricalVariant>` relate to the Defining :ref:`Sequence Location <SequenceLocation>`.

.. note:: *relations* are **not** definitional and thus do not alter the scope of the Categorical Variant's definition. In other words, they do not restrict or expand which variants satisfy the Categorical Variant's constraints. However, they **are** definitional for some :ref:`Recipes <Recipes>`.

The following relation terms are some to consider using with this Constraint:

.. warning:: Some relation-terms are based on the system ``ga4gh-gks-term``. This is an internally controlled ontology for use specifically with the Categorical Variant Representation Specification.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - How the ``member`` relates to the Categorical Variant
   * - ga4gh-gks-term:self
     - Use when the ``member`` is the Defining ``Sequence Location`` itself.
   * - ga4gh-gks-term:liftover_of
     - Use when the ``member`` is the "same" genomic Sequence Location, as represented on another reference genome.
   * - ga4gh-gks-term:projection_of
     - Use when the ``member`` is the "same" RNA (pre-mRNA), mRNA, or protein Sequence Location, as represented on another transcript or protein isoform.

matchCharacteristic
###################

The *matchCharacteristic* attribute is required and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from an externally defined ontology. This attribute is used to describe *how* members' Sequence Location relates to the Defining Sequence Location. We recommend using one of the terms from either the the `Sequence Ontology <https://www.ebi.ac.uk/ols4/ontologies/so>`_ and the `Relations Ontology <https://www.ebi.ac.uk/ols4/ontologies/ro>`_:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - :ref:`Coding <Coding>`
     - Name
     - Use case
   * - skos:exactMatch
     - exactMatch
     - Use when the ``member``'s ``Sequence Location`` exactly matches the Defining ``Sequence Location`` itself.
   * - `RO:0000050 <https://www.ebi.ac.uk/ols4/ontologies/flopo/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000050?lang=en>`_
     - part of
     - Use when the ``members``'s ``Sequence Location`` is entirely within the Defining ``Sequence Location``, a narrow match.
   * - `RO:0000051 <https://www.ebi.ac.uk/ols4/ontologies/flopo/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000051?lang=en>`_
     - has part
     - Use when the ``members``'s ``Sequence Location`` entirely contains the Defining ``Sequence Location``, a broad match.
   * - `RO:0002151 <https://www.ebi.ac.uk/ols4/ontologies/flopo/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0002151?lang=en>`_
     - partially overlaps
     - Use when the ``members``'s ``Sequence Location`` partially overlaps with the Defining ``Sequence Location``, a broad match.

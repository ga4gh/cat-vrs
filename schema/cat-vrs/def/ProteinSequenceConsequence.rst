**Computational Definition**

A change that occurs in a protein sequence as a result of genomic changes. Due to the degenerate nature of the genetic code, there are often several genomic changes that can cause a protein sequence consequence. The protein sequence consequence, like a :ref:`CanonicalAllele`, is defined by an `Allele <https://vrs.ga4gh.org/en/2.x/concepts/MolecularVariation/Allele.html#>` that is representative of a collection of congruent Protein Alleles that share the same altered codon(s).

**Information Model**

Some ProteinSequenceConsequence attributes are inherited from :ref:`CategoricalVariation`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - mappings
      - :ref:`ConceptMapping`
      - 0..m
      - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
   *  - members
      - :ref:`Variation` | :ref:`IRI`
      - 0..m
      - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
   *  - type
      - string
      - 1..1
      - MUST be "ProteinSequenceConsequence"
   *  - definingContext
      - :ref:`Allele` | :ref:`IRI`
      - 1..1
      - The `Allele <https://vrs.ga4gh.org/en/2.x/concepts/MolecularVariation/Allele.html#>`_ object that is congruent with (projects to the same codons) as alleles on other protein reference sequences.

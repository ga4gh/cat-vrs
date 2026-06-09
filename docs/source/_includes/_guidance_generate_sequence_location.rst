We recommend the following resources for constructing :ref:`Sequence Location <SequenceLocation>` objects:

- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate a VRS digest for a Sequence Location.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information, such as names and aliases, when constructing Sequence Location objects directly.

.. note:: While neither the *moleculeType* nor *residueAlphabet* are required attributes for a :ref:`Sequence Reference <SequenceReference>`, we strongly recommend populating them within your implementation to clearly communicate to users what type of sequence your ``Location`` exists upon. Consider the following values, depending on the type of ``Location`` expressed:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Sequence reference type
     - moleculeType
     - residueAlphabet
   * - Genomic
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

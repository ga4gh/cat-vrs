We recommend the following resources for constructing VRS objects:

- The `Variant Normalizer <https://github.com/cancervariants/variation-normalization/>`_ is a Python package and
  public REST instance that translates plain-text HGVS expressions (for example, "NM_004333.4:c.1799T>A") or free text natural language input (for example, "BRAF V600E") into `Normalized VRS Allele
  objects <https://vrs.ga4gh.org/en/latest/conventions/normalization.html#allele-normalization>`_.
  Genomic coordinates default to GRCh38, transcripts default to `MANE Select transcripts <https://www.ncbi.nlm.nih.gov/refseq/MANE/>`_, and HGVS del dup mode unless otherwise specified.
- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference
  implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate VRS digests for
  an Allele, Sequence Location, Sequence Reference, and other VRS concepts.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information,
  such as names and aliases, when constructing Sequence Reference objects directly.

We recommend the following resources for constructing VRS objects:

- The `Variation Normalizer <https://github.com/cancervariants/variation-normalization/>`_ is a Python package and
  public REST instance that translates plain-text HGVS expressions (for example, "NM_004333.4:c.1799T>A") or free text natural language input (for example, "BRAF V600E") into `Normalized VRS Allele
  objects <https://vrs.ga4gh.org/en/latest/conventions/normalization.html#allele-normalization>`_. The ``/normalize`` endpoint will lift genomic coordinates to the preferred GRCh38 assembly and transcripts will use the `transcript selection algorithm <https://coolseqtool.readthedocs.io/stable/transcript_selection.html>`_. Additionally, `HGVS Dup Del Mode <https://github.com/cancervariants/variation-normalization/blob/main/docs/hgvs_dup_del_mode.md>`_ will be applied for deletions and duplications represented as HGVS expressions.
- `vrs-python <https://github.com/ga4gh/vrs-python>`_ is a Python package and reference
  implementation for `VRS <https://vrs.ga4gh.org>`_ that can be used to generate VRS digests for
  an Allele, Sequence Location, Sequence Reference, and other VRS concepts.
- `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ provides access to reference
  sequences and can be used to obtain :ref:`Sequence Reference <SequenceReference>` information,
  such as names and aliases, when constructing Sequence Reference objects directly.

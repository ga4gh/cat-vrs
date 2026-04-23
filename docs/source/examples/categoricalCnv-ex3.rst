:orphan:
.. _CategoricalCnvEx3:

GRCh38 Xp22.31(chrX:6978350-7594949)x3
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Source**: `ClinGen CACN42032202 <https://reg.clinicalgenome.org/redmine/projects/Registry/genboree_registry/by_canonicalid?canonicalid=CACN42032202>`_

**Recipes that this example satisfies**: :ref:`Categorical CNV <CategoricalCnv>`

.. rubric:: Attributes

- ``id``: clingen:cacn42032202, where CACN42032202 is the Canonical CNV Identifier listed by ClinGen.
- ``type``: CategoricalVariant, as required by the specification.
- ``name``: GRCh38 Xp22.31(chrX:6978350-7594949)x3, the Community Standard Title listed for the variant by ClinGen.
- ``description``: A brief placeholder note, as ClinGen does not contain a longform description of this variant.
- ``aliases``: The HGVS representations for GRCh38 (NC_000023.11) and GRCh37 (NC_000023.10) are listed.
- ``extensions``: The cytogenetic location (Xp22.31) was obtained from the Community Standard Title for this variant.
- ``mappings``: A mapping to ClinGen's webpage for this variant is included.

.. rubric:: Constraints

:ref:`Copy Count Constraint <CopyCountConstraint>`: The ``copies`` field is set to 3, reflecting the "x3" copy count specified in the variant name as provided by ClinGen.

:ref:`Defining Location Constraint <DefiningLocationConstraint>`: The defining location is a VRS Sequence Location on chromosome X (refseq:NC_000023.11, GRCh38), extracted from the GRCh38 CopyNumberCount included within ``members``. Unlike :ref:`categoricalCnv-ex1 <CategoricalCnvEx1>` and :ref:`categoricalCnv-ex2 <CategoricalCnvEx2>`, this example uses ranged values for both the ``start`` and ``end`` positions to reflect uncertainty in the breakpoint locations, specifying start within the interval 6,978,350–6,996,235 and end within 7,564,455–7,594,949.

.. rubric:: Members

The ``members`` field includes one VRS CopyNumberCount object generated using the VICC Variation Normalizer: NC_000023.11:g.(6978350_6996235)_(7564455_7594949)dup on the GRCh38 chromosome X reference sequence, with a copies value of 3 and ranged start and end positions reflecting breakpoint uncertainty.

.. rubric:: Full example: JSON

.. literalinclude:: ../../../examples/json/categoricalCnv-ex3.json
   :language: json

.. rubric:: Full example: YAML

.. literalinclude:: ../../../examples/yaml/categoricalCnv-ex3.yaml
   :language: yaml

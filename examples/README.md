# Examples - Categorical Variant Representation Specification

This README is automatically generated from the [Makefile](./Makefile) and [an accompanying Python script](./generate_readme.py). **Please edit examples in [YAML](./yaml/)** When ready to compile, run the Makefile to generate both the [JSON versions](./json/) and this README. From this directory:

```bash
make all
```

## Examples by Constraint

A Constraint is a rule or set of rules that must be satisfied for a CategoricalVariant to be considered valid. Constraint sub classes are only used in CategoricalVariant objects.

| Constraint | Representative examples |
| --- | --- |
| AdjacencyConstraint | [?::ZNF384(ncbi:171017)](json/adjacencyFusion-ex3.json), [BCR(ncbi:613)::ABL1(ncbi:25)](json/adjacencyFusion-ex1.json), [FGFR2(hgnc:3689)::v](json/adjacencyFusion-ex4.json), [v::NTRK1(hgnc:8031)](json/adjacencyFusion-ex2.json) |
| CopyChangeConstraint | [GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy change)](json/categoricalCnv-ex2.json), [TP53 Loss](json/tp53-copy-loss.json), [TP53 Loss (annotated)](json/tp53-copy-loss.annotated.json) |
| CopyCountConstraint | [GRCh38 Xp22.31(chrX:6978350-7594949)x3](json/categoricalCnv-ex3.json), [GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count)](json/categoricalCnv-ex1.json) |
| DefiningAlleleConstraint | [EGFR L858R](json/proteinSequenceConsequence-ex1.json), [NC_000001.11:g.1699974C>G](json/canonicalAllele-ex2.json), [NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)](json/canonicalAllele-ex1.json), [NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)](json/proteinSequenceConsequence-ex2.json), [PIK3CA p.R38H](json/functionVariant-ex3.json) |
| DefiningLocationConstraint | [BRAF V600](json/braf-v600.json), [BRAF V600 (annotated)](json/braf-v600.annotated.json), [GRCh38 Xp22.31(chrX:6978350-7594949)x3](json/categoricalCnv-ex3.json), [GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy change)](json/categoricalCnv-ex2.json), [GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 (copy count)](json/categoricalCnv-ex1.json), [TP53 Loss](json/tp53-copy-loss.json), [TP53 Loss (annotated)](json/tp53-copy-loss.annotated.json) |
| FeatureContextConstraint | [BRCA2 loss of function variants](json/functionVariant-ex2.json), [NRAS functionally normal variants](json/functionVariant-ex1.json), [PIK3CA p.R38H](json/functionVariant-ex3.json), [TP53 Loss](json/tp53-copy-loss.json), [TP53 Loss (annotated)](json/tp53-copy-loss.annotated.json) |
| FunctionConstraint | [BRCA2 loss of function variants](json/functionVariant-ex2.json), [NRAS functionally normal variants](json/functionVariant-ex1.json), [PIK3CA p.R38H](json/functionVariant-ex3.json) |
| None | [t(2;15)(q23.1;q25.3)](json/describedVariant-ex1.json) |

# Examples - Categorical Variant Representation Specification


## Examples by Constraint
A [constraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#constraint) is a rule or set of rules that must be satisfied for a CategoricalVariant to be considered valid. Constraint sub classes are only used in CategoricalVariant objects.

| Constraint | Representative example(s)                                                                                                                                                                                                      |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DefiningAlleleConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#definingalleleconstraint) | [canonicalAllele-ex1](#canonicalAllele-ex1), [canonicalAllele-ex2](#canonicalAllele-ex2), [proteinSequenceConsequence-ex1](#proteinSequenceConsequence-ex1), [proteinSequenceConsequence-ex2](#proteinSequenceConsequence-ex2) |
| [DefiningLocationConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#defininglocationconstraint) | [categoricalCnv-ex1](#categoricalCnv-ex1), [categoricalCnv-ex2](#categoricalCnv-ex2), [braf-v600](#braf-v600), [tp53-copy-loss](#tp53-copy-loss)                                                                                                                                           |
| [AdjacencyConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#adjacencyconstraint) | [adjacencyFusion-ex1](#adjacencyfusion-ex1) |
| [CopyCountConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#copycountconstraint) | [categoricalCnv-ex1](#categoricalCnv-ex1), [categoricalCnv-ex3](#categoricalCnv-ex3)                                                                                                                                           |
| [CopyChangeConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#copychangeconstraint) | [categoricalCnv-ex2](#categoricalCnv-ex2), [tp53-copy-loss](#tp53-copy-loss)                                                                                                                                                                                      |
| [FeatureContextConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#featurecontextconstraint) | [tp53-copy-loss](#tp53-copy-loss)                                                                                                                                                                                      |
| [FunctionConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#functionconstraint) | [functionVariant-ex1](#functionVariant-ex1), [functionVariant-ex2](#functionVariant-ex2), [functionVariant-ex3](#functionVariant-ex3)                                                                                                                                                                                     |
| None | [describedVariant-ex1](#describedVariant-ex1)                                                                                                                                                                                  |

## Examples by Recipe
[Recipes](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html) are pre-defined CategoricalVariants with specific constraints that represent standard categorical variants that have been identified in variant knowledgebases and registries.

| Recipe | Representative example(s) |
|---|---|
| [CanonicalAllele](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#canonicalallele) | [canonicalAllele-ex1](#canonicalAllele-ex1), [canonicalAllele-ex2](#canonicalAllele-ex2) |
| [ProteinSequenceConsequence](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#proteinsequenceconsequence) | [proteinSequenceConsequence-ex1](#proteinSequenceConsequence-ex1), [proteinSequenceConsequence-ex2](#proteinSequenceConsequence-ex2) |
| [CategoricalCnv](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#categoricalcnv) | [categoricalCnv-ex1](#categoricalCnv-ex1), [categoricalCnv-ex2](#categoricalCnv-ex2) |
| [FunctionVariant](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#functionvariant) | [functionVariant-ex1](#functionVariant-ex1), [functionVariant-ex2](#functionVariant-ex2), [functionVariant-ex3](#functionVariant-ex3) |
| None | [braf-v600](#braf-v600), [tp53-copy-loss](#tp53-copy-loss) |

# About each example
Here, we provide examples of representing several types of variation from other knowledgebases as Categorical Variants. All example Categorical Variants will be modeled using fields required by the [Categorical Variant](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#categorical-variant) class within the specification.

## adjacencyFusion-ex1
[adjacencyFusion-ex1.yaml](./adjacencyFusion-ex1.yaml) represents [CIViC variant id 1: _BCR_::_ABL1_ Fusion](https://civicdb.org/variants/1/summary) as a Categorical Variant. Fields were populated as follows:
- `id`: `civic.vid:` followed by the listed Variant ID, "1", contained within the URL for the genomic alteration. `vid` within the `id` stands for [Variant ID](https://civicdb.org/variants/home), CIViC's way to represent variants.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label given to the genomic alteration by CIViC, "BCR::ABL1", with Gene identifiers per the [VICC Fusion](https://fusions.cancervariants.org/en/latest/information_model.html) representation recommendation. CIViC provided NCBI identifiers for the genes, so we used those.
- `description`: CIViC does not provide a longform description of "BCR::ABL1", so this field was left preallocated with the following text: "An optional field to describe BCR::ABL1".
- `aliases`: All aliases for _BCR_::_ABL1_ as provided by CIViC.
- `extensions`: The `5'` and `3' Partner Representative Genomic Coordinates` provided by CIViC for _BCR_::_ABL1_.

This example applies the [AdjacencyConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#adjacencyconstraint) to represent it as a Categorical Variant. Both genes are modeled as mappable concepts, using the NCBI gene id provided by CIViC.

## adjacencyFusion-ex2
[adjacencyFusion-ex2.yaml](./adjacencyFusion-ex2.yaml) represents [CIViC feature id 62026: v::_NTRK1_ Fusion](https://civicdb.org/features/62026/summary) as a Categorical Variant. Fields were populated as follows:
- `id`: `civic.fid:` followed by the listed Feature ID, "62026", contained within the URL for the genomic alteration. `fid` within the `id` stands for [Feature ID](https://civicdb.org/features/home), CIViC's way to represent genomic features.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label given to the genomic alteration by CIViC, "v::NTRK1", with Gene identifiers per the [VICC Fusion](https://fusions.cancervariants.org/en/latest/information_model.html) representation recommendation. CIViC provided did not provide identifiers for the genes, so we used HGNC identifiers.
- `description`: CIViC does not provide a longform description of "v::NTRK1", so this field was left preallocated with the following text: "An optional field to describe v::NTRK1(hgnc:8031)".
- `aliases`: CIViC does not provide any aliases for this fusion. Thus, we added `v::NTRK1` and `NTRK1 fusion` to the aliases as examples.

This example applies the [AdjacencyConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#adjacencyconstraint) to represent it as a Categorical Variant. CIViC lists multiple possible fusion partners for the 5' partner, and _NTRK1_ as the 3' partner. Thus, the 5' partner is listed within the `adjoinedElements` array as `multipleKnownGeneElements` with `knownElements` including all known elements cataloged in [COSMIC Fusion](https://cancer.sanger.ac.uk/cosmic/fusion) with _NTRK1_ listed as a partner. The 3' partner includes _NTRK1_ as a mappable concept.

## adjacencyFusion-ex3
[adjacencyFusion-ex3.yaml](./adjacencyFusion-ex3.yaml) represents [CIViC variant id 5186: ?::_ZNF384_ Fusion](https://civicdb.org/variants/5186/summary) as a Categorical Variant. Fields were populated as follows:
- `id`: `civic.vid:` followed by the listed Variant ID, "5186", contained within the URL for the genomic alteration. `vid` within the `id` stands for [Variant ID](https://civicdb.org/variants/home), CIViC's way to represent genomic variants.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label given to the genomic alteration by CIViC, "?::ZNF384", with Gene identifiers per the [VICC Fusion](https://fusions.cancervariants.org/en/latest/information_model.html) representation recommendation. CIViC provided NCBI identifiers for the genes, so we used those.
- `description`: CIViC does not provide a longform description of "?::ZNF384", so this field was left preallocated with the following text: "An optional field to describe ?::ZNF384(ncbi:171017)".
- `aliases`: CIViC provides "ZNF384 Fusion" as an alias for this fusion. Thus, we added this alias as well as `?::ZNF384` to the aliases as examples.

This example applies the [AdjacencyConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#adjacencyconstraint) to represent it as a Categorical Variant. CIViC lists unknown Gene Element for the 5' partner, and _ZNF384_ as the 3' partner of this fusion. Thus, the 5' partner is listed within the `adjoinedElements` array as `unknownGeneComponent` and the 3' partner includes _ZNF384_ as a mappable concept.

## canonicalAllele-ex1
[canonicalAllele-ex1](./canonicalAllele-ex1.yaml) represents [ClinVar entry 662001](https://www.ncbi.nlm.nih.gov/clinvar/variation/662001/?oq=662001&m=NM_004958.4(MTOR):c.5992_5993del%20(p.Met1998fs)), NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs), as a Categorical Variant. This example satisfies the [CanonicalAllele Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#canonicalallele). Fields were populated as follows:

- `id`: `clinvar:` followed by the listed Variation ID, "662001", contained within the Identifiers section of Variant Details.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label listed within the Identifiers section of Variant Details, "NM_004958.4(MTOR):c.5992_5993del (p.Met1998fs)".
- `description`: No description was populated because ClinVar does not contain a longform description of the variant.
- `aliases`: All listed hgvs representations within ClinVar's Variant Details for the variant.
- `extensions`: The values for the extensions named "cytogenetic location" and "clinvar variation type" were obtained from the Location and Type and length sections within ClinVar's Variant Details for the variant. Values for the extension named "hgvs list" included hgvs representations for the variant, as provided by ClinVar in the HGVS section within ClinVar's Variant Details for the variant.
- `mappings`: mappings to resources included within the Links section within ClinVar's Varaint Details for the variant are included. Specifically, mappings to ClinVar's page for the variant, ClinGen, VarSome, and dbSNP.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for the hgvs.g and hgvs.c MANE Select representation of this variant ("NC_000001.11:g.11128044_11128045del" and "NM_004958.4:c.5992_5993del").

This example applies the [DefiningAlleleConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#definingalleleconstraint) to represent it as a Categorical Variant. The Allele associated with the MANE Select representation, "NM_004958.4:c.5992_5993del", as included within the `members` field, was used to populate the `allele` field.

## canonicalAllele-ex2
[canonicalAllele-ex2](./canonicalAllele-ex2.yaml) represents [ClinGen entry CA415424538](https://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA415424538) as a Categorical Variant. This example satisfies the [CanonicalAllele Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#canonicalallele). Fields were populated as follows:

- `id`: `clingen:` followed by the listed Canonical Allele Identifier, "CA415424538", listed for the variant.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The GRCh38 HGVS Genomic Allele listed for the variant by ClinGen.
- `description`: No description was populated because ClinGen does not contain a longform description of the variant.
- `aliases`: The HGVS representations of genomic alleles for the GRCh38 and GRCh38 genome assemblies were listed, as provided by ClinGen.
- `extensions`: The value for extension named "cytogenetic location" was obtained from the HGNC page for the Genes listed for this Canonical Allele, [MMP23A (HGNC:7170)](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7170) and [MMP23B (HGNC:7171)](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7171). Values for the extension named "hgvs list" included hgvs.g representations for the Canonical Allele, as provided by ClinGen for the GRCh38 and GRCh37 genomic alleles.
- `mappings`: mappings to resources included within the "Linked Data" section of ClinGen's page for this Canonical Allele. Specifically, we included mappings to ClinGen's webpage, dbSNP, and gnomAD v2, v3, and v4.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for the hgvs.g representations of this variant on GRCh38 and GRCh37, respectively ("NC_000001.11:g.1699974C>G" and "NC_000001.10:g.1631413C>G").

This example applies the [DefiningAlleleConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#definingalleleconstraint) to represent it as a Categorical Variant. The Allele associated with the GRCh38 VRS Allele, "NC_000001.11:g.1699974C>G", as included within the `members` field, was used to populate the `allele` field.

## categoricalCNV-ex1
[categoricalCNV-ex1](./categoricalCNV-ex1.yaml) represents [ClinVar entry 151061](https://www.ncbi.nlm.nih.gov/clinvar/variation/151061/?oq=151061&m=GRCh38%2Fhg38+7p22.1(chr7:5905831-6014161)x3) as a Categorical Variant. This example satisfies the [CategoricalCNV Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#categoricalcnv). Fields were populated as follows:

- `id`: `clinvar:` followed by the listed Variation ID, "151061", contained within the Identifiers section of Variant Details.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label listed within the Identifiers section of Variant Details, "GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3".
- `description`: No description was populated because ClinVar does not contain a longform description of the variant.
- `aliases`: All listed hgvs representations within ClinVar's Variant Details for the variant.
- `extensions`: The values for the extensions named "cytogenetic location" and "clinvar variation type" were obtained from the Location and Type and length sections within ClinVar's Variant Details for the variant. Values for the extension named "hgvs list" included hgvs representations for the variant, as provided by ClinVar in the HGVS section within ClinVar's Variant Details for the variant.
- `mappings`: mappings to resources included within the Links section within ClinVar's Varaint Details for the variant are included. Specifically, mappings to ClinVar's page for the variant and dbVar were included.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS CopyNumberChange](https://cat-vrs.readthedocs.io/en/stable/concepts/imported/CopyNumberChange.html) for the hgvs.g representations of this variant ("NC\_000007.14:g.(?\_5905831)\_(6014161\_?)dup" and "NC_000007.13:g.(?\_5945462)\_(6053792\_?)dup").

This example applies two constraints: [CopyCountConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#copycountconstraint) and [DefiningLocationConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#defininglocationconstraint). The `copies` field of CopyCountConstraint is set to "3", per the copies being specified as "x3" within the `name` field, as specified by ClinVar. The DefiningLocationConstraint includes the [VRS Sequence Location](https://cat-vrs.readthedocs.io/en/stable/concepts/imported/SequenceLocation.html#sequencelocation) from the NC_000007.14 CopyNumberChange included within `members`.

## categoricalCNV-ex2
[categoricalCNV-ex2](./categoricalCNV-ex2.yaml) represents [ClinVar entry 151061](https://www.ncbi.nlm.nih.gov/clinvar/variation/151061/?oq=151061&m=GRCh38%2Fhg38+7p22.1(chr7:5905831-6014161)x3) as a Categorical Variant. This example satisfies the [CategoricalCNV Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#categoricalcnv).

This example is identical to [categoricalCNV-ex1](./categoricalCNV-ex1.yaml), except that it applies [CopyChangeConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#copychangeconstraint) instead of [CopyCountConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#copycountconstraint). The `copyChange` field is populated as a mappableConcept, identical to the `copyChange` field within VRS variations listed under `members`.

Fields were otherwise populated identical to [categoricalCNV-ex1](./categoricalCNV-ex1.yaml).

## categoricalCNV-ex3
[categoricalCNV-ex3](./categoricalCnv-ex3.yaml) represents [ClinGen entry CACN42032202](https://reg.clinicalgenome.org/redmine/projects/Registry/genboree_registry/by_canonicalid?canonicalid=CACN42032202) as a Categorical Variant. This example satisfies the [CategoricalCNV Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#categoricalcnv). Fields were populated as follows:

- `id`: `clingen:` followed by the listed Canonical Allele Identifier, "CACN42032202", listed for the variant.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The Community Standard Title listed for the variant by ClinGen.
- `description`: No description was populated because ClinGen does not contain a longform description of the variant.
- `aliases`: The HGVS representations of genomic alleles for the GRCh38 and GRCh38 genome assemblies were listed.
- `extensions`: The value for extension named "cytogenetic location" was obtained from the Community Standard Title for this variant.
- `mappings`: mapping to ClinGen's webpage for this variant.

This example applies two constraints: [CopyCountConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#copycountconstraint) and [DefiningLocationConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#defininglocationconstraint). The `copies` field of CopyCountConstraint is set to "3", per the copies being specified as "x3" within the `name` field, as specified by ClinGen. The DefiningLocationConstraint includes the [VRS Sequence Location](https://cat-vrs.readthedocs.io/en/stable/concepts/imported/SequenceLocation.html#sequencelocation) from the GRCh38 representation of this variant, as included within `members`. Unlike [categoricalCNV-ex1](./categoricalCnv-ex1.yaml) and [categoricalCNV-ex2](./categoricalCnv-ex2.yaml), this example includes ranges for the `start` and `end` positions.

## describedVariant-ex1
[describedVariant-ex1](./describedVariant-ex1.yaml) represents [ClinVar entry 1177130](https://www.ncbi.nlm.nih.gov/clinvar/variation/1177130/?oq=1177130&m=t(2%3B15)(q23.1%3Bq25.3)), t(2;15)(q23.1;q25.3). This example **does not include any constraints**. Implementers may choose to represent Categorical Variants in this way while waiting for the specification to support a means to model them. Given this, fields were populated as follows:

- `id`: `clinvar:` followed by the listed Variation ID, "1177130, contained within the Identifiers section of Variant Details.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label listed within the Identifiers section of Variant Details, "t(2;15)(q23.1;q25.3)".
- `description`: No description was populated because ClinVar does not contain a longform description of the variant.
- `aliases`: was left empty because ClinVar does not provide any alternative representations of this variant.
- `extensions`: The values for the extensions named "cytogenetic location" and "clinvar variation type" were obtained from the Location and Type and length sections within ClinVar's Variant Details for the variant.
- `mappings`: was left empty because ClinVar does not provide any mappings within the Links section of this variant's Variant Details.
- `members`: was left empty because [VRS](https://vrs.ga4gh.org/en/stable/) does not yet support translocations.

## functionVariant-ex1
[functionVariant-ex1](./functionVariant-ex1.yaml) represents _NRAS_ functionally normal variants, which closely resembles the [CIViC entry for NRAS Wild type](https://civicdb.org/molecular-profiles/4428/summary). This example satifies the [FunctionVariant Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#functionvariant). Fields were populated as follows:
- `id`: `civic.mpid:` followed by the listed Molecular Profile ID, "4428", contained within the url for the genomic alteration. `id` stands for [Molecular Profile ID](https://docs.civicdb.org/en/latest/model/molecular_profiles/overview.html), CIViC's way to represent groups of genomic alterations.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: While CIViC represents Wild type _NRAS_ with this Molecular Profile, we instead name this example "NRAS functionally normal variants" to represent the set of _NRAS_ variants that are likely neutral.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for NM_002524.5(NRAS):c.170A>C(p.D57A), a variant [categorized as Likely Neutral by OncoKB](https://www.oncokb.org/gene/NRAS#tab=Biological).

This example applies two constraints: [FeatureContextConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#featurecontextconstraint) and [FunctionConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#functionconstraint). Both the `featureContext` and `functionConsequence` properties are [MappableConcept](https://cat-vrs.ga4gh.org/en/latest/concepts/imported/MappableConcept.html)s, and include mappings to [NRAS (HGNC:7989)](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7989) and [functionally_normal (SO:0002219)](http://www.sequenceontology.org/browser/current_release/term/SO:0002219).

## functionVariant-ex2
[functionVariant-ex2](./functionVariant-ex2.yaml) represents _BRCA2_ loss of function variants, based on the [CIViC entry for BRCA2 Mutation with Loss Of Function Variant Type](https://civicdb.org/molecular-profiles/186/summary). This example satifies the [FunctionVariant Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#functionvariant). Fields were populated as follows:
- `id`: `civic.mpid:` followed by the listed Molecular Profile ID, "186", contained within the url for the genomic alteration. `id` stands for [Molecular Profile ID](https://docs.civicdb.org/en/latest/model/molecular_profiles/overview.html), CIViC's way to represent groups of genomic alterations.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: "BRCA2 loss of function variants" to represent the set of _BRCA2_ variants that result in loss of function.

This example applies two constraints: [FeatureContextConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#featurecontextconstraint) and [FunctionConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#functionconstraint). Both the `featureContext` and `functionConsequence` properties are [MappableConcept](https://cat-vrs.ga4gh.org/en/latest/concepts/imported/MappableConcept.html)s, and include mappings to [BRCA2 (HGNC:1101)](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1101) and [loss_of_function (SO:0002054)](http://www.sequenceontology.org/browser/current_release/term/SO:0002054).

## functionVariant-ex3
[functionVariant-ex3](./functionVariant-ex3.yaml) represents NM_006218.4(_PIK3CA_):c.113G>A(p.Arg38His), based on the [CIViC entry for _PIK3CA_ R38H](https://civicdb.org/molecular-profiles/1150/summary). This example satifies the [FunctionVariant Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#functionvariant) as a gain of function variant. Fields were populated as follows:
- `id`: `civic.mpid:` followed by the listed Molecular Profile ID, "1150", contained within the url for the genomic alteration. `id` stands for [Molecular Profile ID](https://docs.civicdb.org/en/latest/model/molecular_profiles/overview.html), CIViC's way to represent groups of genomic alterations.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: "PIK3CA p.R38H" to follow the naming convention used by CIViC.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for NM_006218.4:c.113G>A.

This example includes three constraints: [DefiningAlleleConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#definingalleleconstraint), [FeatureContextConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#featurecontextconstraint), and [FunctionConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#functionconstraint). Both the `featureContext` and `functionConsequence` properties are [MappableConcept](https://cat-vrs.ga4gh.org/en/latest/concepts/imported/MappableConcept.html)s, and include mappings to [PIK3CA (HGNC:8975)](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8975) and [gain_of_function (SO:0002053)](http://www.sequenceontology.org/browser/current_release/term/SO:0002053).

## proteinSequenceConsequence-ex1.yaml
[proteinSequenceConsequence-ex1](./proteinSequenceConsequence-ex1.yaml) represents [CIViC entry for EGFR L858R](https://civicdb.org/variants/33/summary) as a Categorical Variant. This example satisfies the [ProteinSequenceConsequence Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#proteinsequenceconsequence). Fields were populated as follows:

- `id`: `civic.mpid:` followed by the listed Molecular Profile ID, "33", contained within the url for the genomic alteration. `mpid` within the `id` stands for [Molecular Profile ID](https://docs.civicdb.org/en/latest/model/molecular_profiles/overview.html), CIViC's way to represent groups of genomic alterations.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label given to the genomic alteration by CIViC, "EGFR L858R"
- `description`: The longform description of "EGFR L858R", as provided by [CIViC](https://civicdb.org/molecular-profiles/33/summary).
- `aliases`: All aliases, HGVS Descriptions, and MANE Select Transcript listed for "EGFR L858R" within the Summary section of the variant's page, as provided by CIViC.
- `extensions`: The values for the extensions named "CIViC Representative Variant Coordinates" and "CIViC Variant Type" come from the "Representative Variant Coordinates" and "Variant Type" sections of the CIViC's Summary for this variant. The Variant Type was mapped to [Sequence Ontology](http://www.sequenceontology.org/browser/release_2.5.3/term/SO:0001583). The values for the extension names "hgvs" are derived from the "HGVS Descriptions" and "MANE Select Transcript" sections of CIViC's Variant Summary.
- `mappings`: mappings were included for CIViC variant and molecular profile page, as well as ClinGen, ClinVar, and dbSNP pages linked from CIViC's variant page for this example.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for HGVS representations of this variant (NC_000007.13:g.55259515T>G, NM_005228.5:c.2573T>G, and NP_005219.2:p.Leu858Arg).

This example applies the [DefiningAlleleConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#definingalleleconstraint) to represent it as a Categorical Variant. The Allele associated with the hgvs.p representation, "NP_005219.2:p.Leu858Arg", as included within the `members` field, was used to populate the `allele` field.

## proteinSequenceConsequence-ex2.yaml
[proteinSequenceConsequence-ex2](./proteinSequenceConsequence-ex2.yaml) represents [ClinVar entry 55628](https://www.ncbi.nlm.nih.gov/clinvar/variation/55628/), NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter), as a Categorical Variant. This example satisfies the [ProteinSequenceConsequence Recipe](https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html#proteinsequenceconsequence). Fields were populated as follows:

- `id`: `clinvar:` followed by the listed Variation ID, "55628", contained within the Identifiers section of Variant Details.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable label listed within the Identifiers section of Variant Details, "NM_007294.4(BRCA1):c.5558dup (p.Tyr1853Ter)".
- `description`: No description was populated because ClinVar does not contain a longform description of the variant.
- `aliases`: ClinVar includes many representations within the HGVS section of Variant Details for this variant. We list a subset of HGVS representations as aliases: the MANE Select nucleotide coding and protein expression, the protein expressions using hgvs.p short to abbreviate the amino acids as a single letter, and both hgvs.g variants. We additionaly include the Canonical SPDI representation that ClinVar provides.
- `extensions`: The values for the extensions named "cytogenetic location" and "clinvar variation type" were obtained from the Location and Type and length sections within ClinVar's Variant Details for the variant. Values for the extension named "hgvs list" included hgvs representations for the variant, as provided by ClinVar in the HGVS section within ClinVar's Variant Details for the variant.
- `mappings`: a subset of mappings to resources included within the Links section within ClinVar's Varaint Details for the variant are included. Specifically, mappings to ClinVar's page for the variant, ClinGen, and dbSNP.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for the hgvs.g, hgvs.c MANE Select representation and corresponding hgvs.p of this variant ("NC_000017.11:g.43045712dup", "NC_000017.10:g.41197729dup", and "NP_009225.1:p.Tyr1853Ter"); the variant normalization service was unable to generate a VRS Allele for "NM_007294.4:c.5558dup".

This example applies the [DefiningAlleleConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#definingalleleconstraint) to represent it as a Categorical Variant. The Allele associated with the MANE Select's representation, "NP_009225.1:p.Tyr1853Ter", as included within the `members` field, was used to populate the `allele` field.

## braf-v600
[braf-v600](./braf-v600.yaml) represents [CIViC entry 17](https://civicdb.org/variants/17/summary), BRAF V600, as a Categorical Variant. Fields were populated as follows:

- `id`: `civic.vid:` followed by the listed Variation ID, "17".
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The human readable name.
- `description`: A summary was written of the categorical variant.
- `aliases`: Representations with the MANE Select transcript for BRAF were shown.
- `extensions`: The CIViC Variant Representative Coordinates were included.
- `mappings`: A set of ClinVar variants that are amino acid substitutions at BRAF V600.
- `members`: The [VICC variant normalization](https://github.com/cancervariants/variation-normalization) was used to translate hgvs representations into [VRS variations](https://vrs.ga4gh.org/en/stable/). Specifically, the `/variation/to_vrs` endpoint was used to generate a [VRS Allele](https://cat-vrs.readthedocs.io/en/latest/concepts/imported/Allele.html#allele) for the hgvs.c representations of BRAF V600E, V600K, V600R, V600M, and V600G.

This example applies the [DefiningLocationConstraint](https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#defininglocationconstraint) to represent it as a Categorical Variant.

We additionally created an [annotated](./braf-v600.annotated.yaml) version of this example, detailing each field.

## tp53-copy-loss
[tp53-copy-loss](./tp53-copy-loss.yaml) represents [TP53 Loss](https://civicdb.org/variants/4452/summary) as a Categorical Variant. Fields were populated as follows:

- `id`: `civic.vid:` followed by the variant id provided by CIViC, 4452, listed for the variant.
- `type`: specified as "CategoricalVariant", as required by [the specification](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#categorical-variant).
- `name`: The name of the variant, as provided by CIViC.
- `description`: A plain text description of the variant.
- `aliases`: "Copy Number Loss" was provided to clearly specify that this is a copy number event.
- `extensions`: The value for extension named "cytogenetic location" was obtained from HGNC for TP53.
- `mappings`: mapping to ClinGen's webpage for this variant.

This example applies two constraints: [CopyChangeConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html#copychangeconstraint) and [FeatureContextConstraint](https://cat-vrs.readthedocs.io/en/stable/concepts/catvrs_model.html). The `copyChange` field of CopyChangeConstraint uses "loss" to specify the category of copy change. FeatureContextConstraint represents the gene context with a primaryCoding to [HGNC](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11998).

We additionally created an [annotated](tp53-copy-loss.annotated.yaml) version of this example, detailing each field.

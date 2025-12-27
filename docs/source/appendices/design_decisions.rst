.. _design-decisions:

Design Decisions
!!!!!!!!!!!!!!!!

Cat-VRS contributors confronted numerous trade-offs in developing this specification. As these trade-offs may not be apparent to outside readers, this section highlights the most significant ones and the rationale for our design decisions, including the following.


Design decisions as they pertain to the `Categorical Variant Representation Specification (Cat-VRS)
<https://github.com/ga4gh/cat-vrs>`_ are categorized within this document by impact: how foundational they are to the specification. These categories are defined as follows:


* **Major impact**: Decisions that significantly alter the structure, functionality, or core principles of the product.
* **Medium impact**: Decisions that introduce moderate changes by affecting specific components or functionalities without altering the overall product.
* **Minor impact**: Decisions that involve minor tweaks or optimizations, with limited scope and minimal effect on the overall product.
* **General Principles**: Technical decisions and stylistic conventions that are observed in the Cat-VRS schema and documentation, but do not materially impact the design of the function of the standard.


Decisions are labeled based on their maturity status based on the :ref:`maturity-model`. While the Maturity Model includes draft, trial use, normative, and deprecated categories, to date all components of this product are either draft or trial use status. Components must undergo a period of public comment before changing maturity status.

Because maturity is a function of (1) the breadth of model adoption and (2) expected stability, rather than a function of how fundamental a concept is to the model, the maturity status property is entirely orthogonal to the impact of a decision on Cat-VRS.


.. contents::
   :local:
   :depth: 1


.. major_impact

Major Impact
############


.. hyperintensional_catvars

Treatment of CatVars as ((Hyper)intensional) Set-Theoretic Objects
==================================================================

**Decision:**
The group decided to model categorical variants as `hyperintensional <https://plato.stanford.edu/entries/hyperintensionality/>`_ set objects to address the complexities of categorical data representation.

**Rationale:**
This decision is comprised of three others that build atop one another, each deciding to model categorical variants (a) as sets of properties, (b) as *intensional* set objects: defined by properties of what they *are*, instead of *extensional*: defined by set membership, and (c) using a *hyper* intensional semantic model. A more in-depth rationale can be found here: :ref:`hyperintensional-catvars`.


#. **Catvars as sets:** The group recognized that catvars often represent high-order, unspecified variants, which are best conceptualized as sets to capture their broad and flexible nature within genomic knowledgebases.

#. **Catvars as intensional sets:** Given the impracticality of extensional sets–defined by their list of members--due to potentially infinite members, the group opted for intensional sets, defined by constraints on set membership, enhancing efficacy and clarity in representation.

#. **Catvars as hyperintensional sets:** To address the limitations of intensional models in distinguishing between sets with identical properties but different contextual meanings, the group adopted a hyperintensional model, allowing for nuanced differentiation and improved interoperability across different representations.


For example, an extensional set describing *BRAF*  p.V600E would need to include every possible nucleotide change that results in it, whereas an intensional set description uses concepts such as the location and protein consequence to do so. Hyperintensional semantics allows for labeling of set members to distinguish otherwise identical information; for example, 7-14075336-A-T, NM_004333.6:6.1799T>A, and rs113488022 all represent the same underlying genomic variant–which result in *BRAF*  p.V600E–and a hyperintensional model allows us to represent each of these catvars in parallel with knowledge associated with each.

**Citations:**

*  `2024-04-16 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.cexaqt7e0bcy>`_

*  `2024-04-03 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.6pvf9r63mi1h>`_

*  `2023-11-22 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.s3afo1i22mnl>`_

*  `2023-10-25 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.8xxp7lqoun48>`_

*  `2023-10-11 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.cmwm638mk3jb>`_

*  `Categorical Variation Study Group motivation and mandate <https://docs.google.com/document/d/12LMQu39hRiRATNwEYRlGqU5djRQHGar27szJTXxB3JE/edit?tab=t.0>`_


.. constraint_model

Adoption of a Constraint-Based Model Instead of a Fixed Top-Down Typology of Data Classes
=========================================================================================

**Decision:**
The group decided to use a `constraint-based model <https://github.com/ga4gh/cat-vrs/discussions/22>`_, defining categorical variants dynamically in a bottom-up fashion based on set constraints rather than in a rigid top-down hierarchy of variant types.

**Rationale:**

One challenge associated with modelling categorical variation is that new category concepts are coined on an ongoing and ad hoc basis by researchers, clinicians, and study authors. These names also reflect ongoing developments in analytical methodologies, technologies, and clinical perspectives. As a result, we expect novel catvar types to be minted in the future, and for existing catvars to be reexamined later under different lenses. Therefore, rather than attempting to prescriptively construct major catvar classes we expect to be used and enforce rigid adherence to that variant type hierarchy, the group instead took a different approach. Based on our variant test set and the use cases put forward for assayed-to-catvar and catvar-to-catvar matching, we instead attempted to determine the broad representation space of possible categorical variation, and proposed a bottom-up system to allow users to build catvars representations by specifying the values for all and only the hyperintensional set properties they know of for their given catvar.


This approach provides flexibility in defining catvars across diverse genomic applications, including somatic mutations, germline variants, and expression-based changes. It also improves interoperability with knowledge bases like CIViC and ClinVar while avoiding the need for an excessive amount of predefined variant categories. Because this approach directly relies on the hyperintensional model of catvars discussed above, these properties function as constraints on set membership in the catvar. It is in this context that we came to call this a constraint model of catvars. Simultaneously, the term constraint model alludes to the fact that matching in such a system is a form of constraint-satisfaction problem.

**Citations:**

*  `2024-06-18 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.x1ipvuxknxqe>`_

*  `2024-05-21 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.eh267uijjtqm>`_

*  `“A constraint-based model of CatVars” GitHub Discussion <https://github.com/ga4gh/cat-vrs/discussions/22>`_

*  `“Constraint name consistency” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/66>`_

*  `Cat-VRS Model: Categorical Variant <https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html>`_



.. medium_impact

Medium Impact
#############


.. constraint_array_of_anded_elements

Constraints as an Array of implicitly ANDed elements
====================================================

**Decision:**
The group decided that the individual *constraints* in the array of the constraints property are to be treated as implicitly ANDed together, and that no other boolean relations should be used in the context of the *CategoricalVariant* data class.

**Rationale:**
One property of the base *CategoricalVariant* class in the constraint model is constraints, an array of constraints. It is understood that in cases of singular or simplex catvar (i.e. excluding cases analogous to molecular profiles, such as “*MET* Amplification and *TP53* Loss”), the constraints are meant to denote set intersection. For example, the catvar “*MET* Amplification” requires members to satisfy two constraints: (1) a member variant must pertain to the *MET* gene, and (2) a member variant must entail copy-number gain. Importantly, either of those constraints individually can also define a catvar. The set of *MET* gene variants is a catvar, and so is the set of copy-number gain variants. The set of *MET* Amplification variants is equal to the set intersection of these two more general (and dimensionally orthogonal) sets. This is recognized to be a general trend in simplex catvars, and so the schema was designed to enforce this relation between constraints within a simplex catvar.

**Citations:**

*  `2024-11-06 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.6uib69olrqg5>`_

*  `"Categorical variants with Boolean operators” GitHub Discussion <https://github.com/ga4gh/cat-vrs/issues/92>`_



.. including_recipes

Including Recipes in the Cat-VRS Specification
==============================================

**Decision:**
The group decided to include recipes in Cat-VRS which illustrate representation of genomic variant types under the constraint model.

**Rationale:**
It is intended that implementations of Cat-VRS will allow for variants to be searched by matching query terms to catvars in a knowledgebase on the basis of the inclusion or exclusions of constraints in a given catvar, and the information content of such constraints. For example, searching for *MET* Amplification variants by matching against a query containing both a *FeatureContext* pointing to the *MET* gene, and a *CopyCountConstraint* indicating copy-number gain. A recipe is a template for such queries that represents classes of categorical variants of particular interest to Cat-VRS adopters and knowledgebase maintainers. For example, *CategoricalCNV*, the class of copy-number catvars. The *CategoricalCNV* recipe requires member catvars to satisfy the DefiningLocationConstraint and one of the copy number constraints, the *CopyCountConstraint* (change in the absolute copy number) or the *CopyChangeConstraint* (change in the number of copies relative to a baseline value). Thus, the categorical variant *MET* Amplification described above satisfies the *CategoricalCNV* recipe.


**Citations:**

*  `2024-11-06 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.6uib69olrqg5>`_

*  `CatVRS Data Model: Recipes <https://cat-vrs.readthedocs.io/en/latest/concepts/recipes.html>`_


.. machine_readable_spec

Machine Readable Specifications
===============================

**Decision:**
The group decided to adopt several repository and organizational conventions to ensure a single source of truth during development and ensure that the schema is readily computable:

*  The machine readable Cat-VRS is written using JSON Schema.
*  The schema itself is written in YAML and converted to individual JSON files for each class in the schema.
*  Contributions to the schema MUST be written in the YAML document.


**Rationale:**
These decisions bring Cat-VRS development in line with accepted best practices in the Genomic Knowledge Standards (GKS) work stream.

**Citations:**

*  `2023-11-22 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.s3afo1i22mnl>`_

*  `2023-10-25 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.8xxp7lqoun48>`_


.. separating_copycount_and_copychange

Separating CopyNumberConstraint into CopyCountConstraint and CopyChangeConstraint
=================================================================================

**Decision:**
The original model had a single copy number constraint, which was later split into two distinct constraints: the *CopyCountConstraint* (absolute copy numbers) and *CopyChangeConstraint* (relative changes such as amplifications and deletions).

**Rationale:**
Separating these two constraints ensures greater precision in representing categorical copy number variation. The *CopyCountConstraint* focuses on absolute values (e.g., "6 copies"), while the *CopyChangeConstraint* captures relative changes (e.g., "3-fold copy gain"). This prevents ambiguity when modeling CNVs in clinical databases like ClinVar, and prevents the quantity of an absolute copy count being misparsed as a relative x-fold copy change, and vice versa.

**Citations:**

*  `“Update the CopyConstraint to reflect model updates” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/67>`_

*  `“Dialing in CNV classes for next Trial-Use release” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/88>`_

*  `2024-11-19 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.hd9lu8gw3jh9>`_

*  `2024-11-06 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.6uib69olrqg5>`_


.. separating_definingallele_and_defininglocation

Separating DefiningContextConstraint into DefiningAlelleConstraint and DefiningLocationConstraint
=================================================================================================

**Decision:**
The group decided to split up the single combined *DefiningContextConstraint* into a *DefiningAlleleConstraint* and separate *DefiningLocationConstraint*.

**Rationale:**
This decision was driven by three primary considerations: (1) the need for greater precision in variant representation, (2) improved flexibility for structural variant and copy number variation representation, and (3) compatibility with existing genomic standards.

#. **Greater precision in variant representation:** The original *DefiningContextConstraint* did not differentiate between allele and location attributes, which made it difficult to distinguish if a categorical variant was defined by its location-state (allele) or just by its coordinates (location).

#. **Improved flexibility for structural variant and copy number variation representation:** Many structural variants do not have a clear allele-level definition. Instead, they may be defined by their genomic location, sequence change, or a combination of the two.

#. **Compatibility with existing genomic standards:** Existing GKS standards like VRS and knowledgebases like ClinVar treat sequence (location-state) variants and location variants separately. A single *DefiningContextConstraint* was somewhat misaligned with these models, making interoperability more challenging.

Splitting this constraint allows the model to explicitly define variants based on location, sequence, or both while allowing for smoother integration across implementations by mirroring representation in other well established resources.

**Citations:**

*  `2024-11-19 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.hd9lu8gw3jh9>`_, this was primarily discussed in person during a pre-conference hackathon before ASHG

.. using_gks_maturity_model

Utilization of semantic versioning and the GKS maturity model
=============================================================

**Decision:**
The group decided to adopt standard semantic versioning practices and to indicate data class maturity in compliance with the :ref:`maturity-model`.

**Rationale:**

These decisions bring Cat-VRS in compliance with generally accepted best practices in the GKS workstream and improve transparency.

**Citations:**

*  `2023-10-25 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.8xxp7lqoun48>`_

*  `2023-10-11 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.cmwm638mk3jb>`_

.. generalizing_genecontextconstraint

Generalization of GeneContextConstriant into FeatureContextConstraint
=====================================================================

**Decision:**
The specification originally proposed a *GeneContextConstraint* to capture variation knowledge tied to a specific gene, but this constraint was later broadened into a *FeatureContextConstraint* to include regulatory elements, pseudogenes, and other sequence-related features.

**Rationale:**

This change was necessary to generalize the model and improve modularity, ensuring that Cat-VRS supports diverse genomic elements beyond strictly defined genes. It also aligns better with other genomic standardization efforts and accommodates structural variants that do not map directly to specific genes​; for example, protein contexts such as “Estrogen Receptor (ER)”. Furthermore, FeatureContext better allows for catvar harmonization across different gene name-space conventions, as these change over time and between organizations. For example, in an older refseq version, *DUXL4* was considered as pseudogene, but in the current refseq version it is not recognized as a gene (or pseudogene) at all.


**Citations:**

*  `“Shouldn’t CategoricalCnv be based on a CanonicalLocation vs a Contextual Location?” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/11>`_
*  `“Adding FeatureContextConstraint” GitHub issue <https://github.com/ga4gh/cat-vrs/issues/98>`_
*  `“Handling Function Variants” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/14>`_
*  `2025-01-21 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.f3vr43fppyez>`_
*  `2024-12-17 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.bwcukl5umkkw>`_




.. minor_impact

Minor Impact
############


.. relations_and_mappings

Distinction between Relations and Mappings
==========================================

**Decision:**
Relations refer to structured transformations to the underlying variant, such as translating a transcript sequence into an amino acid sequence. Mappings refer to homomorphisms of coded variant concepts between different codings systems and ontologies, for example, mapping the property of protein gain-of-function EFO code to that of a protein hypermorphism in SO.


**Rationale:**

The group followed existing practices in other GKS standards for relations and mappings adapted to the problem domain of catvar and catvar properties.

**Citations:**

*  `"Should 'relations' be a mappable concept?" GitHub issue <https://github.com/ga4gh/cat-vrs/issues/97>`_

*  `2025-02-04 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.ujjbabr6rnl>`_

*  GKS Core: `ConceptMapping <https://cat-vrs.readthedocs.io/en/latest/concepts/imported/ConceptMapping.html#conceptmapping>`_ and `MappableConcept <https://cat-vrs.readthedocs.io/en/latest/concepts/imported/MappableConcept.html#mappableconcept>`_


.. members_are_non-exhaustive

Inclusion of Members as non-exhaustive array of contextual variants
===================================================================

**Decision:**
Items in the *members* property constitute representative examples of GA4GH Variation Representation Specification (VRS) Variations that satisfy the constraints of a given categorical variant. It is neither required nor expected for *members* to contain an exhaustive list of representative VRS variants.


**Rationale:**

Because catvars are `defined by their properties (constraints), <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.8tp6mx3oau6h>`_ matching is performed by matching constraints between categorical variants. Thus, listing variants that satisfy the constraints defining a given categorical variant do not impact matching, and instead only serve as representative examples and to aid in human readability. As a result of these considerations, *members* is not a required property of the *CategoricalVariant* data class, and when included, the array of *members* is not to be understood as an exhaustive array of all member variants, even though, in some cases, it may incidentally feasible to exhaustively list all member variants. For example, the *members* property for the categorical variant “*BRAF* p.V600K” should list VRS Variations that correspond to the nucleotide changes that result in this amino acid substitution.

**Citations:**

*  `2024-07-03 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.8tp6mx3oau6h>`_

*  `2024-04-16 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.cexaqt7e0bcy>`_

*  `Cat-VRS Model: Categorical Variant class <https://cat-vrs.readthedocs.io/en/latest/concepts/catvrs_model.html#categorical-variant>`_


.. name_as_a_non-required_field

Name as a non-required field
============================

**Decision:**
The *name* property in the *CategoricalVariant* class is an optional (but not required) field for *CategoricalVariant*.


**Rationale:**
The *name* property is a string field, and is intended to hold a *name* for a categorical variant, often for the benefit of human readability. This field is not required, however, because it is not involved in catvar matching, and will probably be eschewed altogether in programmatic workflows involving Cat-VRS, as it serves no major computational function.



.. profiles_to_recipes

Renaming “Profiles” to “Recipes” to represent standard categorical variants templates
=====================================================================================

**Decision:**
:ref:`recipes` were originally called Profiles, but the group decided to change the name to the current Recipes.


**Rationale:**
The term `profile is already used within the Variant Annotation Specification (VA-spec), <https://va-ga4gh.readthedocs.io/en/latest/va-standard-profiles/>`_ and means something very different from what we intended it to mean in the context of Cat-VRS, so the term was changed in Cat-VRS to avoid confusion.


**Citations:**

*  `“Turn ‘profiles’ into ‘recipes’” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/60>`_



.. function_variants_mullers_morphs

Handling of Function Variants using Müller's Morphs
===================================================

**Decision:**
The classification of functional impact on protein structure in the FunctionConstraint was standardized using terms like hypermorphic, amorphic, neomorphic, and antimorphic (based on `Müller’s morphs <https://en.wikipedia.org/wiki/Muller%27s_morphs>`_), rather than terms like "gain-of-function" or "loss-of-function".


**Rationale:**
This approach provides a more structured, ontology code-backed classification. Additionally, it reserves the use of the variant descriptive keywords “gain” and “loss” solely for the context of copy number gain and copy number loss, avoiding ambiguity in the language surrounding categorical function variants.

We recognize that this terminology is inconsistent with current colloquial use of gain-of-function and loss-of-function descriptors. `A Discussion <https://github.com/ga4gh/cat-vrs/discussions/54>`_ was created on the Cat-VRS GitHub repository on October 6th, 2024 to promote discussion around this design decision. This decision will further be interrogated when this constraint is nominated to Trial Use as part of a GKS review ballot.

**Citations:**

*  `"Terminology for function changes" GitHub Discussion <https://github.com/ga4gh/cat-vrs/discussions/23>`_
*  `“Function Variants in the Constraint Model” GitHub Discussion <https://github.com/ga4gh/cat-vrs/discussions/54>`_
*  `2024-08-27 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.6pa182hdgx2a>`_
*  `2024-07-03 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.8tp6mx3oau6h>`_
*  `“Handling Function Variants” GitHub Issue <https://github.com/ga4gh/cat-vrs/issues/14>`_
*  `“Generalizing Canonical allele and Categorical CNV to handle function / expression variants” GitHub Issue <https://github.com/ga4gh/cat-vrs/discussions/16>`_

.. mappable_concepts_for_relations

Integration of Mappable Concepts for Variant Relations
======================================================

**Decision:**
For the relations property in the DefiningAlleleConstraint and DefiningLocationConstraint, the group decided to remove the explicit enum of possible relation methods (such as translates_to and translates_from) and instead refer to the :ref:`MappableConcept` data class.

**Rationale:**
This decision was made for a number of reasons: First, it is more consistent with `DRY <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_ best practices to have a single mechanism to handle relations rather than repeating lists of them multiple times throughout the specification. Second, the *gks.core:MappableConcept* class is a general-purpose data structure that holds codings of a concept and maps them to codings within other systems within a standardized way. Therefore, regardless of which coded methods are used by an implementation to relate one version of a variant to another, containerizing these coded methods in the *gks.core:MappableConcept* should make them easier to map to other coding systems.

**Citations:**

*  `“Should relation or relations be renamed?” GitHub discussion <https://github.com/ga4gh/cat-vrs/discussions/100>`_
*  `2025-02-05 meeting minutes <https://docs.google.com/document/d/1oI4ir4OzXFvhZNbMVEX-RHGAQ-d2K4lAKP-7lf-uzPc/edit?tab=t.0#heading=h.ujjbabr6rnl>`_

.. Error_Handling

Error handling is intentionally unspecified and delegated to implementation.
============================================================================

Cat-VRS provides foundational data types that enable significant flexibility.  Except where required by this specification, implementations may choose whether and how to validate data.  For example, implementations MAY choose to validate that particular combinations of objects are compatible, but such validation is not required.

.. Text_Case

Text casing
===========

**Cat-VRS uses** `PascalCase (a.k.a. CamelCaps) <https://simple.wikipedia.org/wiki/CamelCase>`__ **to represent compound words and** `snake_case <https://simple.wikipedia.org/wiki/Snake_case>`__ **to represent compound file names** Although the schema is currently JSON-based (which would typically use camelCase), Cat-VRS itself is intended to be neutral with respect to languages and database.

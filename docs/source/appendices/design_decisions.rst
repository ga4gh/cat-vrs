.. _design-decisions:

Cat-VRS Record of Design Decisions
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Cat-VRS contributors confronted numerous trade-offs in developing this specification. As these trade-offs may not be apparent to outside readers, this section highlights the most significant ones and the rationale for our design decisions, including the following.


Design decisions as they pertain to the `Categorical Variant Representation Specification (Cat-VRS)
<https://github.com/ga4gh/cat-vrs>`_ are categorized within this document by impact: how foundational they are to the specification. These categories are defined as follows:


* **Major impact**: Decisions that significantly alter the structure, functionality, or core principles of the product.
* **Medium impact**: Decisions that introduce moderate changes by affecting specific components or functionalities without altering the overall product.
* **Minor impact**: Decisions that involve minor tweaks or optimizations, with limited scope and minimal effect on the overall product.
* **General Principles**: Technical decisions and stylistic conventions that are observed in the Cat-VRS schema and documentation, but do not materially impact the design of the function of the standard.


Decisions are labeled based on their maturity status based on the `Genomic Knowledge Standards (GKS) Maturity Model
<https://cat-vrs.readthedocs.io/en/latest/appendices/maturity_model.html>`_. While the Maturity Model includes draft, trial use, normative, and deprecated categories, to date all components of this product are either draft or trial use status. Components must undergo a period of public comment before changing maturity status.

Because maturity is a function of (1) the breadth of model adoption and (2) expected stability, rather than a function of how fundamental a concept is to the model, the maturity status property is entirely orthogonal to the impact of a decision on Cat-VRS.


.. toctree::
   :maxdepth: 3
   :includehidden:

   major_impact
   medium_impact
   minor_impact
   general_principles





.. major_impact

Major Impact
############



.. medium_impact

Medium Impact
#############



.. minor_impact

Minor Impact
############



.. general_principles

General Principles
##################

**Machine Readable Specifications**
The machine readable Cat-VRS is written using `JSON Schema
<https://json-schema.org/>`_.

The schema itself is written in YAML (|catvrs_yaml|) and converted to individual JSON files for each class in the schema (|catvrs_json|).

Because the JSON and rst files are programatically generated from the "-source.yaml" files,  contributions to the schema MUST be written in the "-source.yaml" documents.


.. Error_Handling

**Error handling is intentionally unspecified and delegated to implementation.**
Cat-VRS provides foundational data types that enable significant flexibility.  Except where required by this specification, implementations may choose whether and how to validate data.  For example, implementations MAY choose to validate that particular combinations of objects are compatible, but such validation is not required.


.. Text_Case

**Cat-VRS uses** `PascalCase (a.k.a. CamelCaps) <https://simple.wikipedia.org/wiki/CamelCase>`__ **to represent compound words and** `snake_case <https://simple.wikipedia.org/wiki/Snake_case>`__ **to represent compound file names** Although the schema is currently JSON-based (which would typically use camelCase), Cat-VRS itself is intended to be neutral with respect to languages and database.

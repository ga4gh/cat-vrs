.. _CategoricalCnv:

Categorical CNV
!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CategoricalCnv.rst

A CategoricalCNV is a :ref:`CategoricalVariant` with exactly two constraints:

1. A :ref:`DefiningLocationConstraint` with the `.relations` array containing only a
   `liftover_to` code.
2. A :ref:`CopyChangeConstraint` or :ref:`CopyCountConstraint`.

Examples
@@@@@@@@

The following :ref:`example Categorical Variants <Examples>` satisfy this :ref:`Recipe <Recipes>`:

- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <CategoricalCnvEx1>`
  - This example utilizes the :ref:`Copy Count Constraint <CopyCountConstraint>`
- :ref:`GRCh38/hg38 7p22.1(chr7:5905831-6014161)x3 <CategoricalCnvEx2>`
  - This example utilizes the :ref:`Copy Change Constraint <CopyChangeConstraint>`
- :ref:`GRCh38 Xp22.31(chrX:6978350-7594949)x3 <CategoricalCnvEx3>`

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

Constraints
###########

Categorical Variants that are intended to represent Categorical Copy Number Variants must **only** contain two constraints. While the choice of using a :ref:`Copy Change Constraint <CopyChangeConstraint>` or :ref:`Copy Count Constraint <CopyCountConstraint>` will depend on the type of Copy Number Variant intended to be expressed, the :ref:`Defining Location Constraint <DefiningLocationConstraint>` is **required** to contain the following :ref:`coding <Coding>` as a *relations*:

.. list-table::
    :header-rows: 1
    :widths: 25 25 50

    * - Code
      - System
      - Rationale
    * - liftover_to
      - gks-gks-term:allele-relation
      - To specify that VRS objects that are listed as *members* may have a Sequence Location that is a liftover to another reference genome of the Defining ``Sequence Location``.

For the *matchCharacteristic* attribute of the Defining Location, we recommend using one of the following terms from the `Sequence Ontology <https://www.ebi.ac.uk/ols4/ontologies/so>`_ and the `Relations Ontology <https://www.ebi.ac.uk/ols4/ontologies/ro>`_, depending on the Defining Location is intended to be interpreted:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

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

.. include:: ../../_includes/_guidance_generate_sequence_location.rst

Members
#######

When modeling a Categorical Copy Number Variant, *members* may be populated with VRS :ref:`Copy Number Change <CopyNumberChange>` or :ref:`Copy Number Count <CopyNumberCount>` objects that satisfy:

- The :ref:`Sequence Location <SequenceLocation>` specified within the :ref:`Defining Location Constraint <DefiningLocationConstraint>`, and the associated *matchCharacteristic*.
- The *copyChange* or *copies* values specified within the :ref:`Copy Change <CopyChangeConstraint>` or :ref:`Copy Count <CopyCountConstraint>` Constraints, respectively.

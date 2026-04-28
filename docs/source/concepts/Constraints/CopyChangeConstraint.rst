.. _CopyChangeConstraint:

.. |indent| unicode:: U+00A0 U+00A0 U+00A0

Copy Change Constraint
!!!!!!!!!!!!!!!!!!!!!!

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include:: ../../def/cat-vrs/CopyChangeConstraint.rst

Examples
@@@@@@@@

The following are example implementations of Copy Change Constraint:

.. collapse:: Gain

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_categoricalCnv-ex2
      :language: json
      :lines: 43-46

.. collapse:: Loss

   .. literalinclude:: ../../../../schema/cat-vrs/json/example_tp53-copy-loss
      :language: json
      :lines: 99-102

Implementation Guidance
@@@@@@@@@@@@@@@@@@@@@@@

This Constraint is used when constructing a :ref:`Categorical Copy Number Variant <CategoricalCnv>` when a copy number variation is classified into a category. If looking to express the copy number variation as an integer or :ref:`Range`, consider instead applying the :ref:`Copy Count Constraint <CopyCountConstraint>`.

copyChange
##########

The *copyChange* attribute is required and uses a value set derived from the `Experimental Factor Ontology (EFO) <https://www.ebi.ac.uk/efo/>`_, with definitions reproduced from EFO. The EFO describes these categories hierarchically; subtypes are indicated by indentation in the table below. Broadly, a copy number amplification or gain should be represented using **gain** or one of its subtypes, and a copy number deletion or loss should be represented using **loss** or one of its subtypes. When the source data does not distinguish between subtypes, the parent term (for example, **loss**) should be preferred over a more specific subtype. Any of the following **Name** values can be used to populate this attribute:

.. list-table::
   :header-rows: 1
   :widths: 20 15 45 20

   * - Name
     - EFO ID
     - EFO Definition
     - EFO Name
   * - **gain**
     - `EFO:0030070 <http://www.ebi.ac.uk/efo/EFO_0030070>`_
     - Assessment of genomic copy number gain.
     - copy number gain
   * - |indent| **high-level gain**
     - `EFO:0030072 <http://www.ebi.ac.uk/efo/EFO_0030072>`_
     - Assessment of high-level genomic copy number gain.
     - high-level copy number gain
   * - |indent| **low-level gain**
     - `EFO:0030071 <http://www.ebi.ac.uk/efo/EFO_0030071>`_
     - Assessment of low-level genomic copy number gain.
     - low-level copy number gain
   * - **regional base ploidy**
     - `EFO:0030064 <http://www.ebi.ac.uk/efo/EFO_0030064>`_
     - Copy number assessment of regional base ploidy.
     - regional base ploidy
   * - **loss**
     - `EFO:0030067 <http://www.ebi.ac.uk/efo/EFO_0030067>`_
     - Assessment of genomic copy number loss.
     - copy number loss
   * - |indent| **low-level loss**
     - `EFO:0030068 <http://www.ebi.ac.uk/efo/EFO_0030068>`_
     - Assessment of low-level genomic copy number loss.
     - low-level copy number loss
   * - |indent| **high-level loss**
     - `EFO:0020073 <http://www.ebi.ac.uk/efo/EFO_0020073>`_
     - Assessment of high-level genomic copy number loss.
     - high-level copy number loss
   * - |indent| |indent| **complete genomic loss**
     - `EFO:0030069 <http://www.ebi.ac.uk/efo/EFO_0030069>`_
     - Assessment of complete genomic deletion.
     - complete genomic deletion

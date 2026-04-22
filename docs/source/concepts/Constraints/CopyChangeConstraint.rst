.. _CopyChangeConstraint:

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
The `copyChange` attribute uses a value set derived from the `Experimental Factor Ontology (EFO) <https://www.ebi.ac.uk/efo/>`_, with definitions reproduced from EFO. Any of the following **Name** values can be used to populate this attribute:

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
   * - **high-level gain**
     - `EFO:0030072 <http://www.ebi.ac.uk/efo/EFO_0030072>`_
     - Assessment of high-level genomic copy number gain.
     - high-level copy number gain
   * - **low-level gain**
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
   * - **low-level loss**
     - `EFO:0030068 <http://www.ebi.ac.uk/efo/EFO_0030068>`_
     - Assessment of low-level genomic copy number loss.
     - low-level copy number loss
   * - **high-level loss**
     - `EFO:0020073 <http://www.ebi.ac.uk/efo/EFO_0020073>`_
     - Assessment of high-level genomic copy number loss.
     - high-level copy number loss
   * - **complete genomic loss**
     - `EFO:0030069 <http://www.ebi.ac.uk/efo/EFO_0030069>`_
     - Assessment of complete genomic deletion.
     - complete genomic deletion

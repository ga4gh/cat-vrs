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
The `copyChange` attribute uses a value set derived from the the `Experimental Factor Ontology (EFO) <https://www.ebi.ac.uk/efo/>`_. Any of the following **bolded terms** can be used to populate this attribute:

* **gain** (`EFO:0030070 <http://www.ebi.ac.uk/efo/EFO_0030070>`_ - *copy number gain*): Assessment of genomic copy number gain.

    * **high-level gain** (`EFO:0030072 <http://www.ebi.ac.uk/efo/EFO_0030072>`_ - *high-level copy number gain*): Assessment of high-level genomic copy number gain.

    * **low-level gain** (`EFO:0030071 <http://www.ebi.ac.uk/efo/EFO_0030071>`_ - *low-level copy number gain*): Assessment of low-level genomic copy number gain.

* **regional base ploidy** (`EFO:0030064 <http://www.ebi.ac.uk/efo/EFO_0030064>`_ - *regional base ploidy*): Copy number assessment of regional base ploidy.

* **loss** (`EFO:0030067 <http://www.ebi.ac.uk/efo/EFO_0030067>`_ - *copy number loss*): Assessment of genomic copy number loss.

    * **low-level loss** (`EFO:0030068 <http://www.ebi.ac.uk/efo/EFO_0030068>`_ - *low-level copy number loss*): Assessment of low-level genomic copy number loss.

    * **high-level loss** (`EFO:0020073 <http://www.ebi.ac.uk/efo/EFO_0020073>`_ - *high-level copy number loss*): Assessment of high-level genomic copy number loss.

        * **complete genomic loss** (`EFO:0030069 <http://www.ebi.ac.uk/efo/EFO_0030069>`_ - *complete genomic deletion*): Assessment of complete genomic deletion.

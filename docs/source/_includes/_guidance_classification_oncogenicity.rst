The *classification* attribute is required and is a :ref:`MappableConcept`, meaning that it should be represented using a term from an externally defined terminology. We recommend setting the *conceptType* of this :ref:`MappableConcept` to ``Oncogenicity Classification`` and using one of the following terms, which correspond to the five-tier oncogenicity classifications of the `ClinGen/CGC/VICC Standard Operating Procedure <https://pubmed.ncbi.nlm.nih.gov/35101336/>`_. Where available, terms are drawn from the `NCI Thesaurus <https://evsexplore.semantics.cancer.gov/evsexplore/welcome?terminology=ncit>`_ :

.. list-table::
   :header-rows: 1
   :widths: 18 22 12 30 18

   * - Name
     - :ref:`Code <Coding>`
     - NCIt Definition
     - NCIt Preferred Name
   * - **Benign**
     - `C168802 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C168802>`_
     - A genetic variant that is known to not contribute to the development of a disease.
     - Variant Benign
   * - **Likely Benign**
     - `C168801 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C168801>`_
     - A genetic variant that is not expected to contribute to the development of a disease, but the scientific evidence may be insufficient to prove this conclusively.
     - Variant Likely Benign
   * - **Variant of Uncertain Significance**
     - `C94187 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C94187>`_
     - *No definition provided by NCIt.*
     - Variant of Unknown Significance
   * - **Likely Oncogenic**
     - *None*
     - *No corresponding NCIt term.*
     -
   * - **Oncogenic**
     - `C183322 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C183322>`_
     - Related to or causing tumor formation.
     - Oncogenic

The *name* of the :ref:`MappableConcept` should be set to the recommended name above (for example, ``Variant of Uncertain Significance``), with the alternative labels included as *aliases*. The *name* of the *primaryCoding* should be set to the NCIt preferred name.

.. note:: As of NCIt version 26.08e, the NCI Thesaurus does not contain terms for either **Likely Oncogenic Variant** or **Oncogenic Variant**. Until one is available, represent this classification as a :ref:`MappableConcept` with a *name* of and no *primaryCoding*. In the interim, we are recommending `C183322 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C183322>`_ (Oncogenic), but it is a general qualitative concept rather than a variant classification term.

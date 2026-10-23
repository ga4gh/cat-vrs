The *classification* attribute is required and is a :ref:`MappableConcept`, meaning that it should be represented using a term from an externally defined terminology. We recommend setting the *conceptType* of this :ref:`MappableConcept` to ``Pathogenicity Classification`` and using one of the following terms from the `NCI Thesaurus <https://evsexplore.semantics.cancer.gov/evsexplore/welcome?terminology=ncit>`_ , which correspond to the five-tier pathogenicity classifications of the `ACMG/AMP guidelines <https://pubmed.ncbi.nlm.nih.gov/25741868/>`_:

.. list-table::
   :header-rows: 1
   :widths: 18 14 46 22

   * - Name
     - :ref:`Code <Coding>`
     - NCIt Definition
     - NCIt Preferred Name
   * - **Pathogenic**
     - `C168799 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C168799>`_
     - A genetic variant that is known to directly contribute to the development of disease.
     - Pathogenic Variant
   * - **Likely Pathogenic**
     - `C168800 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C168800>`_
     - A genetic variant that is known to have a high likelihood (greater than 90% certainty) to contribute to the development of a disease.
     - Likely Pathogenic Variant
   * - **Variant of Uncertain Significance**
     - `C94187 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C94187>`_
     - A variation in a genetic sequence whose association with disease risk is unknown.
     - Variant of Unknown Significance
   * - **Likely Benign**
     - `C168801 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C168801>`_
     - A genetic variant that is not expected to contribute to the development of a disease, but the scientific evidence may be insufficient to prove this conclusively.
     - Variant Likely Benign
   * - **Benign**
     - `C168802 <https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C168802>`_
     - A genetic variant that is known to not contribute to the development of a disease.
     - Variant Benign

The *name* of the :ref:`MappableConcept` should be set to the recommended name above (e.g., ``Variant of Uncertain Significance``), with the alternative labels included as *aliases*. The *name* of the *primaryCoding* should be set to the NCIt preferred name.

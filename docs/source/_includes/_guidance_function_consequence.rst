The *functionConsequence* attribute is required and is a :ref:`MappableConcept`, meaning that it should be
represented using a term from an externally defined ontology. We recommend using descendant terms of the `functional effect variant <https://www.ebi.ac.uk/ols4/ontologies/so/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0001536?lang=en>`_ concept in the `Sequence Ontology <https://www.ebi.ac.uk/ols4/ontologies/so>`_, such as:

.. list-table::
   :header-rows: 1
   :widths: 20 15 45 20

   * - Name
     - :ref:`Code <Coding>`
     - SO Definition
     - SO Name
   * - **dominant negative variant**
     - `SO:0002052 <https://www.ebi.ac.uk/ols4/ontologies/so/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0002052>`_
     - A variant where the mutated gene product adversely affects the other (wild type) gene product.
     - dominant_negative_variant
   * - **gain of function**
     - `SO:0002053 <https://www.ebi.ac.uk/ols4/ontologies/so/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0002053>`_
     - A sequence variant whereby new or enhanced function is conferred on the gene product.
     - gain_of_function_variant
   * - **loss of function**
     - `SO:0002054 <https://www.ebi.ac.uk/ols4/ontologies/so/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0002054>`_
     - A sequence variant whereby the gene product has diminished or abolished function.
     - loss_of_function_variant
   * - **loss of heterozygosity**
     - `SO:0001786 <https://www.ebi.ac.uk/ols4/ontologies/so/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0001786>`_
     - A functional variant whereby the sequence alteration causes a loss of function of one allele of a gene.
     - loss_of_heterozygosity
   * - **functionally normal**
     - `SO:0002219 <https://www.ebi.ac.uk/ols4/ontologies/so/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0002219>`_
     - A sequence variant in which the function of a gene product is retained with respect to a reference.
     - functionally_normal

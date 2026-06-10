The *matchCharacteristic* attribute is required within a Defining Location Constraint and is a :ref:`MappableConcept`, meaning that it should be represented using a term from an ontology. This attribute is used to describe how members' Sequence Location relates to the Defining Sequence Location, or how the Defining Sequence Location is intended to be interpreted.

.. note:: *matchCharacteristics* **are** definitional and thus do alter the scope of the Categorical Variant's definition. In other words, they do restrict or expand which variants satisfy the Categorical Variant's constraints.

We recommend using one of the following terms from the `Sequence Ontology <https://www.ebi.ac.uk/ols4/ontologies/so>`_ and the `Relations Ontology <https://www.ebi.ac.uk/ols4/ontologies/ro>`_:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Name
     - :ref:`Code <Coding>`
     - System
     - Rationale
   * - exact match
     - `skos:exactMatch <https://www.w3.org/TR/skos-reference/#mapping>`_
     - `https://www.w3.org/TR/skos-reference/ <https://www.w3.org/TR/skos-reference/>`_
     - Use when the ``member``'s ``Sequence Location`` exactly matches the Defining ``Sequence Location`` itself.
   * - part of
     - `RO:0000050 <https://www.ebi.ac.uk/ols4/ontologies/flopo/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000050?lang=en>`_
     - `https://oborel.github.io <https://oborel.github.io>`_
     - Use when the ``members``'s ``Sequence Location`` is entirely within the Defining ``Sequence Location``, a narrow match.
   * - has part
     - `RO:0000051 <https://www.ebi.ac.uk/ols4/ontologies/flopo/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000051?lang=en>`_
     - `https://oborel.github.io <https://oborel.github.io>`_
     - Use when the ``members``'s ``Sequence Location`` entirely contains the Defining ``Sequence Location``, a broad match.
   * - partially overlaps
     - `RO:0002151 <https://www.ebi.ac.uk/ols4/ontologies/flopo/properties/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0002151?lang=en>`_
     - `https://oborel.github.io <https://oborel.github.io>`_
     - Use when the ``members``'s ``Sequence Location`` partially overlaps with the Defining ``Sequence Location``, a broad match.

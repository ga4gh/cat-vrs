The *matchCharacteristic* attribute is required within a Defining Location Constraint and is a :ref:`MappableConcept`, meaning that it should be represented using a term from an ontology. This attribute describes how a member's Sequence Location must relate to the Defining Sequence Location in order to satisfy the constraint.

.. note:: *matchCharacteristics* **are** definitional and thus do alter the scope of the Categorical Variant's definition. In other words, they do restrict which variants satisfy the Categorical Variant's constraints.

.. include:: ../../_includes/_guidance_ga4gh_gks_term_warning.rst

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - :ref:`Coding <Coding>`
     - Rationale
   * - ga4gh-gks-term:location-match:is_within
     - Used when the ``member``'s ``Sequence Location`` is entirely within the Defining ``Sequence Location`` . A narrow match.

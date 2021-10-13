**Computational Definition**

The LocatedMolecularConsequenceRule class constructs objects which describe any variation that results in the *molecular_consequence* at the specified *location*.

**Information Model**

Some LocatedMolecularConsequenceRule attributes are inherited from :ref:`SimpleVariationRule`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - _id
      - string
      - 0..1
      - A GA4GH computed identifier.
   *  - type
      - string
      - 1..1
      - MUST be "LocatedMolecularConsequenceRule"
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the variation rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the variation rule expression.
   *  - location
      - `Location <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/Location>`_
      - 1..1
      - The location where the *molecular_consequence* is observed.
   *  - molecular_consequence
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_
      - 1..1
      - A sequence ontology term specifying the type of molecular consequence. The value SHOULD be a descendent term of `SO:0001537 (structural_variant) <http://www.sequenceontology.org/browser/current_release/term/SO:0001537>`_.
   *  - molecular_context
      - string
      - 1..1
      - The molecular context of the *location* value.

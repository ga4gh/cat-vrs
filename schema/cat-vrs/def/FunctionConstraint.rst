.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A classification of the effect on protein function that members of this categorical variant satisfy. # Alternatively, "A classification of the functional consequence that characterizes members of this categorical variant."

**Information Model**

Some FunctionConstraint attributes are inherited from :ref:`Constraint`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - type
      -
      - string
      - 1..1
      - MUST be "FunctionConstraint"
   *  - functionConsequence
      -
      - :ref:`MappableConcept`
      - 1..1
      - The functional consequence of members of this categorical variant, as defined by an external ontology. We recommend using one of the defined terms from `The Sequence Ontology <http://www.sequenceontology.org>`_. See Implementation Guidance for more details.
   *  - description
      -
      - string
      - 0..1
      - A free-text description of the function change.

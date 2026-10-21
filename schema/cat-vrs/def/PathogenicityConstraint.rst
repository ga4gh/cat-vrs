.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

A classification of the pathogenicity that characterizes members of this Categorical Variant.

**Information Model**

Some PathogenicityConstraint attributes are inherited from :ref:`Constraint`.

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
      - MUST be "PathogenicityConstraint"
   *  - classification
      -
      - :ref:`MappableConcept`
      - 1..1
      - The pathogenicity classification of members of this categorical variant, as defined by an external terminology. We recommend using one of the defined terms from the `NCI Thesaurus <https://evsexplore.semantics.cancer.gov/evsexplore/welcome?terminology=ncit>`_. See Implementation Guidance for more details.
   *  - description
      -
      - string
      - 0..1
      - A free-text description of the pathogenicity classification.

**Inherits:** :ref:`Constraint`

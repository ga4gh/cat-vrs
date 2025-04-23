.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

The unique name to identify and describe the variant when no more formal option is available. This is a `last resort` option to allow CategoricalVariants to be defined when no other computationally valid option exists.

**Information Model**

Some DescribedVariationConstraint attributes are inherited from :ref:`Constraint`.

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
      - MUST be "DescribedVariationConstraint"
   *  - name
      -
      - _Not Specified_
      - 1..1
      - A primary name for the categorical variation. This required property should provide a short and descriptive textual representation of the concept. This value may also be used as a display name for the categorical variation, but it is not a requirement.
   *  - description
      -
      - _Not Specified_
      - 0..1
      - A textual description of the domain of variation that should match the categorical variation entity.

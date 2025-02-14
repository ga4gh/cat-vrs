.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

The relative assessment of the change in copies that members of this categorical variant satisfies.

**Information Model**

Some CopyChangeConstraint attributes are inherited from :ref:`Constraint`.

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
      - MUST be "CopyChangeConstraint"
   *  - copyChange
      - 
      - string
      - 1..1
      - The relative assessment of the change in copies that members of this categorical variant satisfies.

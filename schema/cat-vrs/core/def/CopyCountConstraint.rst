**Computational Definition**

The absolute number of copies in a system

**Information Model**

Some CopyCountConstraint attributes are inherited from :ref:`Constraint`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Type
      - Limits
      - Description
   *  - type
      - string
      - 1..1
      - MUST be "CopyCountConstraint"
   *  - copies
      - integer | :ref:`Range`
      - 1..1
      - 

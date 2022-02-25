**Computational Definition**

A representation of a categorically-defined  `functional domain <https://en.wikipedia.org/wiki/Domain_of_a_function>`_  for variation, in which individual variation instances may be members.

**Information Model**

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
      - Categorical Variation Id. MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be Categorical Variation class name.
   *  - complement
      - boolean
      - 1..1
      - This field indicates that a categorical variation is defined to include (false) or exclude (true) variation concepts matching the categorical variation. This is  equivalent to a logical NOT operation on the categorical variation properties.

**Computational Definition**

The ComplexRule class constructs objects for defining complex logical relationships between two or more other :ref:`GenomicKnowledgeRule` objects.

**Information Model**

Some ComplexRule attributes are inherited from :ref:`GenomicKnowledgeRule`.

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
      - MUST be "ComplexRule".
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the genomic knowledge rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the genomic knowledge rule expression.
   *  - operands
      - :ref:`GenomicKnowledgeRule`
      - 2..m
      - The :ref:`GenomicKnowledgeRule` objects that are being evaluated collectively.
   *  - operator
      - string
      - 1..1
      - The logical operation applied to evaluating the object *operands*. MUST be "AND" or "OR".

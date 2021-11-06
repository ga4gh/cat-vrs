**Computational Definition**

The SimpleRule abstract class represents the set of :ref:`GenomicKnowledgeRule` classes that are used directly by genomic knowledge statements, or as components for defining a :ref:`ComplexRule`.

**Information Model**

Some SimpleRule attributes are inherited from :ref:`GenomicKnowledgeRule`.

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
      - MUST be Genomic Knowledge Rule class name.
   *  - complement
      - bool
      - 1..1
      - This field indicates whether the genomic knowledge rule is defined to include (false) or exclude (true) variation concepts matching the rule. This is equivalent to a logical NOT operation on the genomic knowledge rule expression.

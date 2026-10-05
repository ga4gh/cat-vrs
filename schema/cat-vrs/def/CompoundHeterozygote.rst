.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Composite Categorical Variant that joins exactly two elements with the AND operator and a trans phase relation, where each element represents one haplotype: either a present Categorical Variant Criterion, or a Composite Categorical Variant that joins two or more present Categorical Variant Criteria with the AND operator and a cis phase relation. The two elements MUST NOT represent the same haplotype.

**Information Model**


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

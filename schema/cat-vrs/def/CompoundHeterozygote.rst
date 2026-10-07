.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

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
   *  - id
      -
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - type
      -
      - string
      - 1..1
      - MUST be "CompositeCategoricalVariant"
   *  - name
      -
      - string
      - 1..1
      - A primary name for the entity.
   *  - description
      -
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - aliases
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - elements
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`CategoricalVariantCriterion` | :ref:`CompositeCategoricalVariant`
      - 2..2
      - The elements array must contain exactly two haplotypes, each of which is either a present Categorical Variant Criterion or a Composite Categorical Variant of two or more present Categorical Variant Criteria in cis.
   *  - operator
      -
      - string
      - 1..1
      - Operator used to join the included elements.
   *  - phaseRelation
      -
      - string
      - 1..1
      - The phase relationship asserted to hold among the present elements of this composite. Only meaningful when `operator` is `AND`, since phase describes a relationship among co-occurring (present) elements.
   *  - mappings
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`ConceptMapping`
      - 0..m
      - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.

**Composes:** :ref:`CompositeCategoricalVariant`

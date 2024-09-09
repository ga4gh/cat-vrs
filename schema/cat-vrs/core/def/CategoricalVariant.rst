**Computational Definition**

A representation of a categorically-defined domain for variation, in which individual contextual variation instances may be members of the domain.

**Information Model**

Some CategoricalVariant attributes are inherited from :ref:`gks.core-im:DomainEntity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - mappings
      - :ref:`ConceptMapping`
      - 0..m
      - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
   *  - type
      - string
      - 1..1
      - MUST be "CategoricalVariant"
   *  - members
      - :ref:`Variation` | :ref:`IRI`
      - 0..m
      - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
   *  - constraints
      - :ref:`Constraint`
      - 0..m
      - 

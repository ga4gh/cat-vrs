**Computational Definition**

Constraints are used to construct an intensional semantics of categorical variant types.

**Information Model**

Some Constraint attributes are inherited from :ref:`gks.core-im:DomainEntity`.

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
   *  - type
      - string
      - 1..1
      - The name of the class that is instantiated by a data object representing the Entity.
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
   *  - description
      - string
      - 0..1
      - A textual description of the domain of variation that should match the categorical  variation entity.
   *  - label
      - string
      - 0..1
      - A primary label for the categorical variation. This required property should provide a  short and descriptive textual representation of the concept.

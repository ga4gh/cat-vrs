**Computational Definition**

Constraints are used to construct and intensional semantics of categorical variant types.

    **Information Model**
    
Some Constraint attributes are inherited from :ref:`gks.core:Entity`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - extensions
          - `Extension <../vrs/../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - description
          - string
          - 0..1
          - A textual description of the domain of variation that should match the categorical  variation entity.
       *  - label
          - string
          - 1..1
          - A primary label for the categorical variation. This required property should provide a  short and descriptive textual representation of the concept.

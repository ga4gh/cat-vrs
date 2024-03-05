**Computational Definition**

A representation of a categorically-defined domain for variation, in which individual  contextual variation instances may be members of the domain.

    **Information Model**
    
Some CategoricalVariation attributes are inherited from :ref:`gks.core:DomainEntity`.

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
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <gks.common.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - mappings
          - `Mapping <gks.common.json#/$defs/Mapping>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - 
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate labels for a Domain Entity.
       *  - members
          - `Variation <vrs.json#/$defs/Variation>`_ | `IRI <gks.common.json#/$defs/IRI>`_
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.

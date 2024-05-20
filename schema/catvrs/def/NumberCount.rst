**Computational Definition**

The absolute count of a discrete assayable unit (e.g. chromosome, gene, or sequence).

    **Information Model**
    
Some NumberCount attributes are inherited from :ref:`CategoricalVariation`.

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
          - `Extension <../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - mappings
          - `Mapping <../gks-common/core.json#/$defs/Mapping>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - MUST be "NumberCount"
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate labels for a Domain Entity.
       *  - members
          - `Variation <../vrs/vrs.yaml#/$defs/Variation>`_ | `IRI <../gks-common/core.yaml#/$defs/IRI>`_
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
       *  - constraints
          - :ref:`Constraint`
          - 0..m
          - 
       *  - count
          - integer | `Range <../vrs/vrs.yaml#/$defs/Range>`_
          - 1..1
          - The integral quantity or quantity range of the subject in a system

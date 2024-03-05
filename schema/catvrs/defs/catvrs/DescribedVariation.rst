**Computational Definition**

Some categorical variation concepts are supported by custom nomenclatures or text-descriptive representations for which a categorical variation model does not exist. DescribedVariation is a class that adds requirements and contextual semantics to the `label` and `description` fields to indicate how a categorical variation concept should be evaluated for matching variants.

    **Information Model**
    
Some DescribedVariation attributes are inherited from :ref:`CategoricalVariation`.

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
          - MUST be "DescribedVariation"
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate labels for a Domain Entity.
       *  - members
          - `Variation <vrs.json#/$defs/Variation>`_ | `IRI <gks.common.json#/$defs/IRI>`_
          - 0..m
          - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
       *  - label
          - string
          - 1..1
          - A primary label for the categorical variation. This required property should provide a  short and descriptive textual representation of the concept.
       *  - description
          - string
          - 0..1
          - A textual description of the domain of variation that should match the categorical  variation entity.

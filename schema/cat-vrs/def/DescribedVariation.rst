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
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - mappings
      - `ConceptMapping </ga4gh/schema/gks-common/1.x/data-types/json/ConceptMapping>`_
      - 0..m
      - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
   *  - members
      - `Variation </ga4gh/schema/vrs/2.x/json/Variation>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..m
      - A non-exhaustive list of VRS variation contexts that satisfy the constraints of this categorical variant.
   *  - type
      - string
      - 1..1
      - MUST be "DescribedVariation"
   *  - label
      - string
      - 1..1
      - A primary label for the categorical variation. This required property should provide a  short and descriptive textual representation of the concept.
   *  - description
      - string
      - 0..1
      - A textual description of the domain of variation that should match the categorical  variation entity.

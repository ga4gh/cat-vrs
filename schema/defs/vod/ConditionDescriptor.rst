**Computational Definition**

This descriptor class is used for describing Condition entities.

**Information Model**

Some ConditionDescriptor attributes are inherited from :ref:`Entity`.

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
      - 1..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
   *  - type
      - string
      - 1..1
      - MUST be "ConditionDescriptor".
   *  - label
      - string
      - 0..1
      - A primary label for the value object.
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - description
      - string
      - 0..1
      - A free-text description of the value object.
   *  - xrefs
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..m
      - List of CURIEs representing associated concepts.
   *  - alternate_labels
      - string
      - 0..m
      - List of strings representing alternate labels for the value object.
   *  - condition
      - `Condition <core.json#/$defs/Condition>`_
      - 0..1
      - 
   *  - condition_id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - 
   *  - member_descriptors
      - :ref:`DiseaseDescriptor` | :ref:`PhenotypeDescriptor`
      - 0..m
      - 

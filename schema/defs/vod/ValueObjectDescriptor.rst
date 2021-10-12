**Computational Definition**

The abstract *Value Object Descriptor* parent class. All attributes of this parent class are inherited by child classes.

**Information Model**

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
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_
      - 1..1
      - Descriptor ID; MUST be unique within document.
   *  - type
      - string
      - 1..1
      - MUST be VOD class name.
   *  - label
      - string
      - 0..1
      - A primary label for the value object.
   *  - description
      - string
      - 0..1
      - A free-text description of the value object.
   *  - xrefs
      - `CURIE <https://raw.githubusercontent.com/ga4gh/vrs/1.2.0/schema/vrs.json#/definitions/CURIE>`_
      - 0..m
      - List of CURIEs representing associated concepts.
   *  - alternate_labels
      - string
      - 0..m
      - List of strings representing alternate labels for the value object.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - List of resource-specific :ref:`Extensions <Extension>` needed to describe the value object.

**Computational Definition**

The absolute count of a discrete assayable unit (e.g. chromosome, gene, or sequence).

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
       *  - type
          - string
          - 0..1
          - MUST be "NumberCount"
       *  - copies
          - integer | `Range <../vrs/vrs.yaml#/$defs/Range>`_
          - 1..1
          - The integral quantity of the subject in a system

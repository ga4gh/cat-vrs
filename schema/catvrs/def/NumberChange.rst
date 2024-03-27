**Computational Definition**

A quantitative assessment of a unit within a system (e.g. genome, cell, etc.) relative to a baseline quantity.

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
          - MUST be "NumberChange"
       *  - change
          - integer | `Range <../vrs/vrs.yaml#/$defs/Range>`_ | string
          - 0..1
          - 

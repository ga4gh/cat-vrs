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
          - a quantitative or qualitative value of the measurement with respect to a baseline (0).  If qualitative, must be one of "efo:0030069" (complete genomic loss), "efo:0020073" (high-level loss), "efo:0030068" (low-level loss), "efo:0030067" (loss), "efo:0030064" (regional base ploidy), "efo:0030070" (gain), "efo:0030071" (low-level gain), "efo:0030072" (high-level gain).

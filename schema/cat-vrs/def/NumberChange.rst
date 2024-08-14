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
      - integer | `Range </ga4gh/schema/vrs/2.x/json/Range>`_ | string
      - 0..1
      - a quantitative or qualitative value of the measurement with respect to a baseline (0).  If qualitative, must be one of "EFO:0030069" (complete genomic loss), "EFO:0020073" (high-level loss), "EFO:0030068" (low-level loss), "EFO:0030067" (loss), "EFO:0030064" (regional base ploidy), "EFO:0030070" (gain), "EFO:0030071" (low-level gain), "EFO:0030072" (high-level gain).

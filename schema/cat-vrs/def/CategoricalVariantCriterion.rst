.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An assertion that a Categorical Variant is required to be present or absent.

**Information Model**

Some CategoricalVariantCriterion attributes are inherited from :ref:`gks-core:Element`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - id
      -
      - string
      - 0..1
      - The 'logical' identifier of the data element in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - extensions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - type
      -
      - string
      - 1..1
      - MUST be "CategoricalVariantCriterion"
   *  - subject
      -
      - :ref:`CategoricalVariant`
      - 1..1
      - The subject Categorical Variant of this criterion.
   *  - presence
      -
      - string
      - 1..1
      - Whether the subject Categorical Variant is asserted to be present or absent.

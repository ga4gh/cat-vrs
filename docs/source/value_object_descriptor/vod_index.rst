Value Object Descriptor Specification
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

This draft specification, under development by Driver Projects of the
GKS Work Stream, specifies standard data classes for the exchange of common
information useful for the description of variation but superfluous to the
salient elements necessary for specifying a value object. We describe these
classes as Value Object Descriptors (VODs). The VOD specification introduced
here is version-controlled and extensible, and envisioned to seed a larger
collection of VODs used with other GA4GH standards beyond VRSATILE.

Use of VODs provides a convenience mechanism for passing labels that you
As an example, this means that a value object representing a genomic variant
in VRS can be conveniently passed alongside human identifiers (e.g. ClinVar
IDs), expressions (e.g. HGVS descriptions), and important contexts (e.g.
sequence type, gene, transcript) in a standard format. This additional
structure is necessary due to the nature of value objects and |vrs|.

The GA4GH Variation Representation Specification (|vrs|) is a terminology,
information model, and schema for the computational representation of
variation. VRS also describes useful conventions for the normalization of
variation forms for message passing between systems. Objects compliant
with VRS are value objects: data objects that are compared by structure and
value, in contrast to entities which are compared by registered identifiers.
For example, the variants represented by the *NM_004415.2:c.8472_8483del* and
*LRG_423t1:c.8472_8483del* HGVS_ descriptions are not found equivalent by
comparing these strings, but by comparing the structure of the reference
sequence and indicated change underlying the descriptors. Conversely, the
meaning of the variant (a specific deletion on a specific residue sequence)
is clear without reference to any external naming authority (in this example,
the NM and LRG sequence identifiers), and in fact the referenced entities
can only be retrieved through lookup on a sequence registry instead of
through inspection of the variant itself.

.. _value_object_descriptor:

Value Object Descriptor
@@@@@@@@@@@@@@@@@@@@@@@
The root class of all VODs is the abstract *Value Object Descriptor* class.
All attributes of this parent class are inherited by child classes.

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
      - CURIE_
      - 1..1
      - Descriptor ID; MUST be unique within document
   *  - type
      - string
      - 1..1
      - MUST be VOD class name
   *  - value_id
      - CURIE_
      - 0..1
      - This MUST be provided if `value` is omitted
   *  - value
      - <Value Object>
      - 0..1
      - This MUST be provided if `value_id` is omitted
   *  - label
      - string
      - 0..1
      - A primary label for the value object
   *  - description
      - string
      - 0..1
      - A free-text description of the value object
   *  - xrefs
      - CURIE_\[]
      - 0..*
      - List of CURIEs representing associated concepts
   *  - alternate_labels
      - string[]
      - 0..*
      - List of strings representing alternate labels for
        the value object
   *  - extensions
      - Extension_\[]
      - 0..*
      - List of resource-specific Extensions needed to
        describe the value object

All VODs in VRSATILE are designed to describe exactly one corresponding
class from the VRS standard, and this is explicitly represented
in the VOD type. The following classes from VRS 1.2 are supported by
VRSATILE VODs:

- `Molecular Variation <https://vrs.ga4gh.org/en/latest/terms_and_model.html#molecular-variation>`_
   - Allele (VA)
   - Haplotype (VH)
- `Systemic Variation <https://vrs.ga4gh.org/en/latest/terms_and_model.html#systemic-variation>`_
   - CopyNumber (CN)
- `Utility Variation <https://vrs.ga4gh.org/en/latest/terms_and_model.html#utility-variation>`_
   - Text (VT)
   - VariationSet (VS)
- `Location <https://vrs.ga4gh.org/en/latest/terms_and_model.html#location>`_
   - SequenceLocation (VSL)
   - ChromosomeLocation (VCL)
- `Sequence (SQ) <https://vrs.ga4gh.org/en/latest/terms_and_model.html#sequence>`_
- `Gene <https://vrs.ga4gh.org/en/latest/terms_and_model.html#gene>`_

.. include:: vrs_descriptors.rst

Other Data Classes
@@@@@@@@@@@@@@@@@@

Extension
#########

The Extension class provides VODs with a means to extend descriptions
with other attributes unique to a content provider. These extensions
are not expected to be natively understood under VRSATILE, but may be
used for pre-negotiated exchange of message attributes when needed.

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
      - 1..1
      - MUST be "Extension"
   *  - name
      - string
      - 1..1
      - A name for the Extension
   *  - value
      - any[]
      - 0..*
      - Any primitive or structured object

.. _expression:

Expression
##########

The Expression class is designed to enable descriptions based on a
specified nomenclature or syntax for representing an object. Common
examples of expressions for the description of molecular variation
include the HGVS and ISCN nomenclatures.

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
      - 1..1
      - MUST be "Expression"
   *  - syntax
      - CURIE_
      - 1..1
      - CURIE referencing the expression syntax
   *  - value
      - string
      - 1..1
      - The concept expression as a string
   *  - version
      - string
      - 0..1
      - An optional version of the expression syntax

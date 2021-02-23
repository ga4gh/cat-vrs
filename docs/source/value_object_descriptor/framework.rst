Value Object Descriptor Framework
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

This draft standard proposal, under development by Driver Projects of the
GKS Work Stream, specifies standard data classes for the exchange of common
information useful for the description of variation but superfluous to the
salient elements necessary for specifying a value object. We describe these
classes as Value Object Descriptors (VODs). The VOD framework introduced
here is version-controlled and extensible, and envisioned to seed a larger
collection of VODs used with other GA4GH standards beyond VRSATILE.

Use of VODs provides a convenience mechanism for passing labels that you
As an example, this means that a value object representing a genomic variant
in VRS can be conveniently passed alongside human identifiers (e.g. ClinVar
IDs), expressions (e.g. HGVS descriptions), and important contexts (e.g.
sequence type, gene, transcript) in a standard format. This additional
structure is necessary due to the nature of value objects and |vrs|.

The GA4GH Variation Representation Specification (|vrs|) is a terminology,
schema, and expressive framework for the computational representation of
variation, and contains useful conventions for the normalization of
variation forms for message passing between systems. Objects compliant
with VRS are value objects, which are compared by structure and value,
in contrast to entities which are compared by registered identifiers. For
example, the variants represented by the *NM_004415.2:c.8472_8483del* and
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



.. include:: variation_descriptor.rst

Other Data Classes
@@@@@@@@@@@@@@@@@@

Pizza
#####
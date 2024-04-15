Terminology & Information Model
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. information on the terminology and information model go here.  subsections include:


When biologists and clinical researchers define terms in order to describe phenomena and
observations, they rely on a background of human experience and
intelligence for interpretation. Definitions may be abstract, perhaps
correctly reflecting uncertainty of our understanding at the
time. Unfortunately, such terms are not readily translatable into an
unambiguous representation of knowledge.

As discussed in the :ref:'Introduction', categorical variation labels are homophonous, ambiguous, and vague, often all three simultanously.  This poses a great difficulty to the precise representation of categorical variation.  In contrast, **the computational representation of categorical variation concepts requires
translating precise categorical definitions into information models and
data structures that may be used in software.** This translation
should result in a representation of information that is consistent
with conventional variant ontologies and, ideally, be able to
accommodate future data as well. The resulting *computational
representation* of information should also be cognizant of
computational performance, the minimization of opportunities for
misunderstanding, and ease of manipulating and transforming data.

Accordingly, for each term we define below, we begin by describing the
term as used by the genetics and/or bioinformatics communities as
available. When a term has multiple such definitions, we
explicitly choose one of them for the purposes of computational
modeling. We then define the **computational definition** that
reformulates the community definition in terms of information content.
Finally, we translate each of these computational definitions into precise
specifications for the (**information model**). 

.. Terms are ordered
"bottom-up" so that definitions depend only on previously-defined terms.

.. note:: The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
          NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
          "OPTIONAL" in this document are to be interpreted as
          described in `RFC 2119`_.


Information Model Principles
@@@@@@@@@@@@@@@@@@@@@@@@@@@@

* **Cat-VRS objects are minimal** `value objects
  <https://en.wikipedia.org/wiki/Value_object>`_. Two objects are
  considered equal if and only if their respective attributes are
  equal.  As value objects, Cat-VRS objects are used as primitive types
  and MUST NOT be used as containers for related data, such as primary
  database accessions, representations in particular formats, or links
  to external data.  Instead, related data should be associated with
  VRS objects through identifiers.  See :ref:`computed-identifiers`.

* **Error handling is intentionally unspecified and delegated to
  implementation.**  VRS provides foundational data types that
  enable significant flexibility.  Except where required by this
  specification, implementations may choose whether and how to
  validate data.  For example, implementations MAY choose to validate
  that particular combinations of objects are compatible, but such
  validation is not required.

* **Cat-VRS uses** `snake_case
  <https://simple.wikipedia.org/wiki/Snake_case>`__ **to represent
  compound words.** Although the schema is currently JSON-based (which
  would typically use camelCase), Cat-VRS itself is intended to be neutral
  with respect to languages and database.

* **Optional attributes start with an underscore.** Optional
  attributes are not part of the value object.  Such attributes are
  not considered when evaluating equality or creating computed
  identifiers.
.. The ``_id`` attribute is available to identifiable
  objects, and MAY be used by an implementation to store the
  identifier for a Cat-VRS object.  If used, the stored ``_id`` element
  MUST be a `CURIE`_. If used for creating a :ref:`truncated-digest`
  for parent objects, the stored element must be a :ref:`GA4GH
  Computed Identifier <identify>`.  Implementations MUST ignore
  attributes beginning with an underscore and they SHOULD NOT transmit
  objects containing them.



Basic types
@@@@@@@@@@@

CHECK BACK SOON FOR UPDATES!
THIS SECTION WILL BE UPDATED WITH FEEDBACK OF TYPE-LOGICAL FRAGMENT.


Primitives
@@@@@@@@@@

CHECK BACK SOON FOR UPDATES!
THIS SECTION WILL BE UPDATED WITH FEEDBACK OF TYPE-LOGICAL FRAGMENT.



.. Deprecated and obsolete classes.

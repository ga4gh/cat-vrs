.. _LengthExpression:

Length Expression
!!!!!!!!!!!!!!!!!

.. admonition:: New in V2

    The `LengthExpression` class is new in VRS v2, and was designed as a means for
    handling unknown sequence content with known length.

A length expression is used to represent molecular sequences with known length
but unknown sequence content, typically as determined by molecular weight assays
(e.g. gel electrophoresis).

Definition and Information Model
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. note::
   This class is imported from VRS. Its full documentation can be found in the
   latest VRS specification at `vrs.ga4gh.org <https://vrs.ga4gh.org/en/latest/concepts/SequenceExpression/LengthExpression.html>`__.

.. include::  ../../def/cat-vrs/LengthExpression.rst

Example
@@@@@@@

.. code-block:: json

  {
    "type": "LengthExpression",
    "length": 20000
  }

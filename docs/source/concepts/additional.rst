.. _additionalDataTypes:

Additional Data Types
@@@@@@@@@@@@@@@@@@@@@

Below are the additional data types used by the Cat-VRS models.

.. _UnspecifiedElement:

UnspecifiedElement
##################

The UnspecifiedElement class is an available item to populate the `adjoinedElements` property within the :ref:`AdjacencyConstraint`. It is intended to represent both the `Multiple Possible Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ and `Unknown Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#unknown-gene-component>`_  from the VICC Gene Fusion Specification. It has been generalized to "UnspecifiedElement" to support other than genes.

.. include:: ../def/cat-vrs/UnspecifiedElement.rst

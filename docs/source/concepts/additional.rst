.. _additionalDataTypes:

Additional Data Types
@@@@@@@@@@@@@@@@@@@@@

Below are the additional data types used by the Cat-VRS models.

.. _FunctionalDomain:

FunctionalDomain
##################

The FunctionalDomain class is used to populate the `functionalDomains` property within the :ref:`AdjacencyConstraint`. It is intended to represent `Functional Domains <https://fusions.cancervariants.org/en/latest/information_model.html#categorical-elements>`_ from the VICC Gene Fusion Specification.

.. include:: ../def/cat-vrs/FunctionalDomain.rst

.. _UnspecifiedElement:

UnspecifiedElement
##################

The UnspecifiedElement class is an available item to populate the `adjoinedElements` property within the :ref:`AdjacencyConstraint`. It is intended to represent both the `Multiple Possible Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#multiple-possible-gene-component>`_ and `Unknown Gene Component <https://fusions.cancervariants.org/en/latest/nomenclature.html#unknown-gene-component>`_  from the VICC Gene Fusion Specification.

.. include:: ../def/cat-vrs/UnspecifiedElement.rst

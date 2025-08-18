.. _impl-guide:

Implementation Guide
!!!!!!!!!!!!!!!!!!!!

This section describes the data and algorithmic components that are REQUIRED for the implementation of Cat-VRS. This
page will be updated as work on the reference implementation proceeds.  Please check back later for more information!

* Read the :ref:`introduction` and :ref:`how-cat-vrs-works` to understand the specification.
* Review the :ref:`data-model` and associated examples. :ref:`CategoricalVariants <CategoricalVariant>` are constructed using :ref:`Constraints <constraint>`, and :ref:`recipes` are standard types of categorical variants.
* Validate your constructed :ref:`CategoricalVariants <CategoricalVariant>` using the Python reference implementation, `Cat-VRS-Python <https://github.com/ga4gh/cat-vrs-python>`_.

The `VICC Variation Normalizer <https://github.com/cancervariants/variation-normalization>`_, `VRS-Python <https://github.com/ga4gh/vrs-python>`_, and `SeqRepo <https://github.com/biocommons/biocommons.seqrepo>`_ are useful services for generating `VRS <https://vrs.ga4gh.org>`_ :ref:`Allele` and :ref:`Location` objects, both of which are required for implementing the :ref:`DefiningAlleleConstraint` and :ref:`DefiningLocationConstraint`.

.. image:: ../images/cat-vrs-transparent-bg.png
    :width: 50%
    :alt: An irresistably cute kittynaut beckoning you to enter the Cat-VRS.
    :align: center

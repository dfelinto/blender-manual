
************
Introduction
************

Eevee's materials system uses the same node based approach as :doc:`Cycles </render/materials/index>`.


Nodes Support
=============

Due to realtime constraints, not all Cycles features are available in Eevee.
See :doc:`/render/eevee/materials/nodes_support`.


Performance
===========

Performance is highly dependent on the number of BSDF nodes present in the node tree.

.. tip::

   Prefer using the Principled BSDF instead of multiple BSDF nodes because Eevee is optimized for it.

.. seealso:: :ref:`Limitations <eevee-limitations-materials>`.

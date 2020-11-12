
*****
Debug
*****

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Performance`

These settings are mainly useful to developers and can be accessed
by enabling the :doc:`Cycles Debug </editors/preferences/experimental>`.

OptiX Flags
   Native OptiX Curve Primitive
      Use OptiX curves API for hair instead of custom implementation.

Viewport BVH Type
   Dynamic BVH
      Objects can be transformed, added and deleted interactively, at the cost of slower renders.
   Static BVH
      Object modifications require a complete :term:`BVH` rebuild which reduces interactivity but renders faster.

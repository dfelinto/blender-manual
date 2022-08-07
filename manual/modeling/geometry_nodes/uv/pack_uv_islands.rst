.. index:: Geometry Nodes; Pack UV Islands
.. _bpy.types.GeometryNodeUVPackIslands:

********************
Pack UV Islands Node
********************


.. figure:: /images/node-types_GeometryUVPackIslands.png
   :align: right
   :alt: Pack UV Islands node.

The *Pack UV Islands Node* scales islands of a UV map and moves them so they fill the UV space as much as possible.


.. seealso::

   The :ref:`bpy.ops.uv.pack_islands` operator performs a similar operation in the UV editor.


Inputs
======

UV
   The UV map to modify.

Selection
   Faces to consider when packing islands.
   UVs that are part of any other face will not be affected.

Margin
   The distance to leave between UV islands.

Rotate
   Allow Rotating islands for best fit.


Properties
==========

This node has no properties.


Output
======

UV
   The modified UVs.

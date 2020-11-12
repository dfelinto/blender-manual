.. _bpy.types.CompositorNodeDiffMatte:

*******************
Difference Key Node
*******************

.. figure:: /images/compositing_node-types_CompositorNodeDiffMatte.png
   :align: right

   Difference Key Node.

This node produces a matte that isolates foreground content by comparing it with a reference background image.


Inputs
======

Image
   Contains foreground content against the background that is to be removed.
Image
   The reference background image.


Properties
==========

Tolerance
   Where pixels match the reference background to within the specified threshold, the matte is made transparent.
Falloff
   Increase to make nearby pixels partially transparent producing a smoother blend along the edges.


Outputs
=======

Image
   Image with its alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.

.. _bpy.types.CompositorNodeRotate:

***********
Rotate Node
***********

.. figure:: /images/compositing_node-types_CompositorNodeRotate.png
   :align: right

   Rotate Node.

This node rotates an image.


Inputs
======

Image
   Standard image input.
Degr
   Rotation angle in degree. Positive values rotate clockwise and negative ones counterclockwise.


Properties
==========

Filter
   Interpolation Methods.

   Nearest
      No interpolation, uses nearest neighboring pixel.
   Bilinear
      Simple interpolation between adjacent pixels.
   Bicubic
      Highest quality interpolation.


Outputs
=======

Image
   Standard image output.

.. _bpy.types.CompositorNodeTransform:

**************
Transform Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeTransform.png
   :align: right

   Transform Node.

This node combines the functionality of three other nodes: :doc:`Scale </compositing/types/distort/scale>`,
:doc:`translate </compositing/types/distort/translate>`,
and :doc:`rotate </compositing/types/distort/rotate>` nodes.


Inputs
======

Image
   Standard image input.
X, Y
   Used to move the input image horizontally and vertically.
Angle
   Used to rotate an image around its center.
   Positive values rotate counter-clockwise and negative ones clockwise.
Scale
   Used to resize the image. The scaling is relative, meaning a value of 0.5
   gives half the size and a value of 2.0 gives twice the size of the original image.


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

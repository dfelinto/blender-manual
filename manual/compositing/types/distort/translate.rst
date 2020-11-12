.. _bpy.types.CompositorNodeTranslate:

**************
Translate Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeTranslate.png
   :align: right

   Translate Node.

The Translate node moves an image.

Could also be used to add a 2D camera shake.


Inputs
======

Image
   Standard image input.
X, Y
   Used to move the input image horizontally and vertically.


Properties
==========

Relative
   Percentage translation values relative to the input image size.
Wrapping
   Repeat pixels on the other side when they extend over the image dimensions, making endless translating possible.

   None, X Axis, Y Axis, Both Axis


Outputs
=======

Image
   Standard image output.

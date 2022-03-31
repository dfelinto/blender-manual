.. _bpy.types.CompositorNodeColorMatte:

**************
Color Key Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeColorMatte.webp
   :align: right
   :alt: Color Key node.

The Color Key node creates a matte based on a specified color of the input image.


Inputs
======

Image
   Standard color input.


Properties
==========

Color
   The sliders represent threshold values.
   Higher values in this node's context mean a wider range of colors from
   the specified will be added to the matte.

   Hue, Saturation, Value


Outputs
=======

Image
   Image with its alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.

.. _bpy.types.CompositorNodePixelate:

*************
Pixelate Node
*************

.. figure:: /images/compositing_node-types_CompositorNodePixelate.png
   :align: right

   Pixelate Node.

Add this node in front of a :doc:`Scale node </compositing/types/distort/scale>`
to get a pixelated (non-smoothed) image from the resultant upscaled image.


Inputs
======

Color
   Standard image input.


Properties
==========

This node has no properties.


Outputs
=======

Color
   Standard image output.


Example
=======

Open an image you would like to pixelate using an Image node.
Add two Scale nodes between the input and output :menuselection:`Add --> Distort --> Scale`.
Change the values of X and Y to 0.2 in the first scale box and to 5 in the second.
The composited image will appear unchanged. Now add a Pixelate node between the two Scale nodes.
The result will be a pixelated image.

.. figure:: /images/compositing_types_filter_pixelate_example.png

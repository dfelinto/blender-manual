.. _bpy.types.CompositorNodePosterize:

*********
Posterize
*********

.. figure:: /images/compositing_node-types_CompositorNodePosterize.webp
   :align: right
   :alt: Posterize Node.

   Posterize Node.

The *Posterize Node* reduces the number of colors that compose the image
by converting portions of continuous gradation into abrupt changes from one color to another.
This node is useful for generating masks in particular for rotoscoping.


Inputs
======

Image
   Standard color input.
Steps
   The number of colors per channel;
   A value of 8 will result is :math:`3^8 = 512` total colors.


Properties
==========

This node has no properties.


Outputs
=======

Image
   Standard color output.

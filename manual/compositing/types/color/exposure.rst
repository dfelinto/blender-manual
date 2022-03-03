.. _bpy.types.CompositorNodeExposure:

*************
Exposure Node
*************

.. figure:: /images/compositing_node-types_CompositorNodeExposure.png
   :align: right
   :alt: Exposure Node.

The Exposure Node adjusts the perceived brightness of an image by a scalar value.
This node allows you to make areas of an image brighter or dimmer.

.. seealso::

   The exposure can also be adjusted in the scene :ref:`Color Management <render-post-color-management>`.


Inputs
======

Image
   Standard color input.
Exposure
   Scalar factor to adjust the exposure of the image.


Properties
==========

This node has no properties.


Outputs
=======

Image
   Standard color output.


Examples
========

In the example below, the Exposure node is used to increase the brightness of the window area using a mask.

.. figure:: /images/compositing_types_color_exposure_example.png

   Example of an Exposure node.

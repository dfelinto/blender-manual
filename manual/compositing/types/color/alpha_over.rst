.. _bpy.types.CompositorNodeAlphaOver:

***************
Alpha Over Node
***************

.. figure:: /images/compositing_node-types_CompositorNodeAlphaOver.png
   :align: right

   Alpha Over Node.

The *Alpha Over* node is used to layer images on top of one another.
Where the foreground image pixels have an alpha greater than 0, it will be overlaid over the background image.


Inputs
======

Factor
   Controls the transparency of the foreground image.
   A factor less than 1 will make the foreground more transparent.
Image
   Input for the *background* image.
Image
   Input for the *foreground* image.


Properties
==========

Convert Premultiplied
   Converts foreground image to :term:`Premultiplied Alpha` format.

   The *Alpha Over* node is designed to work with premultiplied alpha color format.
   Use this checkbox when you know that your image has :term:`Straight Alpha` color values,
   to perform the correct over operation. Result will still be premultiplied alpha.

Premultiply
   Mix between using :term:`Premultiplied Alpha` or :term:`Straight Alpha`.

   When set to 1, the foreground color values will be multiplied by alpha, i.e. premultiplied;
   this is equivalent to enabling *Convert Premultiplied*.
   When set to 0, color values does not change.

   If *Premultiply* is not zero, *Convert Premultiplied* will be ignored.

   .. note:: This is a legacy option.


Outputs
=======

Image
   Standard image output.


Examples
========

Overlay
-------

In the node tree below, *Color Ramp* node is used to add an alpha channel to the black-and-white swirl image.
Then *Alpha Over* node is used to overlay it on top of another image.

.. figure:: /images/compositing_types_converter_color-ramp_create-alpha-mask.png
   :width: 600px

   Assembling a composite image using Alpha Over.


Fade In
-------

In the next example, the *Factor* is used to make a "Fade In" effect.
This effect can be animated by adding a *Time* node to feed the *Factor* socket as shown below.
Over the course of 30 frames, the *Alpha Over* node outputs an image that
starts with the pure background image, and the title slowly appearing.

.. figure:: /images/compositing_types_color_alpha-over_example.png
   :width: 600px

   Animated fade in effect using Alpha Over.

Note the *Convert Premultiply* checkbox is enabled,
since as the foreground used a PNG image that has straight alpha.

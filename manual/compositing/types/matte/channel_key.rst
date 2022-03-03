.. _bpy.types.CompositorNodeChannelMatte:

****************
Channel Key Node
****************

.. figure:: /images/compositing_node-types_CompositorNodeChannelMatte.png
   :align: right
   :alt: Channel Key Node.

The *Channel Key* node determines background objects from foreground objects by
the difference in the selected channel's levels.

For example in YUV color space,
this is useful when compositing stock footage of explosions (very bright)
which are normally shot against a solid, dark background.


Inputs
======

Image
   Standard color input.


Properties
==========

Color Space
   This button selects what color space the channels will represent.

   RGB, HSV, YUV, YCbCr

Key Channel
   This button selects the channel, defined by the *Color Space*, to use to determine the matte.

Algorithm
   Method to calculate the difference between levels.

   :Max:
      Limit by the maximum of the other two channels other than the *Key Channel*.
   :Single:
      Limit by the maximum of the selected *Limiting Channel*.

      Limiting Channel
         The channel to use when computing the maximum, the options are defined by the *Color Space*.

High
   Determines the lowest values that are considered foreground.
   (Which is supposed to be -- relatively -- high values: from this value to 1.0.)

Low
   Determines the highest values that are considered to be background objects.
   (Which is supposed to be -- relatively -- low values: from 0.0 to this value.)

.. tip::

   It is possible to have a separation between the *High* and *Low* values to allow
   for a gradient of transparency between foreground and background objects.


Outputs
=======

Image
   Image with an alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.

.. _bpy.types.CompositorNodeColorCorrection:

*********************
Color Correction Node
*********************

.. figure:: /images/compositing_node-types_CompositorNodeColorCorrection.png

   Color Balance Node.

The Color Correction node can adjust the color of an image, separately in several tonal ranges
(highlights, midtones and shadows) and only affect the necessary RGB channels.


Properties
==========

Red, Green, Blue
   Specifies which RGB channels will be affected by the correction.


Correction Tools (Columns)
--------------------------

Saturation
   Adjusts the image's saturation.
Contrast
   Adjust image contrast.
Gamma
   Exponential gamma correction, affecting the midtones of the image. (Works like Power in the Color Balance node.)
Gain
   Multiplier, stronger influence on the highlights. (Works like Slope in the Color Balance node.)
Lift
   This value (can be negative) will be added (+), linear lightens or darkens the image.
   (Works like *Offset* in the Color Balance node.)


Tonal Ranges (Rows)
-------------------

Master
   These sliders affect the entire tonal range.
Highlights
   These sliders only affect the highlights.
Midtones
   These sliders only affect the midtones.
Shadows
   Affects the dark tones of an image often affecting the shadows.

Midtones Start, Midtones End
   Defines the start and the end of midtones range, i.e.
   values where the whole tonal range is divided into the highlights, midtones and shadows
   (there is also a smooth transition between the ranges of width 0.2 units).


Inputs
======

Image
   Standard image input.
Mask
   Controls the amount of influence the node exerts on the output image.


Outputs
=======

Color
   Standard image output.

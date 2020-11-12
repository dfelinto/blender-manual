.. _bpy.types.TransformSequence:

*********
Transform
*********

Transform is a swiss-army knife of image manipulation.
It moves, rotates, and scales the images within a strip.


Options
=======

Interpolation
   None
      No interpolation, uses nearest neighboring pixel.
   Bilinear
      Simple interpolation between adjacent pixels.
   Bicubic
      Highest quality interpolation.
Translation Unit
   Control whether the input values are in *Percent* or *Pixels*.
Position
   Moves the input along the X and Y axis.
Uniform Scale
   Scale the input evenly along the X and Y axis.
Scale
   Scale the image on the X and Y axis.
Rotation
   Rotates the input two-dimensionally along the Z axis.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_effects_transform_example.png

   Transform Effect.

.. _bpy.types.CompositorNodeDBlur:

*********************
Directional Blur Node
*********************

.. figure:: /images/compositing_node-types_CompositorNodeDBlur.png
   :align: right

   Directional Blur Node.

Blurs an image in a specified direction and magnitude. Can be used to fake motion blur.


Inputs
======

Image
   Standard image input.


Properties
==========

Iterations
   Controls how may times the image is duplicated to create the blur effect.
   Higher values give smoother results.
Wrap
   Wraps the image on the X and Y axis to fill in areas,
   that become transparent from the blur effect.
Center X, Y
   Sets the position where the blur center is.
   This makes a difference if the angle, spin, and/or zoom are used.

Distance
   How large the blur effect is.
Angle
   Image is blurred at this angle from the center.

Spin
   Rotates the image each iteration to create a spin effect, from the center point.
Zoom
   Scales the image each iteration, creating the effect of a zoom.


Outputs
=======

Image
   Standard image output.

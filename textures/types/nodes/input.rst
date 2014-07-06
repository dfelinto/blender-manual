
..    TODO/Review: {{review|text= elaborate, exampls?}} .


Input Nodes
***********

Input nodes provide input data for other nodes.


Time

----


.. figure:: /images/Doc26-textureNodes-time.jpg
   :width: 200px
   :figwidth: 200px

   Time node


The time node uses a frame range to output a value between 0 and 1.
By default the node output a linear transition from 0 to 1 from frame 1 to 250.
The shape of the curve can be manipulated to vary the output over time in different ways.


:kbd:`+`:Zoom in.
:kbd:`-`:Zoom out
:guilabel:`Tools`:

   :guilabel:`Reset View`
      Resets curve view
   :guilabel:`Vector Handle`
      Breaks tangent at curve handle, making a angle.
   :guilabel:`Auto Handle`
      Default smooth interpolation of curve segments
   :guilabel:`Extend Horizontal`
      Causes the curve to stay horizontal before the first point and after the last point.


.. figure:: /images/Doc26-textureNodes-time-extendHorizontal.jpg
   :width: 150px
   :figwidth: 150px

   Extend Horizontal


   :guilabel:`Extend Extrapolated`
      Causes the curve to extrapolate before the first point and after the last point, based on the shape of the curve.


.. figure:: /images/Doc26-textureNodes-time-extendExtrapolate.jpg
   :width: 150px
   :figwidth: 150px

   Extend Extrapolate


   :guilabel:`Reset Curve`
      Resets shape of curve to original linear shape.

:guilabel:`Clipping Options`:
   :guilabel:`Use Clipping`
      Forces curve points to stay between specified values.
   :guilabel:`Min X/Y and Max X/Y`
      Set the minimum and maximum bounds of the curve points.

:kbd:`x`:Delete curve points. The first and last points cannot be deleted.
:guilabel:`X and Y` The coordinates of the selected edit point.
:guilabel:`Sta`:Specify the start frame to use.
:guilabel:`End`:Specify the end frame to use.


Coordinates
===========

.. figure:: /images/Doc26-textureNodes-coordinate2.jpg

   Coordinates node


The Coordinates node outputs the geometry local coordinates,
relative to its bounding box as RGB colors:

- Red channel corresponds to X value.
- Green channel corresponds to Y value.
- Green channel corresponds to Z value.


Texture Node
============

.. figure:: /images/Doc26-textureNodes-texture.jpg

   Texture node


The texture node can be used to load a another node based or non-node based texture.

:guilabel:`Color 1 and Color 2`
   These can be used to remap a greyscale texture using two colors.


Image Node
==========

.. figure:: /images/Doc26-textureNodes-image.jpg

   Image node


The image node can be used to load an external image.

:guilabel:`Browse for image`
   Select an image that already exists in the scene.
:guilabel:`Datablock name`
   Set the name of the image datablock.
:kbd:`F`
   Save this image datablock, even if it has no users.
:guilabel:`Open image`
   Select image to use from file browser.
:guilabel:`Unlink datablock`
   Remove the image datablock from the node.

.. _bpy.types.CompositorNodeScale:

**********
Scale Node
**********

.. figure:: /images/compositing_node-types_CompositorNodeScale.png
   :align: right

   Scale Node.

This node scales the size of an image.


Inputs
======

Image
   Standard image input.
X, Y
   Scale in the axis directions, only available if *Space* is set to *Relative* or *Absolute*.


Properties
==========

Space
   Coordinate Space to scale relative to.

   Relative
      Percentage values relative to the dimensions of the image input.
   Absolute
      Size of an image by using absolute pixel values.
   Scene Size
      Sizes an image to the size of the final render resolution for the scene.
      For example, rendering a scene at the standard 1080p resolution but setting the render percentage at 50%,
      will produce a 1080p image with the scene scaled down 50% and leaving the rest of the image as alpha.
   Render Size
      Image dimensions set in the Render panel.

      Stretch, Fit, Crop
         Stretch distorts the image so that it fits into the render size.
         Fit scales the image until the bigger axis "fits" into the render size.
         Crop cuts the image so that it is the same aspect ratio as the render size.
      X, Y
         Offset factor for the final scaled image.


Outputs
=======

Image
   Standard image output.


Examples
========

For instance X: 0.5 and Y: 0.5 would produce an image which width and
height would be half of what they used to be.

Use this node to match image sizes.
Most nodes produce an image that is the same size as the image input into their top image socket.
To uniformly combine two images of different size,
the second image has to be scaled up to match the resolution of the first.

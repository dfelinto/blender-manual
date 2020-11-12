.. _bpy.types.CompositorNodeZcombine:

**************
Z Combine Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeZcombine.png
   :align: right

   Z Combine Node.

The Z Combine node combines two images based on their Z-depth maps.
It overlays the images using the provided Z values to
detect which parts of one image are in front of the other.


Inputs
======

Image
   The background image.
Z
   Z depth of the background image.
Image
   The foreground image.
Z
   Z depth of the foreground image.


Properties
==========

Use Alpha
   The chosen Image pixel alpha channel is also carried over.
   If a pixel is partially or totally transparent,
   the result of the Z Combine will also be partially transparent;
   in which case the background image will show through the foreground (chosen) pixel.
Anti-Alias Z
   Applies :term:`Anti-Aliasing` to avoid artifacts at sharp edges or areas with a high contrast.


Outputs
=======

Image
   If both Z values are equal, it will use the foreground image.
   Whichever Z value is less decides which image pixel is used.
   See :term:`Z-buffer`.
Z
   The combined Z depth, which allows to thread multiple Z-combines together.


Examples
========

.. figure:: /images/compositing_types_color_z-combine_example-1.png
   :width: 700px

   Choosing closest pixels.

In the example above, the render output from two scenes are mixed using the Z Combine node,
one from a sphere of size 1.3, and the other a cube of size 1.0.
The sphere and square are located at the same place. The cube is tipped forward,
so the corner in the center is closer to the camera than the sphere surface;
so Z Combine chooses to use the cube's pixels. But the sphere is slightly larger
(a size of 1.3 versus 1.0), so it does not fit totally inside the cube. At some point,
as the cube's sides recede back away from the camera, the sphere's sides are closer.
When this happens, Z Combine uses the sphere's pixels to form the resulting picture.

This node can be used to combine a foreground with a background matte painting.
Walt Disney pioneered the use of multi-plane mattes, where three or four partial mattes were
painted on glass and placed on the left and right at different Z positions; minimal camera
moves to the right created the illusion of depth as Bambi moved through the forest.

.. note:: Valid Input

   Z Input Sockets do not accept fixed values; they must get a vector set (see Map Value node).
   Image Input Sockets will not accept a color since they do not have UV coordinates.

.. figure:: /images/compositing_types_color_z-combine_example-2.png
   :width: 700px

   Mix and match images.

The Z Combine can be used to merge two images as well.
Using the Z values from the sphere and cube scenes above, but inputting different images,
yields the example to the right.

.. figure:: /images/compositing_types_color_z-combine_example-3.png
   :width: 700px

   Z Combine in action.

In this node setup a render scene is mixed with a flat image. In the side view of the scene,
the orange cube is 10 units away from the camera, and the blue ball is 20.
The 3D cursor is about 15 units away from the camera. The image is Z-in at a location of 15,
thus inserting it in between the cube and the ball.
The resulting image appears to have the cube on the green image.

.. note:: Invisible Man Effect

   If a foreground image with a higher Alpha than the background,
   is then mixed in the Z Combine with a slightly magnified background,
   the outline of the transparent area will distort the background,
   enough to make it look like seeing a part of the background through
   an invisible yet Fresnel-lens object.

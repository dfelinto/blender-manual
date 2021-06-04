.. _render-tab-dimensions:

**********
Dimensions
**********

.. figure:: /images/render_output_properties_dimensions_panel.png

   Dimensions panel.

Several render presets exist with common resolution and frame rates
for TVs and screens can be selected in the panel header.

.. _bpy.types.RenderSettings.resolution_x:
.. _bpy.types.RenderSettings.resolution_y:

Resolution X, Y
   The number of pixels horizontally and vertically in the image.

   .. _bpy.types.RenderSettings.resolution_percentage:

   Percentage
      Slider to reduce or increase the size of the rendered image relative to the X/Y values above.
      This is useful for small test renders that have the same proportions as the final image.

.. _bpy.types.RenderSettings.pixel_aspect_x:
.. _bpy.types.RenderSettings.pixel_aspect_y:

Aspect X, Y
   Older televisions may have non-square pixels,
   so this can be used to control the shape of the pixels along the respective axis.
   This will *pre-distort* the images which will look stretched on a computer screen,
   but which will display correctly on a TV set.
   It is important that you use the correct pixel aspect ratio when rendering to prevent re-scaling,
   resulting in lowered image quality.

.. _bpy.types.RenderSettings.use_border:

Render Region
   Renders just a portion of the view instead of the entire frame.
   See the :ref:`Render Region <editors-3dview-navigate-render-region>`
   documentation to see how to define the size of the render region.

   .. note::

      This disables the *Save Buffers* option in the Performance panel.

.. _bpy.types.RenderSettings.use_crop_to_border:

Crop to Render Region
   Crops the rendered image to the size of the render region,
   instead of rendering a transparent background around it.

.. _bpy.types.Scene.frame_start:
.. _bpy.types.Scene.frame_end:

Frame Start, End
   Set the *Start* and *End* frames for :doc:`Rendering Animations </render/output/animation>`.

.. _bpy.types.Scene.frame_step:

Step
   Controls the number of frames to advance by for each frame in the timeline.

.. _bpy.types.RenderSettings.fps:
.. _bpy.types.RenderSettings.fps_base:

Frame Rate
   The number of frames that are displayed per second, relevant for :doc:`Animation </render/output/animation>`.
   The menu gives several common frame rates, custom frame rates can be used by selecting *Custom*
   which gives access to the following properties:

   FPS
      The frame rate, expressed in frames per second.
   Base
      Some standards require more precise frame rate, for example NTSC.
      To get such precise frame rates it is possible to represent the frame rate as a fraction.
      The *Base* value is used as the fraction's denominator with the FPS being the numerator:
      :math:`\frac{FPS}{Base}`.


Time Remapping
==============

Use to remap the length of an animation.

.. _bpy.types.RenderSettings.frame_map_old:

Old
   The length in frames of the original animation.

.. _bpy.types.RenderSettings.frame_map_new:

New
   The length in frames the new animation will last.

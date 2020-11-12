
***************
Output Settings
***************

The first step in the rendering process is to determine and set the output settings.
This includes render size, frame rate, pixel aspect ratio, output location, and file type.


.. _bpy.types.RenderSettings.use_border:
.. _render-tab-dimensions:

Dimensions Panel
================

.. figure:: /images/render_output_settings_dimensions-panel.png

   Dimensions panel.

Several render presets exist with common resolution and frame rates
for TVs and screens can be selected in the panel header.

Resolution X, Y
   The number of pixels horizontally and vertically in the image.

   Percentage
      Slider to reduce or increase the size of the rendered image relative to the X/Y values above.
      This is useful for small test renders that have the same proportions as the final image.

Aspect X, Y
   Older televisions may have non-square pixels,
   so this can be used to control the shape of the pixels along the respective axis.
   This will *pre-distort* the images which will look stretched on a computer screen,
   but which will display correctly on a TV set.
   It is important that you use the correct pixel aspect ratio when rendering to prevent re-scaling,
   resulting in lowered image quality.

   See :doc:`Video Output </render/output/file_formats>` for details on pixel aspect ratio.

.. _render-output-dimensions-region:

Render Region
   Renders just a portion of the view instead of the entire frame.
   See the :ref:`Render Region <editors-3dview-navigate-render-region>`
   documentation to see how to define the size of the render region.

   .. note::

      This disables the *Save Buffers* option in the Performance panel.

Crop to Render Region
   Crops the rendered image to the size of the render region,
   instead of rendering a transparent background around it.

Frame Start, End
   Set the *Start* and *End* frames for :doc:`Rendering Animations </render/output/animation>`.

Step
   Controls the number of frames to advance by for each frame in the timeline.

Frame Rate
   For an :doc:`Animation </render/output/animation>`
   the frame rate is how many frames will be displayed per second.


Time Remapping
--------------

Use to remap the length of an animation.


.. _render-tab-output:
.. _bpy.types.RenderSettings.filepath:
.. _bpy.types.RenderSettings.use_overwrite:
.. _bpy.types.RenderSettings.use_placeholder:
.. _bpy.types.RenderSettings.use_file_extension:
.. _bpy.types.RenderSettings.use_render_cache:

Output Panel
============

.. figure:: /images/render_output_settings_panel.png

   Output panel.

This panel provides options for setting the location of rendered frames for animations,
and the quality of the saved images.

File Path
   Choose the location to save rendered frames.

   When rendering an animation,
   the frame number is appended at the end of the file name with four padded zeros (e.g. ``image0001.png``).
   You can set a custom padding size by adding the appropriate number of ``#`` anywhere in the file name
   (e.g. ``image_##_test.png`` translates to ``image_01_test.png``).

   This setting expands :ref:`files-blend-relative_paths`
   where a ``//`` prefix represents the directory of the current blend-file.

Saving
   File Extensions
      Adds the correct file extensions per file type to the output files.
   Cache Result
      Saves the rendered image and passes to a multi-layer EXR file in temporary location on your hard drive.
      This allows the Compositor to read these to improve the performance, especially for heavy compositing.

File Format
   Choose the file format to save to. Based on which format is used,
   other options such as channels, bit depth and compression level are available.

   For rendering out to images see: :ref:`saving images <bpy.types.ImageFormatSettings>`,
   for rendering to videos see :doc:`rendering to videos </render/output/file_formats>`.

Color Mode
   Choose the color format to save the image to.
   Note that *RGBA* will not be available for all image formats.

   BW, RGB, RGBA

Image Sequence
   Overwrite
      Overwrite existing files when rendering.
   Placeholders
      Create empty placeholder frames while rendering.

.. hint:: Primitive Render Farm

   An easy way to get multiple machines to share the rendering workload is to:

   - Set up a shared directory over a network file system.
   - Disable *Overwrite*, enable *Placeholders* in the Render *Output* panel.
   - Start as many machines as you wish rendering to that directory.


.. _render-output-postprocess:

Post Processing Panel
=====================

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Output --> Post Processing`

The Post Processing panel is used to control different options used to process your image after rendering.

.. figure:: /images/render_output_settings_post-processing-panel.png
   :align: right

   Post Processing panel.

Pipeline
   Sequencer
      Renders the output of the Video Sequence editor, instead of the view from the 3D scene's active camera.
      If the sequence contains scene strips, these will also be rendered as part of the pipeline.
      If *Compositing* is also enabled, the Scene strip will be the output of the Compositor.
   Compositing
      Renders the output from the compositing node setup,
      and then pumps all images through the Composite node tree,
      displaying the image fed to the Composite Output node.

Dither
   Dithering is a technique for blurring pixels to prevent banding that is seen in areas of
   gradients, where stair-stepping appears between colors.
   Banding artifacts are more noticeable when gradients are longer, or less steep.
   Dithering was developed for graphics with low bit depths,
   meaning they had a limited range of possible colors.

   Dithering works by taking pixel values and comparing them with a threshold and
   neighboring pixels then does calculations to generate the appropriate color.
   Dithering creates the perceived effect of a larger color palette by creating a sort of visual color mixing.
   For example, if you take a grid and distribute red and yellow pixels evenly across it,
   the image would appear to be orange.

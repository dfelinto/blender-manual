
**************
Image Settings
**************

Image Panel
===========

.. TODO2.8
   .. figure:: /images/editors_image_image-settings_movie-image-panel.png
      :align: right

      Image panel.

Image
   Data-block menu.

   New ``+``
      The *New Image* button opens a pop-up to configure a `Generated`_ image.


.. _bpy.types.Image.source:

Source
------

See about :doc:`/files/media/image_formats`.


Single Image
^^^^^^^^^^^^

Still image or a single frame.


.. _image-sequence:

Image Sequence
^^^^^^^^^^^^^^

Each frame is stored in a separate file. How to :ref:`image-formats-open-sequence`.
For options see `Movie`_ below.


Movie
^^^^^

Frames packed into a container.

Frames
   Sets the range of frames to use.

   Match Movie Length
      This button sets the movies *frames* to the length of the selected movie.

Start
   Global starting frame of the sequence, when the playback should start.
   This is a global setting which means it affects all clip users such as the Movie Clip editor itself,
   motion tracking constraints and Compositor nodes.
Offset
   Offsets the first frame of the clip. It adds an extra offset to the frame number when
   converting a scene frame to the frame number in the file name.
   This option does not affect tracking data or any other associated data.
Cyclic
   Start over and repeats after the last frame to create a continuous loop.
Auto Refresh
   Automatically refresh images on frame changes.
Deinterlace
   Removes fields in a video file. For example,
   if it is an analog video and it has even or odd interlacing fields.


.. _image-generated:

Generated
^^^^^^^^^

Image generated in Blender.

.. list-table::

   * - .. figure:: /images/editors_image_image-settings_generated-image-panel.png

          Image panel for Generated source.

     - .. figure:: /images/editors_image_image-settings_generated-new-image.png

          The New Image pop-up menu.

Width, Height
   The size of image in pixels.
Color
   Sets the fill color if creating a blank image.
Type
   :Blank: Creates a Blank image of a single specified color.
   :UV Grid: Creates a checkerboard pattern with a colored cross (+) in each square.
   :Color Grid:
      Creates a more complex colored grid with letters and numbers denoting locations in the grid.
      It could be used for testing how the UVs have been mapped and to reduce stretching or distortion.
32-bit Float
   Creates a 32-bit image. This is a larger file size,
   but holds much more color information than the standard 8-bit image.
   For close-ups and large gradients, it may be better to use a 32-bit image.
Tiled
   Creates an image with support for :doc:`/modeling/meshes/uv/workflows/udims`.
   This option creates the first ``1001`` tile; more tiles can be added later in the *UDIM Tiles* panel.


.. _editors-image-image-settings-common:

Common Options
--------------

.. _bpy.types.Image.filepath:

File
   Use for replacing or packing files.

   Pack
      Embed the resource into the current blend-file.
   Path
      Path to the linked file.
   Open
      Opens the :doc:`/editors/file_browser` to select a file from a drive.
   Reload
      Reloads the file. Useful when a file has been reworked in an external application.

.. _bpy.types.Image.is_multiview:

Use Multi-View
   See :doc:`Multi-View </render/output/properties/stereoscopy/index>`.

.. _bpy.types.ColorManagedInputColorspaceSettings.name:

Color Space
   The :term:`Color Space` the image file was saved in.
   Once loaded into Blender, the color will be treated as linear color.
   This option ensure the correct conversion to linear color is used.

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   Using the default config will list the following options:

   :sRGB: Standard RGB display space.
   :Linear: Linear 709 (full range). Blender native linear space.
   :Linear ACES: ACES linear space.
   :XYZ: Standard linear XYZ space.
   :Non-Color: Color space used for images which contains non-color data (e.g. normal maps).
   :Raw: Does not automatically convert to linear; same as Non-Color.
   :Filmic Log: Intermediate log color space of Filmic view transform.

.. _bpy.types.Image.alpha_mode:

Alpha
   Representation of the image's :term:`Alpha Channel`, to convert to and from when saving and loading the image.
   This option is only available if the input format support's encoding transparency.

   :Straight:
      Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha.
      Commonly used by image editing applications and file formats like PNG.
      This preserves colors in parts of the image with zero alpha.
   :Premultiplied:
      Store RGB channels with alpha multiplied in, also known as associated alpha.
      The natural format for renders and used by file formats like OpenEXR.
      This can represent purely emissive effects like fire correctly, unlike straight alpha.
   :Channel Packed:
      Different images are packed in the RGB and alpha channels, and they should not affect each other.
      Channel packing is commonly used by game engines to save memory.
   :None:
      Ignore alpha channel from the file and make image fully opaque.

.. _bpy.types.Image.use_half_precision:

Half Float Precision
   Load the image as having only a :term:`Bit Depth` of 16 bits per channel instead of 32 bits which saves memory.

.. _bpy.types.Image.use_view_as_render:

View as Render
   Applies :doc:`color transform </render/color_management>` when displaying this image on the screen.

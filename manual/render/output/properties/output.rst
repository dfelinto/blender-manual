.. _render-tab-output:

******
Output
******

.. figure:: /images/render_output_properties_output_panel.png

   Output panel.

This panel provides options for setting the location of rendered frames for animations,
and the quality of the saved images.

.. _bpy.types.RenderSettings.filepath:

File Path
   Choose the location to save rendered frames.

   When rendering an animation,
   the frame number is appended at the end of the file name with four padded zeros (e.g. ``image0001.png``).
   You can set a custom padding size by adding the appropriate number of ``#`` anywhere in the file name
   (e.g. ``image_##_test.png`` translates to ``image_01_test.png``).

   This setting expands :ref:`files-blend-relative_paths`
   where a ``//`` prefix represents the directory of the current blend-file.

Saving
   .. _bpy.types.RenderSettings.use_file_extension:

   File Extensions
      Adds the correct file extensions per file type to the output files.

   .. _bpy.types.RenderSettings.use_render_cache:

   Cache Result
      Saves the rendered image and passes to a multi-layer EXR file in temporary location on your hard drive.
      This allows the Compositor to read these to improve the performance, especially for heavy compositing.

.. _bpy.types.ImageFormatSettings.file_format:

File Format
   Choose the file format to save to. Based on which format is used,
   other options such as channels, bit depth and compression level are available.

   For rendering out to images see: :ref:`saving images <bpy.types.ImageFormatSettings>`,
   for rendering to videos see the `Encoding`_ panel.

.. _bpy.types.ImageFormatSettings.color_mode:

Color
   Choose the color format to save the image to.
   Note that *RGBA* will not be available for all image formats.

   BW, RGB, RGBA

Image Sequence
   .. _bpy.types.RenderSettings.use_overwrite:

   Overwrite
      Overwrite existing files when rendering.

   .. _bpy.types.RenderSettings.use_placeholder:

   Placeholders
      Create empty placeholder frames while rendering.

.. hint:: Primitive Render Farm

   An easy way to get multiple machines to share the rendering workload is to:

   - Set up a shared directory over a network file system.
   - Disable *Overwrite*, enable *Placeholders* in the Render *Output* panel.
   - Start as many machines as you wish rendering to that directory.


.. _render-output-video-encoding-panel:
.. _bpy.types.FFmpegSettings:

Encoding
========

.. reference::

   :Panel:     :menuselection:`Properties --> Output --> Encoding`

.. figure:: /images/render_output_properties_output_video-encoding-panel.png

   Encoding panel.

Here you choose which video container, codec, and compression settings you want to use.
With all of these compression choices, there is a trade-off between file size,
compatibility across platforms, and playback quality.
In the header, you can use the presets, which choose optimum settings for you for that type of output.

.. tip::

   When you view the :doc:`System Console </advanced/command_line/introduction>`,
   you can see some of the output of the encoding process.
   You will see even more output if you execute Blender as ``blender -d``.

Container
   Video container or file type. For a list of all available options, see
   :doc:`video formats </files/media/video_formats>`.

Autosplit Output
   If your video is huge and exceeds 2GiB, enable Autosplit Output.
   This will automatically split the output into multiple files after the first file is 2GiB in size.


Video
-----

Video Codec
   Chooses the method of compression and encoding.
   For a list of all available options see :doc:`video formats </files/media/video_formats>`.

.. note:: Standards

   Some containers and codecs are not compatible with each other,
   so if you are getting errors check that your container and codec are compatible.
   Like containers and codecs are sometimes not compatible with each other, some codecs
   do not work with arbitrary dimensions. So, try to stick with common dimensions
   or research the limitations of the codec you are trying to use.

Output Quality
   These are preset `Rate`_.
Encoding Speed
   Presets to change between a fast encode (bigger file size) and more compression (smaller file size).

Keyframe Interval
   The number of pictures per `Group of Pictures <https://en.wikipedia.org/wiki/Group_of_pictures>`__.
   Set to 0 for "intra_only", which disables `inter-frame <https://en.wikipedia.org/wiki/Inter-frame>`__ video.
   A higher number generally leads to a smaller file but needs a higher-powered device to replay it.
Max B-frames
   Enables the use of :term:`B‑frames <Frame Types>`.

   Interval
      The maximum number of :term:`B‑frames <Frame Types>` between non-B-frames.


Rate
^^^^

Bitrate
   Sets the average `bit rate <https://en.wikipedia.org/wiki/Bit_rate>`__ (quality),
   which is the count of binary digits per frame.
   See also: `FFmpeg -b:v <https://ffmpeg.org/ffmpeg.html#Description>`__.
Rate
   Video files can use what is called variable bit rate (VBR).
   This is used to give some segments of the video less compressing to frames that need more data
   and less to frames with less data. This can be controlled by the *Minimum* and *Maximum* values.
Buffer
   The `decoder bitstream buffer <https://en.wikipedia.org/wiki/Video_buffering_verifier>`__ size.

Mux Rate
   Maximum bit rate of the multiplexed stream.
   `Multiplexing <https://www.afterdawn.com/glossary/term.cfm/multiplexing>`__
   is the process of combining separate video and audio streams into a single file,
   similar to packing a video file and MP3 audio file in a zip-file.
Mux Packet Size
   Reduces data fragmentation or muxer overhead depending on the source.


.. _render-output-video-encoding-audio:
.. _bpy.types.FFmpegSettings.audio:

Audio
-----

These settings change how sound is exported while rendering.
To control how sound is played back from within Blender, see the audio settings
in the :ref:`Preferences <prefs-system-sound>`.

Audio Codec
   Audio format to use. For a list of all available options, see
   :doc:`video formats </files/media/video_formats>`.
Audio Channels
   Sets the audio channel count.
Sample Rate
   Sets the audio `sampling rate <https://en.wikipedia.org/wiki/Sampling_(signal_processing)#Sampling_rate>`__.
Bitrate
   For each codec, you can control the bit rate (quality) of the sound in the movie.
   Higher bit rates are bigger files that stream worse but sound better.
   Use powers of 2 for compatibility.
Volume
   Sets the output volume of the audio.


Tips
----

.. tip::

   The choice of video format depends on what you are planning to do.

   It's not recommended to render directly to a video format in the first instance.
   If a problem occurs while rendering, the file might become unplayable and you will
   have to re-render all frames from the beginning. If you first render out a set
   of static images such as the default PNG format or the higher-quality OpenEXR
   (which can retain HDR pixel data), you can combine them as
   an :doc:`Image Strip </video_editing/sequencer/strips/image>`
   in the Video Sequencer. This way, you can easily:

   - Restart the rendering from the place (the frame) where any problem occurred.
   - Try out different video encoding options in seconds,
     rather than minutes or hours as encoding is usually much faster than rendering the 3D scene.
   - Enjoy the rest of the features of the Video Sequencer, such as adding
     :doc:`Image Strips </video_editing/sequencer/strips/image>`
     from previous renders, audio, video clips, etc.

.. tip::

   You shouldn't post-process a lossy-compressed file as the compression artifacts may become visible.
   Lossy compression should be reserved as a final 'delivery format'.

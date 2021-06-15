.. _bpy.types.MovieSequence:

***********
Movie Strip
***********

To add a movie (with or without audio) select a movie file(s) in the File Browser
e.g. in the Audio-Video Interleaved format (``*.avi`` file).

.. note:: Clips can be Huge

   A three minute Quicktime ``.mov`` file can be 140MB.
   Loading it, even over a high-speed LAN can take some time.
   Do not assume your computer or Blender has locked up if nothing happens for awhile.


.. _bpy.ops.sequencer.movie_strip_add:

Add Movie Strip
===============

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Add --> Movie`

Relative Path
   Store the location of the image file relative to the blend-file.

Start Frame
   The :ref:`Start Frame <bpy.types.Sequence.frame_start>` to place the left handle of the strip.

Channel
   The :ref:`Channel <bpy.types.Sequence.channel>` to place the strip.

Replace Selection
   Replaces the currently selected strips with the new strip.

Fit Method
   Determines how images with an aspect ratio different than
   the :doc:`Scene's </render/output/properties/dimensions>` are scaled to
   fit inside the render area.

   :Scale to Fit:
      Adjusts the strips :ref:`Scale Transforms <bpy.types.SequenceTransform.scale>` so the visual contents of
      the strip to fit exactly within the project's :doc:`/render/output/properties/dimensions` while maintaining
      the original aspect ratio.

      This may mean that the transparent areas may be added
      along the content's border to fit the content in the rendered area.
   :Scale to Fill:
      Adjusts the strips :ref:`Scale Transforms <bpy.types.SequenceTransform.scale>`
      so the visual contents of the strip to span the project's :doc:`/render/output/properties/dimensions`
      while maintaining the original aspect ratio.

      This may mean that portions of the original image no longer fit the content inside the rendered area.
   :Stretch to Fill:
      Adjusts the strips :ref:`Scale Transforms <bpy.types.SequenceTransform.scale>` so the visual contents of
      the strip to fill the project's :doc:`/render/output/properties/dimensions`. Note,
      unlike the other two methods described above, *Stretch to Fill* does not maintaining the original aspect ratio.

      This may mean that the original image becomes distorted to fit the content inside the rendered area.

Set View Transform
   Automatically sets an appropriate :ref:`View Transform <bpy.types.ColorManagedViewSettings.view_transform>`
   based on the :term:`Color Space` of the imported media. In most cases, the *Standard* should be used;
   using the wrong transform could result in inaccurate colors or degraded rendering performance.

Sound
   Add a :doc:`Sound Strip </video_editing/sequencer/strips/sound>` that contains the movie's audio track.

Use Movie Frame Rate
   Sets the :ref:`Scene Frame Rate <bpy.types.RenderSettings.fps>` to the frame rate encoded in the movie file.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_movie-image_example.png

   Imported movie strip with audio track underneath.

In the strip itself, you can see strip name, path to source file, and strip length.

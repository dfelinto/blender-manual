.. _clip-editor-clip-display-label:

************
Clip Display
************

This pop-over contains display settings related to editor itself.

.. _bpy.types.SpaceClipEditor.show_red_channel:
.. _bpy.types.SpaceClipEditor.show_green_channel:
.. _bpy.types.SpaceClipEditor.show_blue_channel:

R, G, B
   Control the color channels used for frame preview.
   It is needed because the tracking algorithm works with grayscale images and it is not
   always obvious to see which channels disabled will increase contrast of feature points and reduce noise.

.. _bpy.types.SpaceClipEditor.use_grayscale_preview:

Grayscale Preview (B/W)
   Shows the whole frame gray-scale.

.. _bpy.types.SpaceClipEditor.use_mute_footage:

Mute (eye icon) :kbd:`M`
   Shows black frames in the preview instead of the movie clip.
   It helps to find tracks which are tracked inaccurately or which were not tracked at all.

.. _bpy.types.MovieClipUser.use_render_undistorted:

Render Undistorted
   Applies the *Lens Distortion* settings to the viewport image in order to display the footage undistorted.
   It is only a preview option, which does not actually change the footage itself.

.. _bpy.types.SpaceClipEditor.show_stable:

Show Stable
   This option makes the displayed frame be affected by the 2D stabilization settings
   (available in reconstruction mode only).
   It is only a preview option, which does not actually change the footage itself.

.. _bpy.types.SpaceClipEditor.show_grid:

Grid
   Displays a grid which is originally orthographic,
   but is affected by the distortion model (available in distortion mode only).
   This grid can be used for manual calibration --
   distorted lines of grids are equal to straight lines in the footage.

.. _bpy.types.SpaceClipEditor.use_manual_calibration:

Calibration
   Applies the distortion model for annotation strokes (available in distortion mode only).
   This option also helps to perform manual calibration.
   A more detailed description of this process will be added later.

.. _bpy.types.MovieClip.display_aspect:

Display Aspect Ratio
   Changes the aspect ratio for displaying only. It does not affect the tracking or solving process.


Marker Display
==============

Defines how markers are displayed in the editor.
Settings can be found in the :ref:`Clip Display <clip-editor-clip-display-label>` pop-over.

Pattern
   Can be used to disable displaying of rectangles which correspond to pattern areas of tracks.
   In some cases it helps
   to make the clip view cleaner to check how good tracking is.

Search :kbd:`Alt-S`
   Can be used to disable displaying of rectangles which correspond to search areas of tracks.
   In some cases it helps to make the clip view cleaner to check how good tracking is.
   Only search areas for selected tracks will be displayed.

Path
   And *Length* control displaying of the paths of tracks. The ways tracks are moving can be visible looking
   at only one frame. It helps to determine if a track jumps from its position or not.

Show Disabled :kbd:`Alt-D`
   Makes it possible to hide all tracks which are disabled on the current frame.
   This helps to make view more clear, to see if the tracking is accurate enough.

Info
   Displays information such as track name and status of the track
   (if it is keyframed, disabled, tracked or estimated).
   Names and status for selected tracks are displayed.

3D Markers
   Shows the markers after solving the movie clip. Therefor the solved position of each track is
   projected back to the movie clip and displayed as a small point.
   The color of the point depends on the distance between the projected coordinate and
   the original coordinate: if they are close enough, the point is green, otherwise it will be red.
   This helps to find tracks which were not solved nicely and need to be tweaked.

Display Thin
   The way in which markers are displayed compact (black outline and yellow foreground color)
   makes tracks visible on all kind of footage (both dark and light).
   But sometimes it can be annoying and this option will make the marker display more compactly --
   the outline is replaced by dashed black lines rendered on top of the foreground,
   so that marker areas are only 1px thick.

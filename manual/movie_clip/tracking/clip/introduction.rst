
************
Introduction
************

The Clip View is used is the main part of the of the Movie Clip editor.
Almost all motion tracking tools are concentrated in the Movie Clip Editor.

It should be mentioned that the camera solver consists of three quite separate steps:

#. 2D tracking of footage.
#. Camera intrinsics (focal length, distortion coefficients) specification/estimation/calibration.
#. Solving camera, scene orientation, and scene reconstruction.


Header
======

Marker Display
--------------

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
   Makes sense after solving the movie clip,
   and it works in the following way: the solved position of each track gets
   projected back to the movie clip and displayed as a small point. The color of the point depends on the distance
   between the projected coordinate and the original coordinate: if they are close enough, the point is green,
   otherwise it will be red. This helps to find tracks which were not solved nicely and need to be tweaked.
Display Thin
   The way in which markers are displayed compact (black outline and yellow foreground color)
   makes tracks visible on all kind of footage (both dark and light).
   But sometimes it can be annoying and this option will make the marker display more compactly --
   the outline is replaced by dashed black lines rendered on top of the foreground,
   so that marker areas are only 1px thick.

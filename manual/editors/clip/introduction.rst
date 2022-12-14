.. index:: Editors; Movie Clip Editor

************
Introduction
************

The Movie Clip Editor has two main purposes,
it can be used for :doc:`tracking or masking </movie_clip/index>` movies.
The empty editor looks like the image below.

.. figure:: /images/editors_clip_introduction_example.png

   Movie Clip Editor interface.


Header
======

Mode
   - :doc:`Tracking </movie_clip/tracking/index>`
   - :doc:`Mask </movie_clip/masking/index>`

View
   Menu of operators for controlling how the content is displayed in the editor.

   Center View to Cursor
      Centers the view so that the cursor is in the middle of the view.
Select
   Menu of operators for :doc:`Selecting Markers </movie_clip/tracking/clip/selecting>`.
Clip
   Menu of operators for :doc:`Editing Movie Clips </movie_clip/tracking/clip/editing/clip>`.

Clip
   A :ref:`data-block menu <ui-data-block>` used for add a movie file.
   Both movie files and image sequences can be used in the Clip editor.
   When a movie clip is loaded into the Clip editor, extra panels are displayed in the interface.

Pivot Point
   See :doc:`Pivot Points </editors/3dview/controls/pivot_point/index>`.

.. _bpy.types.SpaceClipEditor.lock_selection:
.. _bpy.ops.clip.lock_selection_toggle:

Toggle Lock Selection :kbd:`L`
   Display selected tracks at the same screen position
   along the whole footage during playback or tracking.
   This option helps to control the tracking process and
   stop it when the track is starting to slide off or when it jumped.

Clip Display
   See :doc:`/editors/clip/display/clip_display`.

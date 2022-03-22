
**********
Navigating
**********

Header
======

.. figure:: /images/video-editing_sequencer_navigating_header.png
   :align: center

   Video Sequencer Header.


.. _bpy.types.SpaceSequenceEditor.show_region_hud:

View Menu
---------

As usual, the View Menu controls the editor's view settings.

Sidebar :kbd:`N`
   Show or hide the :ref:`Sidebar <ui-region-sidebar>`.
Toolbar :kbd:`T`
   Show or hide the :ref:`Toolbar <ui-region-toolbar>`.
Adjust Last Operation
   Displays a pop-up panel to alter properties of the last
   completed operation. See :ref:`bpy.ops.screen.redo_last`.
Preview as Backdrop
   Displays the current frame in the background of the main view like in the Compositor.

Frame Selected :kbd:`NumpadPeriod`
   Zooms in the display to fit only the selected strips.
Frame All :kbd:`Home`
   Zooms the display to show all strips.
Zoom :kbd:`Shift-B`
   Click and drag to draw a rectangle and zoom to this rectangle.

Navigation
   Play Animation :kbd:`Spacebar`
      Start or stop playback of animation. This will start playback in all editors.
   Go to Current Frame :kbd:`Numpad0`
      Scrolls the timeline so the current frame is in the center.
   Jump to Previous Strip :kbd:`PageDown`
      Current frame will jump to beginning of strip.
   Jump to Next Strip :kbd:`PageUp`
      Current frame will jump to end of strip.
   Jump to Previous Strip (Center) :kbd:`Alt-PageDown`
      Jump to previous center of the strip.
   Jump to Next Strip (Center) :kbd:`Alt-PageUp`
      Jump to next center of the strip.
Range
   Set Preview Range :kbd:`P`
      Interactively define frame range used for playback.
      Allows you to define a temporary preview range to use for animation playback
      (this is the same thing as the *Playback Range* option of
      the :ref:`Timeline editor header <animation-editors-timeline-headercontrols>`).
   Set Preview Range to Strips
      Sets the frame range of preview to the range of the selected strips.
   Clear Preview Range :kbd:`Alt-P`
      Clears preview range.
   Set Start Frame :kbd:`Ctrl-Home`
      Set Start of animation range to the current frame.
   Set End Frame :kbd:`Ctrl-End`
      Set End of animation range to the current frame.
   Set Frame Range to Strips
      Sets the frame range of preview and render animation to the frame range of the selected strips.

.. _bpy.ops.sequencer.refresh_all:

Refresh All
   To force Blender to re-read in files, and to force a re-render of the 3D Viewport,
   click the *Refresh Sequencer* button.
   Blender will update and synchronize all cached images and compute the current frame.

   Certain operations, like moving an object in the 3D Viewport, may not force the *Sequencer*
   to call for a refresh of the rendered image (since the movement may not affect the rendered image).
   If an image or video, used as a strip, is changed by some application outside of Blender,
   Blender has no real way of being notified from your operating system.

Sync Visible Range
   Synchronize the visible range with other time based editors.

Show Seconds :kbd:`Ctrl-T`
   Shows seconds instead of frames on the time axis.
Show Markers
   Shows the markers region. When disabled, the `Markers Menu`_ is also hidden
   and markers operators are not available in this editor.

.. _bpy.types.SequenceEditor.show_cache:

Show Cache
   Show which frames are :doc:`Cached </video_editing/sequencer/sidebar/cache>`
   Show all enabled types;
   Final Images, Raw Images, Preprocessed Images, Composite Images

   In order for this property to be visible, enable :ref:`Developer Extras <prefs-interface-dev-extras>`.

Sequence Render Image
   Render an image of the current frame.
Sequence Render Animation
   Render timeline from Preview Start to Preview End Frame to a Video file or series of images.

Export Subtitles
   Exports :doc:`Text strips </video_editing/edit/montage/strips/text>`,
   which can act as subtitles, to a `SubRip <https://en.wikipedia.org/wiki/SubRip>`__ file (``.srt``).
   The exported file contains all Text strips in the video sequence.

Toggle Sequencer/Preview :kbd:`Ctrl-Tab`
   Switch the editor display type between Sequencer and Preview.


Markers Menu
------------

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, markers are shown at the bottom of the editor.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

For descriptions of the different marker tools see :ref:`Editing Markers <animation-markers-editing>`.


Main View
=========

Adjusting the View
------------------

Use these shortcuts to adjust the sequence area of the editor:

- Pan: :kbd:`MMB`
- Zoom: :kbd:`Wheel`
- Vertical Scroll: use :kbd:`Shift-Wheel`, or drag on the left scrollbar.
- Horizontal Scroll: use :kbd:`Ctrl-Wheel`, or drag on the lower scrollbar.
- Scale View: :kbd:`Ctrl-MMB` and drag up/down (vertical scale) or left/right (horizontal scale).
- Scale View Vertically: drag on the circles on the vertical scrollbar.
- Scale View Horizontally: drag on the circles on the horizontal scrollbar.


Playhead
--------

The Playhead is the blue vertical line with the current frame number at the top.
It can be set or moved to a new position by pressing or holding :kbd:`LMB`
in scrubbing area at the top of the timeline.
You can move the Playhead in increments by pressing :kbd:`Left` or :kbd:`Right`, or by using :kbd:`Alt-Wheel`.
You can also jump to the beginning or end frame by pressing :kbd:`Shift-Left` or :kbd:`Shift-Right`.
As you do, the image for that frame is displayed in the Preview region.

When you drag the frame indicator with :kbd:`Shift-RMB` directly on a sequence strip,
this will show the strip *solo*, (temporarily disregarding effects and other strips,
showing only this strip's output) and the strip will be highlighted.

When holding :kbd:`Ctrl` while dragging it will snap to the start and endpoints of strips.

Real-time preview is possible on reasonable computers
when viewing an image sequence or movie (``avi``/``mov``) file.
Scene strips can use viewport previews or proxies for real-time playback,
otherwise displaying rendered frame is supported, but typically too slow for real-time playback.

.. hint::

   Every other synced editor can be used for scrubbing e.g. the Timeline.

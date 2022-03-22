
*******
Sidebar
*******

The sidebar of the Preview can be toggled with the menu:
:menuselection:`View --> Sidebar` or with the shortcut :kbd:`N`.

:ref:`fig-editors_vse_preview_sidebar-overview` shows the sidebar of the Preview,
but also the sidebar of the sequencer. In the Preview sidebar,
the View tab is active and all panels are expanded.
Safe Areas are enabled and an Annotation is added.

.. _fig-editors_vse_preview_sidebar-overview:
.. figure:: /images/editors_vse_preview_sidebar-overview.svg
   :alt: Sidebar overview

   Video Sequence Editor with two sidebars: Preview and Sequencer.


Tool
====

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> Tool tab`

Displays information about the active :doc:`tool </editors/video_sequencer/preview/toolbar>`.


View
====

View Settings
-------------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> View Settings`

.. _bpy.types.SpaceSequenceEditor.proxy_render_size:

Proxy Render Size
   Size to display proxies at in the preview region.
   Using a smaller preview size will increase speed.

   :No Display: Disables the preview.
   :Scene Size: Matches proxy size to the final render :ref:`resolution <bpy.types.RenderSettings.resolution_y>`.
   :25%, 50%, 75%, 100%: Proxies are sized to be the selected percent of the original input.

.. _bpy.types.SpaceSequenceEditor.use_proxies:

Use Proxies
   Use optimized files for faster scrubbing when available.
   Proxies limit the visual accuracy of the preview by reducing
   the preview resolution and using compressed copies of the input.

.. _bpy.types.SequenceEditor.use_prefetch:

Prefetch Frames
   Automatically fill the cache with frames after the current frame in the background.
   Use this to achieve a more consistent playback speed.
   This feature currently doesn't support rendering Scene strips.

.. _bpy.types.SpaceSequenceEditor.display_channel:

Channel
   Selects the channel to show in the preview.

   Channel 0 is the compositing result of all strips.
   Channel 1 is the current frame's image from the strip in channel 1 only
   (channel 1 is at the bottom of the stack). The display of these modes is either the composite
   (channel 0) or the frame from the strip (channels 1 through n).

.. _bpy.types.SpaceSequenceEditor.show_overexposed:

Show Overexposed
   Shows overexposed (bright white) areas using a zebra pattern.
   The threshold can be adjust with the slider.


.. _editors_sequencer_preview_2d-cursor:

2D Cursor
---------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> 2D Cursor`

The 2D cursor is the white-red circle with a cross-hair that is shown in the main region.
It can be used by setting the :ref:`Pivot Point <bpy.types.SequencerToolSettings.pivot_point>`
to *2D Cursor* to transform all strips in relation to the location of the 2D cursor.

The visibility of the 2D cursor can be controlled with the
:ref:`2D Cursor <bpy.types.SequencerPreviewOverlay.show_cursor>` overlay option.

.. _bpy.types.SpaceSequenceEditor.cursor_location:

Location X, Y
   The location of the 2D cursor relative to the center of the main region.
   The edge of the image will be 0.5 away, so (0.5, 0.5) will be the top right corner.

   The 2D cursor's location can also be set with Cursor tool or by :kbd:`Shift-RMB`.


.. _bpy.types.SequenceEditor.show_overlay:

Frame Overlay
-------------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Frame Overlay`

Option to enable the overlay.
It can be used for comparing the current frame to a reference frame.

.. _bpy.ops.sequencer.view_ghost_border:

Set Overlay Region
   Selects the rectangular bounds for the overlay region.
   This area can be defined by pressing :kbd:`O` key over the preview.

.. _bpy.types.SequenceEditor.overlay_frame:

Frame Offset
   The slider controls the offset of the reference frame relative to current frame.

.. _bpy.types.SpaceSequenceEditor.overlay_frame_type:

Overlay Type
   It describes the way the reference frame should be displayed.

   :Rectangle: Which means the rectangle area of reference frame will be displayed on top of current frame.
   :Reference: Only the reference frame is displayed in the preview region.
   :Current: Only the current frame is displayed in the preview region.

   .. tip::

      It is possible to have several Sequence Editors opened and they can use different overlay types.
      So it is possible to have current and reference frames displayed in different editor spaces.

.. _bpy.types.SequenceEditor.use_overlay_frame_lock:

Overlay Lock
   It's still possible to lock the reference frame to its current position.


Safe Areas
----------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Safe Areas`

Shows guides used to position elements to ensure that
the most important parts of the video can be seen across all screens.

.. seealso::

   :ref:`Camera Safe Areas <bpy.types.DisplaySafeAreas>`.


Scene Strip Display
-------------------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Scene Strip Display`

It allows you to control how the images of :doc:`Scene Strips </video_editing/edit/montage/strips/scene>`
are displayed in the preview.

.. _bpy.types.RenderSettings.sequencer_gl_preview:

Shading
   Method for rendering the viewport.
   See the 3D Viewport's :ref:`view3d-viewport-shading` options.

.. _bpy.types.RenderSettings.use_sequencer_override_scene_strip:

Override Scene Settings
   Use the :doc:`Workbench render settings </render/workbench/index>` from the sequencer scene,
   *not* the Workbench render settings from the source scene.
   This option is only available, if *Solid* shading is activate.


Annotations
-----------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Annotations`

Allows you to use :doc:`Annotations </interface/annotate_tool>` in the Sequencer.


.. _editors_vse_preview_sidebar-metadata:

Metadata
========

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> Metadata tab`

Lists information that has been encoded in the currently displayed movie or image strip;
note that this is the strip under the playhead, *not* the active (selected) strip.
Note, this metadata is readonly and cannot be edited in Blender.
Metadata can include the filename, the date created, the camera model etc.
The metadata from saved from a Blender render is also displayed in the appropriate fields (camera, time, etc...;
see :doc:`Rendered Output </render/output/properties/metadata>` for a full list.
Some other graphic program also store some metadata, however,
only the text stored in the header field "Comments" can be read

Some of this metadata can also be made visible in the Preview with the
:ref:`Metadata <bpy.types.SequencerPreviewOverlay.show_metadata>` overlay.

.. tip::

   To edit a files metadata you can use an external program such as exiftool.
   For example, the command to change the "Comments" field is::

      exiftool --comments="My new comment" name-of-file.png

.. note::

   The metadata will only be displayed for the image/ movie strip and not from strips processed by any effect strip.
   For example, adding an effect strip (eg. Glow) will hide the metadata from view.
   Of course, the metadata isn't removed from the file. Hiding the effect strip will display it again.


*******
Sidebar
*******

Tool
====

Displayes information about the active tool.


View
====

View Settings
-------------

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
   This feature currently doesn't support rendering scene strips.

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


.. _bpy.types.SequenceEditor.show_overlay:

Frame Overlay
-------------

Option to enable the overlay.
It can be used for comparing the current frame to a reference frame.

.. _bpy.ops.sequencer.view_ghost_border:

Set Overlay Region
   Selects the rectangular bounds for the overlay region.
   This area can be defined by pressing :kbd:`O` key over the preview.

.. _bpy.types.SequenceEditor.overlay_frame:

Frame Offset
   The slider controls the offset of the reference frame relative to current frame.

.. _bpy.types.SpaceSequenceEditor.overlay_type:

Overlay Type
   It describes the way the reference frame should be displayed.

   :Rectangle: Which means the rectangle area of reference frame will be displayed on top of current frame.
   :Reference: Only the reference frame is displayed in the preview region.
   :Current: Only the current frame is displayed in the preview region.

   .. tip::

      It is possible to have several Sequence Editors opened and they can use different overlay types.
      So it is possible to have current and reference frames displayed in different editor spaces.

.. _bpy.types.SequenceEditor.use_overlay_lock:

Overlay Lock
   It's still possible to lock the reference frame to its current position.


Safe Areas
----------

Shows guides used to position elements to ensure that
the most important parts of the video can be seen across all screens.

.. seealso::

   See :ref:`Safe Areas <camera-safe-areas>` in the camera docs.


Scene Strip Display
-------------------

It allows you to control how the images of :doc:`Scene Strips </video_editing/sequencer/strips/scene>`
are displayed in the preview.

Shading
   Method for rendering the viewport.
   See the 3D Viewport's :ref:`view3d-viewport-shading` options.

Override Scene Settings
   Use the Workbench render settings from the sequencer scene,
   instead of each individual scene used in the strip.


Annotations
-----------

Allows you to use :doc:`Annotations </interface/annotate_tool>` in the Sequencer.


Metadata
========

A list of metadata of the displayed image.

.. note::

   The metadata will only be displayed for the image, that has not been processed by any effect.
   By default images are processed by alpha over blending.

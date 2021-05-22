
************
Introduction
************

Sequencer preview is used to display result of rendering Sequencer timeline.
This can be further configured to display output from certain channel, overlay or image analyzer (scope).
You can adjust the view by zooming in with :kbd:`NumpadPlus` and zoom out with :kbd:`NumpadMinus`.


Header
======

.. figure:: /images/video-editing_preview_introduction_header.png

   Sequencer Display header.


.. _bpy.types.SpaceSequenceEditor.show:

View Menu
---------

Sidebar :kbd:`N`
   Show or hide the :ref:`Sidebar <ui-region-sidebar>`.
Toolbar :kbd:`T`
   Show or hide the :ref:`Toolbar <ui-region-toolbar>`.

Preview During Transform
   Show a preview of the start or end frame while transforming a strip's start/end handles.

Fit Preview in Window :kbd:`Home`
   Resize the preview so that it fits in the area.
Zoom :kbd:`Shift-B`
   Click and drag to draw a rectangle and zoom to this rectangle.
Fractional Zoom
   Resize the preview in steps from 1:8 to 8:1.

Sequence Render Image
   Render the an image at the current frame.
Sequence Render Animation
   Render timeline from Preview Start to Preview End Frame to a Video file or series of images.

.. _bpy.ops.sequencer.export_subtitles:

Export Subtitles
   Exports :doc:`Text strips </video_editing/sequencer/strips/text>`,
   which can act as subtitles, to a `SubRip <https://en.wikipedia.org/wiki/SubRip>`__ file (``.srt``).
   The exported file contains all Text strips in the video sequence.

Toggle Sequencer/Preview :kbd:`Ctrl-Tab`
   Switch the editor display type between Sequencer and Preview.


Display Mode
------------

Mode to show different aspects of the composite result,
for the current frame:

Image Preview
   Render image preview.
Luma Waveform
   Brightness/contrast analyzer.
Chroma Vectorscope
   Color hue and saturation analyzer.
Histogram
   RGB distribution histogram.


Display Channels
----------------

Color and Alpha
   Display preview image with transparency over checkerboard pattern.
Color
   Ignore transparency of preview image (fully transparent areas will be black).


Overlays
--------

Overlays are information that is displayed on top of the preview region.
There is a switch to turn off/on all overlays for the preview region.

.. rubric:: Preview Overlays

Frame Overlay
   Displays the :ref:`Frame Overlay <bpy.types.SequenceEditor.show_overlay>`,
   to compare the current frame to a reference frame.

.. _bpy.types.SpaceSequenceEditor.show_safe_areas:

Safe Areas
   Display an overlay on the preview, marking where the title safe regions are.

.. _bpy.types.SpaceSequenceEditor.show_metadata:

Metadata
   Display Image metadata in the preview area.

.. _bpy.types.SpaceSequenceEditor.show_annotation:

Annotations
   Displays :doc:`Annotations </interface/annotate_tool>` in the preview region.


Gizmos
======

You can use gizmos to pan and zoom image in the Sequencer preview region.


************
Introduction
************

Sequencer preview is used to display result of rendering Sequencer timeline.
This can be further configured to display output from certain channel, overlay or image analyzer (scope).

The Preview contains two regions (see figure 1), the Header is shown
in a yellow outline with the *Preview* (red outline) underneath.
This Preview has no fixed dimensions; you can zoom in or move indefinitely.
However, in figure 1 you see a checkered area (green outline).
This preview has the aspect ratio of the Project Dimensions; e.g. 1920 x 1080 pixels in figure 1.
But, because the source strip could be scaled in a different resolution,
the yellow outline shows the area that the source strip occupies.
As you can see, the Open movie "Spring" has a different resolution than
the project and letterboxes are added at the top and bottom of the image.

In contrast with the :doc:`Sequencer View </editors/video_sequencer/sequencer/index>` example,
both the Toolbar and Sidebar are expanded in figure 1.
The gizmos however are unique for the Preview.

.. figure:: /images/editors_vse_type.svg
   :alt: Preview window

   Figure 1: Preview window of VSE.

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

Refresh All
   To force Blender to re-read in files, and to force a re-render of the 3D Viewport,
   click the *Refresh Sequencer* button.
   Blender will update and synchronize all cached images and compute the current frame.

   Certain operations, like moving an object in the 3D Viewport, may not force the *Sequencer*
   to call for a refresh of the rendered image (since the movement may not affect the rendered image).
   If an image or video, used as a strip, is changed by some application outside of Blender,
   Blender has no real way of being notified from your operating system.

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

See :doc:`/editors/video_sequencer/preview/display/display_mode`.


Display Channels
----------------

Color and Alpha
   Display preview image with transparency over checkerboard pattern.
Color
   Ignore transparency of preview image (fully transparent areas will be black).


Overlays
--------

See :doc:`Preview Overlays </editors/video_sequencer/preview/display/overlays>`.


Gizmos
======

You can use gizmos to pan and zoom image in the Sequencer preview region.

See :doc:`/editors/video_sequencer/preview/display/gizmos` to manage the visibility of gizmos.

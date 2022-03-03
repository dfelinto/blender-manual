
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


Gizmos
======

You can use gizmos to pan and zoom image in the Sequencer preview region.

See :doc:`/editors/video_sequencer/preview/display/gizmos` to manage the visibility of gizmos.

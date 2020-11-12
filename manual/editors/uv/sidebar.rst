
*******
Sidebar
*******

Image Tab
=========

UV Vertex
---------

Transform Properties :doc:`Selecting UVs </modeling/meshes/uv/editing>`.


Image
-----

See :doc:`/editors/image/image_settings`.


UDIM Grid
---------

Allows you to control the grid size of :doc:`UDIM </modeling/meshes/uv/workflows/udims>` tiles.


Tool Tab
========

Shows the settings for the active tool.


View Tab
========

Display
-------

You can set the editors display options in this panel.

.. figure:: /images/editors_uv_display-panel_panel.png
   :align: right

   Display panel: With both an image and UVs selected.

Aspect Ratio
   Display Aspect for this image. Does not affect rendering.

Repeat Image
   Duplicate the image until it is repeated to fill the main view.

.. _bpy.types.SpaceUVEditor.show_pixel_coords:

Pixel Coordinates
   Display UV coordinates in pixels rather than from 0.0 to 1.0


2D Cursor
---------

Location X, Y
   Control 2D cursor location.


Annotations
-----------

Options for the :doc:`annotation tool </interface/annotate_tool>`.


.. (TODO add) images per type

Scopes
======

.. figure:: /images/editors_image_scopes_main.png
   :align: right

   Scopes in the Image editor.


Histogram
---------

This mode displays a graph showing the distribution of color information in the pixels of
the currently displayed image. The X axis represents values of pixel, from 0 to 1 (or 0 to 255),
while the Y axis represents the number of pixels in that tonal range.
A predominantly dark image would have most of its information toward the left side of the graph.

Use this mode to balance out the tonal range in an image.
A well balanced image should have a nice smooth distribution of color values.

Luma
   Shows the luminosity of an image.
RGB
   Shows the :abbr:`RGB (Red, Green, Blue)` channels stacked on top of each other.
R/G/B/A
   Depending on the channel you choose the scope will show the appropriate channel.
Show Line
   Displays lines rather than filled shapes.


Waveform
--------

.. (TODO add) description of a Waveform maybe this should go in the glossary?

Waveform Opacity
   Opacity of the points.

Waveform Mode
   Luma
      ToDo.
   YCbCr
      ToDo.
   Parade
      The RGB channels are shown side-by-side.
   Red Green Blue
      Shows the RGB channels overlaid as a "Full color" waveform.
      It is useful for color grading.


Vectorscope
-----------

.. (TODO add) description of a Vectorscope maybe this should go in the glossary?

Vectorscope Opacity
   Opacity of the points.


Sample Line
-----------

The *Sample Line* scope is the same as the `Histogram`_
but allows you to get the sample data from a line.

Sample Line
   Used to draw a line to use to read the sample data from.


Scope Samples
-------------

Full Sample
   Sample every pixel.

Accuracy
   Proportion of original image source pixel lines to sample.

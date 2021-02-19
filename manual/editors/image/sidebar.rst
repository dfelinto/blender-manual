
*******
Sidebar
*******

Tool
====

Displays the settings of the active tool.


Image
=====

Image
-----

Tools for working with images, see :doc:`/editors/image/image_settings`.


Metadata
--------

Lists image metadata.


View Tab
========

.. _bpy.types.Image.display_aspect:
.. _bpy.types.SpaceImageEditor.show_repeat:

Display
-------

You can set the editors display options in this panel.

.. figure:: /images/editors_image_view-tab_panel.png
   :align: right

   Display panel.

Aspect Ratio
   Display Aspect for this image. Does not affect rendering.
Repeat Image
   Duplicate the image until it is repeated to fill the main view.


Annotations
-----------

Options for the annotation tool. See :doc:`/interface/annotate_tool`.


.. (TODO add) images per type

.. _editors-image-scopes:

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

.. _bpy.types.TextSequence:

***********
Text Strips
***********

The Text strip allows you to directly display text in the Sequence editor.
The strip will display the text inserted in its text field on the final sequence.

.. tip::

   All Text strips in a video sequence can be :ref:`exported <bpy.ops.sequencer.export_subtitles>`
   as a `SubRip <https://en.wikipedia.org/wiki/SubRip>`__ file.
   This is useful when using Text strips as subtitles.


Options
=======

Text
   The actual text displayed.

Wrap Width
   Wraps the text by the percentage of the frame width,
   setting this to zero disables word wrapping.


Style
-----

Font
   :ref:`ui-data-block` to choose which font-file is used to render the text.

   Bold
      Use a bold font face with a strong/thick visual appearance.
   Italics
      Use an italizized font face with a slanted visual appearance.
Size
   Size of the text.
Color
   The text color.
Shadow
   Creates a shadow of the specified color under the text.
Box
   Creates a background for the text to improve the readability and clarity of text in some situations.
   The color and opacity of the box can be adjusted using the color selector.
Box Margin
   The distance the box boundaries extends from the boundaries of the font glyphs.
   The distance is measured as a factor of the image's width.


Layout
------

Location X, Y
   Positions the text on the X, Y axis.
Anchor X, Y
   Horizontal (X) or vertical (Y) anchor point of the text relative to the location.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_text_example.png

   Text Effect.

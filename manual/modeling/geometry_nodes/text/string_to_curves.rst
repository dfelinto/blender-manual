.. index:: Geometry Nodes; String to Curves
.. _bpy.types.GeometryNodeStringtoCurves:

*********************
String to Curves Node
*********************

.. figure:: /images/modeling_geometry-nodes_text_string-to-curves_node.png
   :align: right

   String to Curves node.

The *String to Curves* converts a string to curve geometry.


Inputs
======

String
   Standard string input.

Size
   Size of the curve.

Character Spacing
   A factor by which space between each character (kerning) is scaled in width.

Word Spacing
   A factor by which white-space between words is scaled in width.

Line Spacing
   A factor by which the vertical space between lines is scaled.

Max Width
   Maximum width of the text


Properties
==========

Font
   Font glyph used to generate the curve.

Overflow
   :Overflow: Allows the text to use more space than the specified height.
   :Scale To Fit: Scales the text size to fit the width and height.
   :Truncate: Only outputs curves that fit within the width and height.

Alignment
   :Left: Aligns the text to the left.
   :Center: Aligns the text to the center.
   :Right: Aligns the text to the right.
   :Justify: Aligns the text to the left and right.
   :Flush: Aligns the text to the left and right with equal character spacing.

Align Y
   :Top Baseline: Aligns the text to the top baseline.
   :Top: Aligns the text to the top.
   :Middle: Aligns the text to the middle.
   :Bottom Baseline: Aligns the text to the bottom baseline.
   :Bottom: Aligns the text to the bottom.


Outputs
=======

Curves
   Generated curve.

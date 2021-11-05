.. index:: Geometry Nodes; String to Curves
.. _bpy.types.GeometryNodeStringtoCurves:

*********************
String to Curves Node
*********************

.. figure:: /images/modeling_geometry-nodes_text_string-to-curves_node.png
   :align: right

   String to Curves node.

The *String to Curves* converts a string to curve instances. Each unique character used in the string
is converted to a curve once, and further uses of that character are more instances of the same geometry.

This makes processing the output geometry very efficient, because each unique character
only has to be processed once. However, it means that the result will be the same
for every instance of the same character. To process each character individually,
the :doc:`/modeling/geometry_nodes/instances/realize_instances` can be used.

.. tip::

   :doc:`Socket inspection </modeling/geometry_nodes/inspection>` can be used to see the value
   of the string input used when the node was evaluated, by holding the mouse over the socket.


Inputs
======

String
   Standard string input.

Size
   The size of each character. The values of the other inputs are scaled by this value.

Character Spacing
   A factor by which the space between each character (kerning) is scaled on the X axis.

Word Spacing
   A factor by which whitespace between words is scaled on the X axis.

Line Spacing
   The distance between separate lines in the output. Scaled by the *Size* input.

Max Width
   Maximum width of the text, applies when the *Overflow* mode is set to *Overflow*.

Text Box Width
   The maximum width of each line, though individual words will not be wrapped.

Text Box Height
   The maximum height for all the lines of the text.


Properties
==========

Font
   Font glyph used to generate the curve.

Overflow
   :Overflow:
      Allows the text to use more space than the specified height. The width of the output is
      still constrained by the *Max Width* input though.
   :Scale To Fit:
      Scales the text size to fit the width and height.
   :Truncate:
      Only outputs text characters that fit within the width and height, based on the *Size* input.
      Any part of the string that did not fit is moved to the *Remainder* output.

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
   Curve instances geometry.

Remainder
   The part of the text that did not fit in the box described by the *Text Box Height* and
   *Text Box Width* inputs. Only used in the *Truncate* overflow mode.


Examples
========

.. figure:: /images/modeling_geometry-nodes_text_string-to-curves_example.png
   :align: center

The node can be used to make overflowing text boxes. Here, the text that does not fit into
the first node's fix-sized text box is passed to a separate *String to Curves* node.
And finally added with a *Scale to Fit* node.

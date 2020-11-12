.. _gpencil_sculpt-toolbar-index:

***************
Sculpting Tools
***************

For Grease Pencil sculpt modes each brush type is exposed as a tool,
the brush can be changed in the Tool Settings.
See :doc:`Brush </grease_pencil/modes/sculpting/tool_settings/brush>` for more information.

.. figure:: /images/grease-pencil_modes_sculpting_tools_brushes.png
   :align: right

Smooth
   Eliminates irregularities in the area of the drawing
   within the brush's influence by smoothing the positions of the points.

Thickness
   Increase or decrease the points thickness in the area of the drawing
   within the brush's influence.

Strength
   Increase or decrease the points transparency (alpha) in the area of the drawing
   within the brush's influence.

Randomize
   Add noise to the strokes in the area of the drawing
   within the brush's influence by moving points location in a random way.

Grab
   Used to drag a group of points around. Unlike the other brushes,
   Grab does not modify different points as the brush is dragged across the model.
   Instead, Grab selects a group of points on mouse-down, and pulls them to follow the mouse.
   The effect is similar to moving a group of points in Edit Mode with Proportional Editing enabled.

Push
   Moves points in the direction of the brush stroke.

Twist
   Twist the points in counter-clockwise (CCW) or Clockwise (CW) rotation.

Pinch/Inflate
   Pulls points towards the center of the brush.
   The inverse setting is Inflate, in which points are pushed away from the center of the brush.

Clone
   Adds copies of the strokes in the clipboard in the center of the brush.
   You have to copy the selected strokes you want into the clipboard with :kbd:`Ctrl-C` before using the tool.

:ref:`Annotate <tool-annotate>`
   Draw free-hand annotation.

   Annotate Line
      Draw straight line annotation.
   Annotate Polygon
      Draw a polygon annotation.
   Annotate Eraser
      Erase previous drawn annotations.

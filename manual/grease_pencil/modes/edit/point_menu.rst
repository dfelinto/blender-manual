
**********
Point Menu
**********

.. _bpy.ops.gpencil.extrude_move:

Extrude
=======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Extrude`
   :Tool:      :menuselection:`Toolbar --> Extrude`
   :Hotkey:    :kbd:`E`

Extrudes points by duplicating the selected points, which then can be moved.
The new points stay connected with the original points of the edit line.

.. note::

   Since Grease Pencil strokes can only have one start an end point,
   a new stroke will be created when extrude intermediate points in the strokes.


.. _bpy.ops.gpencil.stroke_smooth:

Smooth
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Smooth`

Softens strokes by reducing the differences in the locations of the points along the line,
while trying to maintain similar values that make the line fluid and smoother.

Repeat
   The number of times to repeat the procedure.

Factor
   The amount of the smoothness to apply.

Selected Points
   When enabled, limits the effect to only the selected points within the stroke.

Position
   When enabled, the operator affect the points location.

Thickness
   When enabled, the operator affect the points thickness.

Strength
   When enabled, the operator affect the points strength (alpha).

UVs
   When enabled, the operator affect the UV rotation on the points.


.. _bpy.ops.gpencil.stroke_merge:

Merge
=====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Merge`

Combine all selected points into a unique stroke.
All the selected points will be connected by new edit lines when needed to create the new stroke.

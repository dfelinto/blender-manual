
***********
Stroke Menu
***********

This page covers many of the tools in the *Strokes* menu.
These are tools that work primarily on strokes, however,
some also work with point selections.


.. _bpy.ops.gpencil.stroke_subdivide:

Subdivide
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Subdivide`

Subdivides the strokes by inserting points between the selected points.

Number of Cuts
   The number of subdivisions to perform.

Smooth
   The amount of the smoothness on subdivided points.

Repeat
   Number of times to repeat the procedure.

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


.. _bpy.ops.gpencil.stroke_simplify_fixed:
.. _bpy.ops.gpencil.stroke_simplify:
.. _bpy.ops.gpencil.stroke_sample:

Simplify
========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Simplify`

Reduce the amount of points in the strokes.

Fixed
   Deletes alternated points in the strokes, except the start and end points.

   Steps
      The number of times to repeat the procedure.

Adaptive
   Uses the RDP algorithm (Ramer-Douglas-Peucker algorithm) for points deletion.
   The algorithm tries to obtain a similar line shape with fewer points.

   Factor
      Controls the amount of recursively simplifications applied by the algorithm.

Sample
   Recreates the stroke geometry with a predefined length between points.

   Length
      The distance between points on the recreated stroke.
      Smaller values will require more points to recreate the stroke,
      while larger values will result in fewer points needed to recreate the curve.


.. _bpy.ops.gpencil.stroke_trim:

Trim
====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Trim`

Trims selected stroke to first loop or intersection.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_trim-1.png
          :width: 320px

          Original stroke.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_trim-2.png
          :width: 320px

          Result of trim operation.


.. _bpy.ops.gpencil.stroke_join:

Join
====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Join --> Join, Join and Copy`
   :Shortcut:  :kbd:`Ctrl-J`, :kbd:`Shift-Ctrl-J`

Join two or more strokes into a single one.

Type
   Join :kbd:`Ctrl-J`
      Join selected strokes by connecting points.

   Join and Copy :kbd:`Shift-Ctrl-J`
      Join selected strokes by connecting points in a new stroke.

Leave Gaps
   When enabled, do not use geometry to connect the strokes.


.. _bpy.ops.gpencil.move_to_layer:

Move to Layer
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Move to Layer`
   :Shortcut:  :kbd:`M`

A pop-up menu to move the stroke to a different layer.
You can choose the layer to move the selected strokes to
from a list of layers of the current Grease Pencil object.
You can also add a new layer to move the selected stroke to.


.. _bpy.ops.gpencil.stroke_change_color:

Assign Material
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Assign Material`

Changes the material linked to the selected stroke.
You can choose the name of the material to be used by the selected stroke
from a list of materials of the current Grease Pencil object.


.. _bpy.ops.gpencil.set_active_material:

Set as Active Material
======================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set as Active Material`

Sets the active object material based on the selected stroke material.


.. _bpy.ops.gpencil.stroke_arrange:

Arrange
=======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Arrange`

Change the drawing order of the strokes in the 2D layer.

Bring to Front
   Moves to the top the selected points/strokes.

Bring Forward
   Moves the selected points/strokes upper the next one in the drawing order.

Send Backward
   Moves the selected points/strokes below the previous one in the drawing order.

Send to Back
   Moves to the bottom the selected points/strokes.


Close
=====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Close`
   :Shortcut:  :kbd:`F`

Close or open strokes by connecting the last and first point.

Type
   Close All
      Close all open selected strokes.

   Open All
      Open all closed selected strokes.

   Toggle
      Close or Open selected strokes as required.

Create Geometry
   When enabled, points are added for closing the strokes.
   If disabled, the operator act the same as *Toggle Cyclic*.


.. _bpy.ops.gpencil.stroke_cyclical_set:

Toggle Cyclic
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Toggle Cyclic`

Toggles between an open stroke and closed stroke (cyclic).

Type
   Close All
      Close all open selected strokes.

   Open All
      Open all closed selected strokes.

   Toggle
      Close or Open selected strokes as required.

   Create Geometry
      When enabled, points are added for closing the strokes like when using the *Close* tool.
      If disabled, the stroke is close without any actual geometry.


.. _bpy.ops.gpencil.stroke_caps_set:

Toggle Caps
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Toggle Caps`

Toggle ending cap styles of the stroke.

Default
   Sets stroke start and end points to rounded (default).

Both
   Toggle stroke start and end points caps to flat or rounded.

Start
   Toggle stroke start point cap to flat or rounded.

End
   Toggle stroke end point cap to flat or rounded.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_cap-1.png
          :width: 200px

          Stroke ending with rounded caps.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_cap-2.png
          :width: 200px

          Stroke ending with flat caps.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_cap-3.png
          :width: 200px

          Stroke ending with combined caps.


.. _bpy.ops.gpencil.stroke_flip:

Switch Direction
================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Switch Direction`

Reverse the direction of the points in the selected strokes
(i.e. the start point will become the end one, and vice versa).


Scale Thickness
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Scale Thickness`

When enabled, scales the stroke thickness during scale transformations.


Reset Fill Transform
====================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Reset Fill Transform`

Reset all fill translation, scaling and rotations in the selected strokes.

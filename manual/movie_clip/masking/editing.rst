
*******
Editing
*******

The tools and panels available to edit masks are the same in both editors.
Editing of mask splines happens in a way similar to editing Bézier curves or paths in GIMP or other curve editors.

.. tip::

   To get interactive feedback on the resulting mask,
   a Mask node can be connected directly to a Viewer node in the Compositor,
   which will then keep updating the compositing result while editing.


Transform
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Transform`

:doc:`Move </scene_layout/object/editing/transform/move>` :kbd:`G`
   Change the location of control points. Control points can also be moved with :kbd:`LMB`.
   The whole spline can be moved by dragging the center dot with :kbd:`LMB`.
:doc:`Rotate </scene_layout/object/editing/transform/rotate>` :kbd:`R`
   Change the location of control points by rotating about a pivot point.
:doc:`Scale </scene_layout/object/editing/transform/scale>` :kbd:`S`
   Change the location of control points by expanding the distance between points.

:doc:`To Sphere </modeling/meshes/editing/mesh/transform/to_sphere>` :kbd:`Shift-Alt-S`
   Morphs the control points to the shape of a circle.
:doc:`Shear </modeling/meshes/editing/mesh/transform/shear>` :kbd:`Shift-Ctrl-Alt-S`
   Shifts control points along a defined axis so parallel control points move past one another.
:doc:`Push/Pull </modeling/meshes/editing/mesh/transform/push_pull>`
   Moves the control points closer together (Push) or further apart (Pull).

Scale Feather :kbd:`Alt-S`
   Will scale the feather size.


Clear Feather Weight
====================

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Clear Feather Weight`

Resets the feather weight to zero.


Toggle Cyclic
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Toggle Cyclic`
   :Shortcut:  :kbd:`Alt-C`

Toggle to create a closed curve or open it again.
Close the mask by joining the last control point to the first.


Set Handle Type
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Set Handle Type`
   :Shortcut:  :kbd:`V`

Set handle type for selected spline points.


Recalculate Handles
===================

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Recalculate Handles`
   :Shortcut:  :kbd:`Ctrl-N`

Make normals (handle directions) consistent.


Switch Direction
================

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Switch Direction`

Switch Direction handle directions in/out.


Copy Paste
==========

Todo.


Parent
======

Todo.


Animation
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Animation`

Masks can be animated with the shape keying system.
This can be useful when there are not enough good feature points to track in the footage,
or the mask is not based on footage.
Mask animation timing can be edited from the *Dope Sheet's* :ref:`Mask Mode <dope-sheet-mask>`.

Insert Shape Key :kbd:`I`
   Will insert a shape key for the active mask layer at the current frame.
   This works on the level of mask layers,
   so inserting a shape key will keyframe all the splines and points contained in it.
Clear Shape Key :kbd:`Alt-I`
   Will clear the shape key for the active mask layer at the current frame.
Feather Reset Animation
   Resets the feather offset across all animated frames.
Re-Key Points of Selected Shapes
   Re-interpolate selected points on across the range of keys selected in the *Dope Sheet*.


Show/Hide
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Show/Hide`

- Hide Selected :kbd:`H`
- Hide Unselected :kbd:`Shift-H`
- Clear Restricted View :kbd:`Alt-H`


Delete
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Mask Mode
   :Menu:      :menuselection:`Mask --> Delete`
   :Shortcut:  :kbd:`X`

Removes control points.


Miscellaneous
=============

Slide Spline Curvature :kbd:`LMB`
   Moves the curve and/or control points by clicking on them and dragging.

Add Vertex and Slide :kbd:`Ctrl-LMB`
   Inserts new control points and defines handle orientations by a continued mouse drag.
   If the last point was selected, double-click will also close the curve.

Add Feather Vertex and Slide :kbd:`Shift-Ctrl-LMB`
   Inserts new feather control points that can be transformed independently of the main spline curve.
   If no feather mask is in use this will create a basic feather mask to the curve.

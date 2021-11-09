
*********
Selecting
*********

This page discusses specific selecting tools for surface objects in Edit Mode.
The Surface Edit also uses the general select tools used which are described
in the :doc:`interface section </interface/selecting>`.

Surface selection in *Edit Mode* is very similar to
:doc:`NURBS curve selection </modeling/curves/selecting>`.
The basic tools are the same as with :doc:`meshes </modeling/meshes/selecting/index>`,
so you can select a simple control point with an :kbd:`LMB`-click,
add to current selection with :kbd:`Shift-LMB` clicks, Border Select, and so on.


Select Menu
===========

The *Select* menu (in the 3D Viewport header) is even simpler than for curves...

All these options have the same meaning and behavior as in :doc:`Object Mode </scene_layout/object/selecting>`
and mesh :doc:`Edit Mode </modeling/meshes/selecting/index>`.

All :kbd:`A`
   Select all.
None :kbd:`Alt-A`
   Select none.
Inverse :kbd:`Ctrl-I`
   Selects all the geometry that is not selected, and deselect currently selected components.

------------------------

:ref:`Box Select <tool-select-box>` :kbd:`B`
   Interactive box selection.
:ref:`Circle Select <tool-select-circle>` :kbd:`C`
   Interactive circle selection.
:ref:`Lasso Select <tool-select-lasso>`
   Interactive freeform selection.

------------------------

`Select Random`_
   Select random control points.

`Checker Deselect`_
   Select every Nth control point.

`Select Linked`_ :kbd:`Ctrl-L`
   Select control points that are connected to the current selection.

`Select Similar`_ :kbd:`Shift-G`
   Select control points that have similar properties to the current selection.

------------------------

`Select Control Point Row`_
   Select a whole :ref:`row <modeling-surfaces-rows-grids>` of control points.

------------------------

`Select More/Less`_
   Select objects based on their parent child relationships.


Select Random
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Random`

Select random control points.

Percent
   Selects the defined percentage of control points.
Random Seed
   :term:`Seed` used by the pseudo-random number generator.
Action
   Controls whether the operator *Selects* or *Deselects* control points.


Checker Deselect
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Checker Deselect`

This tool applies an alternating selected/deselected checker pattern.
This only works if you already have more than one control point selected.

It works by changing the current selection so that only every Nth
control points will remain selected, starting from the active one.

Deselected
   The number of deselected elements in each pattern repetition.
Selected
   The number of selected elements in each pattern repetition.
Offset
   Offset from the starting point.


Select Linked
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Linked`
   :Shortcut:  :kbd:`L`, :kbd:`Ctrl-L`

*Select Linked* will add to the selection the mouse cursor's nearest control point,
and all the linked ones, i.e. all points belonging to the same surface.


Select Similar
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Similar`
   :Shortcut:  :kbd:`Shift-G`

Selects control points that have certain similar properties to the active one.
The :ref:`bpy.ops.screen.redo_last` panel provides several selection options:

Type
   Type
      Selects splines that have the same spline Type i.e. Bézier, NURBS or Poly.
   Radius
      Selects control points that have a similar Radius value.
   Weight
      Selects all points that have a similar Weight value.
   Direction
      Selects control points that have a similar handles direction.

Compare
   Equal, Greater, Less. (only for Radius, Weight) (ToDo 2.76)
Threshold
   Precision (ToDo 2.76)


.. _bpy.ops.curve.select_row:

Select Control Point Row
========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Control Point Row`
   :Shortcut:  :kbd:`Shift-R`

This option works a bit like
:ref:`edge loop selection <bpy.ops.mesh.loop_multi_select>` for meshes,
inasmuch it selects a whole :ref:`row <modeling-surfaces-rows-grids>` of control points,
based on the active (the last selected) one. The first time you press :kbd:`Shift-R`,
the V row passing through (containing) the active point will be added to the *current* selection.
If you use again this shortcut, you will toggle between the U and V row of this point,
removing *everything else* from the selection.


Select More/Less
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> More/Less`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus` / :kbd:`Ctrl-NumpadMinus`

Expand or contract the selection based on current selected control points.

More
   For each selected control point, select **all** its linked points (i.e. two, three or four).
Less
   For each selected control point, if **all** points linked to this point are selected, keep it selected.
   For all other selected control points, deselect them.

This implies two points:

#. First, when **all** control points of a surface are selected, nothing will happen
   (as for *Less*, all linked points are always selected, and of course, *More* cannot add any).
   Conversely, the same goes when no control point is selected.
#. Second, these tools will never "go outside" of a surface
   (they will never "jump" to another surface in the same object).

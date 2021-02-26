
*******
Surface
*******

Surface editing has even fewer tools and options than its curve counterpart,
but has many common points with it...
So this page covers (or tries to cover) all the subjects,
from the basics of surface editing to more advanced topics, like retopology.


Transform
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Transform`

A surface can be edited by transforming the locations of the control points.

Move, Rotate, Scale
   Like other elements in Blender, control points can be
   moved, rotated, or scaled as described in
   :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>`.
To Sphere, Shear, Warp, Bend, Push/Pull, Warp, Randomize
   These transform tools are described in
   the :doc:`Transformations </modeling/meshes/editing/mesh/transform/index>` sections.
Move/Scale Texture Space
   Like other objects, surfaces have textures spaces which can be
   :ref:`edited <properties-texture-space-editing>`.


Mirror
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Mirror`
   :Hotkey:    :kbd:`Ctrl-M`

The *Mirror* tool is also available, behaving exactly as with
:doc:`mesh vertices </modeling/meshes/editing/mesh/mirror>`.


Snap
====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Snap`
   :Hotkey:    :kbd:`Shift-S`

:doc:`Mesh snapping </editors/3dview/controls/snapping>`
also works with control points, except for within itself (other components of the active spline).
Snapping works with 2D surfaces but points will be constrained to the local XY axes.


.. _bpy.ops.curve.spin:

Spin
====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Spin`

This tool is a bit similar to its :doc:`mesh counterpart </modeling/meshes/tools/spin>`
but with less control and options (in fact, there is none!).

It only works on selected "surfaces" made of *one U row* (and not with one V row),
so-called "surface curves", by "extruding" this "cross section" in a square pattern,
automatically adjusting the weights of control points to get a perfect circular extrusion
(this also implies closing the surface along the V axis), following exactly the same principle
as for the *NURBS Tube* or *NURBS Donut* primitives.


.. _modeling_surface_editing_duplicating:

Add Duplicate
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Add Duplicate`
   :Hotkey:    :kbd:`Shift-D`

Similar as with meshes and curves, this tool duplicates the selection.
The copy is selected and placed in move mode, so you can move it to another place.

However, with surfaces there are some selections that cannot be duplicated,
in which case they will just be placed in move mode... In fact,
only selections forming a *single* valid sub-grid are copiable; let us see this in practice:

- You can copy a single control point.
  From it, you will be able to "extrude" a "surface curve" along the U axis,
  and then extrude this unique U row along the V axis to create a real new surface.
- You can copy a single continuous part of a row (or a whole row, of course).
  This will give you a new *U row*, even if you selected (part of) a V row!
- You can copy a single whole sub-grid.

.. note::

   Trying to duplicate several valid "sub-grids" (even being single points)
   at once will not work; you will have to do it one after the other...


Split
=====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Split`
   :Hotkey:    :kbd:`Y`

The *Split* operator splits a selected segment of a surface from the rest of the surface.
This segment can then be moved or altered without affecting the other surface.
If a single control point is selected the *Split* operator will create a new singular loose control point;
leaving the previously selected control point attached to the rest of the surface.


Separate
========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Separate`
   :Hotkey:    :kbd:`P`

Surface objects that are made of multiple distinct parts can be separated into their own
objects by selecting the desired segments and using *Separate*.
Note, if there is only one surface in a surface object,
*Separate* will create a new surface object with no control points.


Toggle Cyclic
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Toggle Cyclic`
   :Hotkey:    :kbd:`Alt-C`

As in :ref:`curves <modeling-curves-toggle-cyclic>`,
surfaces can be closed (cyclic) or open. However, as surfaces are 2D,
you can control this property independently along the U and V axes.

To toggle the cyclic property of a surface along one axis,
use *Toggle Cyclic* and choose either *Cyclic U* or *Cyclic V* from the pop-up menu.
The corresponding surface's outer edges will join together to form a "closed" surface.

.. note:: Inner and Outer

   Surfaces have an "inner" and "outer" face, the first being black whereas the latter is correctly shaded.
   When you close a surface in one or two directions, you might get an entirely black object! In this case,
   just :ref:`Switch Direction <modeling_surfaces_editing_segments_switch-direction>` of the surface.


Set Spline Type
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Set Spline Type`

This feature only works for :doc:`Curves </modeling/curves/index>`.


Show/Hide
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Show/Hide`
   :Hotkey:    :kbd:`Alt-H`, :kbd:`H`, :kbd:`Shift-H`

When in *Edit Mode*, you can hide and reveal elements from the display.
You can only show or hide control points, as segments are always shown,
unless all control points of the connected surface are hidden,
in which case the surface is fully hidden.

.. seealso::

   See :ref:`object-show-hide` in *Object Mode*.


Cleanup
=======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Cleanup`

This feature only works for :doc:`Curves </modeling/curves/index>`.


Delete
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Delete`
   :Hotkey:    :kbd:`X`, :kbd:`Delete`

The selection must abide by the following rules:

- Whole rows, and only whole rows must be selected.
- Only rows along the same axis must be selected (i.e. you cannot delete both U and V rows at the same time).

Also remember that NURBS order cannot be higher than its number of control points in a given axis,
so it might decrease when you delete some control points...
Of course, when only one row remains, the surface becomes a "surface curve"; when only one point remains,
there is no more visible surface; and when all points are deleted, the surface itself is deleted.

Vertices
   This will delete the selected rows, *without* breaking the surface
   (i.e. the adjacent rows will be directly linked, joined, once the intermediary ones are deleted).
   Remember that NURBS order cannot be higher than its number of control points,
   so it might decrease when you delete some control point.
   Of course, when only one point remains, there is no more visible curve,
   and when all points are deleted, the curve itself is deleted.
Segment
   Deletes the segment that connects the selected control points and disconnects them.
Dissolve Vertices :kbd:`Ctrl-X`
   This feature only works for :doc:`Curves </modeling/curves/index>`.


Example
-------

In the image below (left), a row of control points has been selected by initially selecting
the one control point and using :ref:`bpy.ops.curve.select_row` to select the remaining
control points. Then, using `Delete`_ *Vertices*,
the selected row of control points is erased, resulting in the image below (right).

.. figure:: /images/modeling_surfaces_editing_surface_deleting.png

   Before and after.

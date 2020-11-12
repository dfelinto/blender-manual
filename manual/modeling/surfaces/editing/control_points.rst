
**************
Control Points
**************

Extrude Curve and Move
======================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Extrude Curve and Move`
   :Hotkey:    :kbd:`E`

Unlike meshes or curves, you cannot generally directly add new control points to a surface,
as you can only extend a surface by adding a whole U or V row at once.
The only exception is when working on a NURBS surface curve, i.e.
a surface with only one control point on each U or V row. In this special case,
all works exactly as with :ref:`curves <modeling-curves-extrude>`.

Most of the time, only extrusion is available. As usual, once the tool is activated
the extrusion happens immediately and you are placed into *select mode*,
ready to drag the new extruded surface to its destination.

There are two things very important to understand:

#. Surfaces are *2D* objects. So you cannot extrude anything *inside* a surface
   (e.g. "inner" row); it would not make any sense!
#. The control "grid" *must* remain "squarish",
   which means that you can only extrude a whole row, not parts of rows here and there...

To summarize, the *Extrude* tool will only work, when one and only one whole border
row is selected, otherwise nothing happens.

.. note::

   As for curves, you cannot create a new surface in your object out of nowhere.
   However, unlike for curves, there is no "cut" option allowing you to separate a surface into several parts,
   so you only can create a new surface by :ref:`Duplicating <modeling_surface_editing_duplicating>`
   an existing one, or adding a new one with the *Add* menu.


Examples
--------

Images Fig. :ref:`fig-surface-edit-select-point` to Fig. :ref:`fig-surface-edit-extruding`
show a typical extrusion along the side of a surface.

In Fig. :ref:`fig-surface-edit-select-point` and :ref:`fig-surface-edit-select-row`,
a border row of control points were highlighted by selecting a single control point,
and then using :ref:`bpy.ops.curve.select_row` to select the rest of the control points.

.. list-table::

   * - .. _fig-surface-edit-select-point:

       .. figure:: /images/modeling_surfaces_editing_control-points_selecting-point.png

          Selecting control point.

     - .. _fig-surface-edit-select-row:

       .. figure:: /images/modeling_surfaces_editing_control-points_selecting-row.png

          Select Control Point Row.

The edge is then extruded as shown in Fig. :ref:`fig-surface-edit-extruding`.
Notice how the mesh has bunched up next to the highlighted edge.
That is because the *new* extruded surface section is bunched up there as well.

.. _fig-surface-edit-extruding:

.. figure:: /images/modeling_surfaces_editing_control-points_extruding.png

   Extruding.

By moving the new section away from the area, the surface begins to "unbunch".

You can continue this process of extruding or adding new surface sections
until you have reached the final shape for your model.


Make Segment
============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Make Segment`
   :Hotkey:    :kbd:`F`

Just like :ref:`curves <modeling-curves-make-segment>`,
merging two surfaces requires that a single edge, a border row of control points,
from two separate surfaces is selected. This means that the surfaces must be part of the same object.
For example, you cannot join two surfaces while in *Object Mode* -- but you can of course,
as with any objects of the same type, :ref:`join <bpy.ops.object.join>`
two or more *Surface* objects -- they just will not be "linked" or merged in a single one.

This tool is equivalent to creating edges or faces for meshes (hence its shortcut).
The selection must contain only border rows of the same resolution
(with the same number of control points),
else Blender will try to do its best to guess what to merge with what,
or the merge will fail (either silently, or stating that ``Resolution does not match``
if rows with different number of points are selected, or that there is ``Too few selections to merge``
if you only selected points in one surface...). To select control points of different surfaces,
in the same object, you must use either box select or circle select; :kbd:`Ctrl-LMB` will not work.

So to avoid problems, you should always only select border rows with the same number of
points... Note that you can join a border U row of one surface with a border V row of another
one, Blender will automatically "invert" the axis of one surface for them to match correctly.

NURBS surface curves are often used to create objects like hulls,
as they define cross sections all along the object,
and you just have to "skin" them as described above to get a nice, smooth and harmonious shape.


Examples
--------

Fig. :ref:`fig-surface-edit-join-ready` is an example of two NURBS surface curves,
**not** NURBS curves, in *Edit Mode*, ready to be joined.
Fig. :ref:`fig-surface-edit-join-complete` is the result of joining the two curves.

.. list-table::

   * - .. _fig-surface-edit-join-ready:

       .. figure:: /images/modeling_surfaces_editing_control-points_joining-ready.png

          Joining ready.

     - .. _fig-surface-edit-join-complete:

       .. figure:: /images/modeling_surfaces_editing_control-points_joining-complete.png

          Joining complete.


Smooth
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Control Points --> Smooth`

Iteratively smooths the selected control points
by reducing the distance between neighboring control points.


Hooks
=====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Control Points --> Hooks`
   :Hotkey:    :kbd:`Ctrl-H`

:doc:`Hooks </modeling/modifiers/deform/hooks>` can be added to control one or more points with other objects.


Make Vertex Parent
==================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Control Points --> Make Vertex Parent`
   :Hotkey:    :kbd:`Ctrl-P`

You can make other selected objects :ref:`children <object-parenting>`
of one or three control points, as with mesh objects.

To select a mesh (that is in view) while editing a surface, :kbd:`Ctrl-P` click on it.
Select either one or three control points,
then :kbd:`Ctrl-LMB` the object and use :kbd:`Ctrl-P` to make a vertex parent.
Selecting three control points will make the child follow
the median point between the three vertices. An alternative would be to use
a :doc:`Child Of constraint </animation/constraints/relationship/child_of>`.
See also the :doc:`Curve modifier </modeling/modifiers/deform/curve>`.

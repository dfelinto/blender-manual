
*****
Curve
*****

This page covers the basics of curve editing.


Transform
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Transform`

A Bézier curve can be edited by transforming the locations of both control points and handles.
NURBS curve on the other hand have only control points.

Move, Rotate, Scale
   Like other elements in Blender, curve control points and handles can be
   moved, rotated, or scaled as described in
   :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>`.
To Sphere, Shear, Warp, Bend, Push/Pull, Warp, Randomize
   The transform tools are described in
   the :doc:`Transformations </modeling/meshes/editing/mesh/transform/index>` sections.
Move/Scale Texture Space
   Like other objects, curves have textures spaces which can be
   :ref:`edited <properties-texture-space-editing>`.


.. _modeling-curve-radius:

Radius
------

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Radius`
   :Menu:      :menuselection:`Curve --> Transform --> Radius`
   :Hotkey:    :kbd:`Alt-S`

The Radius allows you to directly control the width of the extrusion along the "spinal" curve.
The radius will be interpolated from point to point (you can check it with the normals).
The *Radius* of the points is set using the *Radius* transform tool. Or in the Sidebar *Transform* panel.

.. figure:: /images/modeling_curves_editing_curve_extrude-radius.png
   :align: center
   :width: 50%

   One control point radius set to zero.


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
also works with curve components.
Both control points and their handles will be affected by snapping,
except for within itself (other components of the active curve).
Snapping works with 2D curves but points will be constrained to the local XY axes.


Spin
====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Spin`

The *Spin* operator only works for one dimensional :doc:`surface </modeling/surfaces/index>` objects.
Its use for curves is currently not possible,
the full feature is documented in :ref:`Surface editing <bpy.ops.curve.spin>`.


.. _bpy.ops.curve.duplicate_move:

Add Duplicate
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Add Duplicate`
   :Hotkey:    :kbd:`Shift-D`

This tool duplicates the selected control points,
along with the curve segments implicitly selected (if any).
If only a handle is selected, the full point will be duplicated too.
The copy is selected and placed in select mode, so you can move it to another place.


.. _bpy.ops.curve.split:

Split
=====

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Split`
   :Hotkey:    :kbd:`Y`

The *Split* operator splits a selected segment of a curve from the rest of the curve.
This curve can then be moved or altered without affecting the other curve.
If a single control point is selected the *Split* operator will create a new singular loose control point;
leaving the previously selected control point attached to the rest of the curve.


.. _bpy.ops.curve.separate:

Separate
========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Separate`
   :Hotkey:    :kbd:`P`

Curve objects that are made of multiple distinct curves can be separated into their own
objects by selecting the desired segments and pressing :kbd:`P`.
Note, if there is only one curve in a Curve object,
*Separate* will create a new Curve object with no control points.


.. _bpy.ops.curve.cyclic_toggle:
.. _modeling-curves-toggle-cyclic:

Toggle Cyclic
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Toggle Cyclic`
   :Hotkey:    :kbd:`Alt-C`

This toggles between an open curve and closed curve (Cyclic).
Only curves with at least one selected control point will be closed/open.
The shape of the closing segment is based on the start and end handles for Bézier curves,
and as usual on adjacent control points for NURBS.
The only time a handle is adjusted after closing is if the handle is an *Auto* one.
Fig. :ref:`fig-curves-editing-open-close` is the same Bézier curve open and closed.

This action only works on the original starting control point or the last control point added.
Deleting a segment(s) does not change how the action applies;
it still operates only on the starting and last control points. This means that
:kbd:`Alt-C` may actually join two curves instead of closing a single curve!
Remember that when a 2D curve is closed, it creates a renderable flat face.

.. _fig-curves-editing-open-close:

.. figure:: /images/modeling_curves_editing_curve_open-closed-cyclic.png

   Open and Closed curves.


.. _bpy.ops.curve.spline_type_set:
.. _curve-convert-type:

Set Spline Type
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Set Spline Type`

*Set Spline Type* converts splines in a curve object between Bézier, NURBS, and Poly curves.
Note, this is not a "smart" conversion, i.e. Blender does not try to keep the same shape,
nor the same number of control points. For example, when converting a NURBS to a Bézier,
each group of three NURBS control points become a unique Bézier one (center point and two handles).

.. seealso::

   :ref:`object-convert-to`/from Mesh.


.. _bpy.ops.curve.reveal:
.. _bpy.ops.curve.hide:
.. _curves-show-hide:

Show/Hide
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Show/Hide`
   :Hotkey:    :kbd:`Alt-H`, :kbd:`H`, :kbd:`Shift-H`

When in *Edit Mode*, you can hide and reveal elements from the display.
You can only show or hide control points, as segments are always shown,
unless all control points of the connected curve are hidden,
in which case the curve is fully hidden.

See :ref:`object-show-hide` in *Object Mode*.
See also the :doc:`/modeling/curves/curve_display` panel.


Cleanup
=======

.. _bpy.ops.curve.decimate:

Decimate Curve
--------------

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Clean Up --> Decimate Curve`

The *Decimate Curve* operator reduces the number of control points
while trying to maintain the curves original shape.
This operator works similar to its :ref:`mesh counterpart <bpy.ops.mesh.decimate>`.

Ratio
   The percentage of control points to remove.

.. note::

   This tool can only decimate Bézier curves.


.. _bpy.ops.curve.delete:
.. _bpy.ops.curve.dissolve_verts:

Delete
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curve --> Delete...`
   :Hotkey:    :kbd:`X`, :kbd:`Delete`; :kbd:`Ctrl-X`

Options for the *Delete* pop-up menu:

Vertices
   This will delete the selected control points, *without* breaking the curve
   (i.e. the adjacent points will be directly linked, joined, once the intermediary ones are deleted).
   Remember that NURBS order cannot be higher than its number of control points,
   so it might decrease when you delete some control point.
   Of course, when only one point remains, there is no more visible curve,
   and when all points are deleted, the curve itself is deleted.
Segment
   Deletes the segment that connects the selected control points and disconnecting them.
Dissolve Vertices :kbd:`Ctrl-X`
   Deletes the selected control points, while the remaining segment is fitted to the deleted curve
   by adjusting its handles.

.. list-table::

   * - .. figure:: /images/modeling_curves_editing_curve_make-segment.png

          Before deleting.

     - .. figure:: /images/modeling_curves_editing_curve_delete-vertices.png

          Deleting vertices.

   * - .. figure:: /images/modeling_curves_editing_curve_delete-segment.png

          Deleting segment.

     - .. figure:: /images/modeling_curves_editing_curve_dissolve-vertices.png

          Dissolve vertices.

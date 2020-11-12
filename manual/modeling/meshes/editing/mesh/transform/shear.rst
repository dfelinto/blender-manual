.. _bpy.ops.transform.shear:
.. _tool-transform-shear:

*****
Shear
*****

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Mode
   :Tool:      :menuselection:`Toolbar --> Shear`
   :Menu:      :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Shear`
   :Hotkey:    :kbd:`Shift-Ctrl-Alt-S`

Shearing is a form of movement where parallel surfaces move past one another. During this transform,
movement of the selected elements will occur along the horizontal axis of the current view.
The axis location will be defined by
the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`.
Everything that is "above" this axis will move (shear)
in the same direction as your mouse pointer (but always parallel to the horizontal axis).
Everything that is "below" the horizontal axis will move in the opposite direction.

.. figure:: /images/modeling_meshes_editing_mesh_transform_shear_operator-panel.png

   Shear Offset Factor.


Tool Settings
=============

Offset
   How far items are shifted from their original location.
Axis
   Defines one axis of the imaginary shearing plane.
Axis Orthographic
   Defines the other axis of the imaginary shearing plane.
Orientation
   See :doc:`Transform Orientations </editors/3dview/controls/orientation>`.
Proportional Editing
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.

.. warning::

   The *Axis* and *Axis Orthographic* cannot be the same axis,
   else the imaginary plane is dimensionless and the objects will disappear into a point.


Usage
=====

See below for the result of using *Shear* on a number of different elements.

.. figure:: /images/modeling_meshes_editing_mesh_transform_shear_mesh.png

   The effects of a Shear transform with different Pivot Points.

The three frames of the image above show the effects of shearing
on the selected vertices when the pivot point is altered.
In middle frame, the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`
is set to *Median Point* and the mouse was moved to the left during the transform.
In right frame, the *Pivot Point* is set to the 3D cursor which is located above the mesh.
When the mouse is moved to the left during a *Shear* transform,
the selected vertices are moved to the right as they are below the horizontal axis.

.. tip:: Shear Transform Magnitude

   The magnitude of the *Shear* transform applied to the selected elements is
   directly proportional to the distance from the horizontal axis.
   i.e. the further it is away from the axis, the greater the movement.

.. figure:: /images/modeling_meshes_editing_mesh_transform_shear_objects.png

   The effects of a Shear transform on objects with different Pivot Points.

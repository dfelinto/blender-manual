.. _bpy.ops.transform.push_pull:
.. _tool-transform-push_pull:

*********
Push/Pull
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Modes
   :Tool:      :menuselection:`Toolbar --> Shrink/Flatten --> Push/Pull`
   :Menu:      :menuselection:`Object/Mesh --> Transform --> Push/Pull`

.. figure:: /images/modeling_meshes_editing_mesh_transform_push-pull_operator-panel.png
   :align: right

   Push/Pull distance.

*Push/Pull* will move the selected elements (objects, vertices, edges or faces)
closer together (Push) or further apart (Pull).
Specifically, each element is moved towards or away from the center by the same distance.
This distance is controlled by moving the mouse up (Push) or down (Pull), numeric input or through slider control.


Usage
=====

See below for the result of using *Push/Pull* on a number of different elements.

.. figure:: /images/modeling_meshes_editing_mesh_transform_push-pull_objects-equidistant.png

   Equidistant objects being pushed together.

.. figure:: /images/modeling_meshes_editing_mesh_transform_push-pull_objects-random.png

   Random objects being pushed together.

.. figure:: /images/modeling_meshes_editing_mesh_transform_push-pull_vertices.png

   Push (middle) vertices around the 3D cursor compared to Scale (right).

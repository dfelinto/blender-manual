.. _bpy.ops.mesh.knife_project:

*************
Knife Project
*************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Knife Project`

Knife projection is a non-interactive tool where you can use objects to cookie-cut into
the mesh rather than hand drawing the line.

This works by using the outlines of other selected objects in Edit Mode to cut into the mesh
along the view axis, resulting geometry inside the cutters outline will be selected.

Outlines can be wire or boundary edges.

To use Knife Project, first while in *Object Mode*, select the "cutting object"
then add to that selection with :kbd:`Shift-LMB` the "object to be cut".
Now, enter *Edit Mode* and press *Knife Project* (found in the Toolbar).

.. seealso::

   :doc:`3D Viewport Alignment </editors/3dview/navigate/align>` to adjust the projection axis.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_text-before.jpg
          :width: 320px

          Before projecting from a text object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_text-after.jpg
          :width: 320px

          Resulting knife projection.

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_mesh-before.jpg
          :width: 320px

          Before projecting from a mesh object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_mesh-after.jpg
          :width: 320px

          Resulting knife projection (extruded after).

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_curve-before.png
          :width: 320px

          Before projecting from a 3D curve object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_curve-after.jpg
          :width: 320px

          Resulting knife projection (extruded after).

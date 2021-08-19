.. _bpy.ops.mesh.knife_project:

*************
Knife Project
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Knife Project`

Knife projection is a non-interactive tool where you can use objects to cookie-cut into
the mesh rather than hand drawing the line.
This works by using the outline of selected objects that are out of edit mode to cut the
mesh along the view axis of objects that are in edit mode,
resulting geometry inside the cutters outline will be selected.
Outlines can be a wireframe or boundary edges (i.e. the unconnected edges of a mesh).

.. note::

   The primitives, being manifold objects, do not have wireframe or boundary edges.
   In the case of the cube, deleting the top face will result in cutting edges.

   :ref:`Select Non-Manifold <bpy.ops.mesh.select_non_manifold>`
   (Wire, Boundaries) will highlight the cutting edges of mesh objects.

To use Knife Project, in *Edit Mode*, select the cutting object (Ctrl + Select)
and choose :menuselection:`Mesh --> Knife Project`.

.. hint::

   :doc:`3D Viewport Alignment </editors/3dview/navigate/align>` to adjust the projection axis.


Options
=======

Cut Through
   Projects the cut through the entire mesh.


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


Known Limitations
=================

When cutting multiple meshes in Edit Mode at once,
geometry from these meshes does not occlude separate mesh objects behind them.

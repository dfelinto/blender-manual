.. _bpy.ops.mesh.knife_project:

*************
Knife Project
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Knife Project`

Knife projection is a non-interactive tool where you can use objects to cookie-cut into
one or more meshes rather than hand drawing the line. The outline of selected objects
that *are not* in Edit Mode are used to cut the meshes along the view axis of objects
that *are* in Edit Mode. Afterwards the resulting geometry inside the cutters outline will be selected.
Outlines can be a wireframe or boundary edges (i.e. the unconnected edges of a mesh), as well as 
Curve objects.

Keep in mind that Knife Project works from the current view's perspective.  For best results, make sure
to rotate your view to exactly the position you require before using this tool.  Orthographic views such
as Right, Front, and Top are commonly used for more predictable results.

.. note::

   The primitives, being manifold objects, do not have wireframe or boundary edges.
   In the case of the cube, deleting the top face will result in cutting edges.
   :ref:`Select Non-Manifold <bpy.ops.mesh.select_non_manifold>`
   (Wire, Boundaries) will highlight the cutting edges of mesh objects.

   In general, for flat shapes, you will usually want to select "Faces Only" from the delete menu to leave 
   behind only edges.

To use Knife Project, first in *Object Mode* select the objects to be cut,
then switch to *Edit Mode* and select the cutting objects in the Outliner (:kbd:`Ctrl-LMB`),
and finally choose :menuselection:`Mesh --> Knife Project`.

.. hint::

   :doc:`3D Viewport Alignment </editors/3dview/navigate/align>` to adjust the projection axis.


Options
=======

Cut Through
   Projects the cut through the entire mesh, including back faces not currently visible.


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

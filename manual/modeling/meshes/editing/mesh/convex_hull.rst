.. _bpy.ops.mesh.convex_hull:

***********
Convex Hull
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Convex Hull`

The Convex Hull operator takes a point cloud as input and outputs a convex hull surrounding those vertices.
If the input contains edges or faces that lie on the convex hull, they can be used in the output as well.
This operator can be used as a bridge tool as well.

.. figure:: /images/modeling_meshes_editing_mesh_convex-hull_example.png

   Input mesh, point cloud, and Convex Hull result.

Delete Unused
   Removes vertices, edges, and faces that were selected, but not used as part of the hull.
   Note that vertices and edges that are used
   by other edges and faces not part of the selection will not be deleted.

Use Existing Faces
   Where possible, use existing input faces that lie on the hull.
   This allows the convex hull output to contain n-gons rather than triangles
   (or quads if the *Join Triangles* option is enabled).

Make Holes
   Delete edges and faces in the hull that were part of the input too.
   Useful in cases like bridging to delete faces between the existing mesh and the convex hull.

Join Triangles
   Joins adjacent triangles into quads.
   Has all the same properties as the *Tris to Quads* operator (angle limit, compare UVs, etc.).
Max Face Angle, Max Shape Angle, Compare
   See :ref:`mesh-faces-tristoquads`.

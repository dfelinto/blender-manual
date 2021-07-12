
********
Clean Up
********

These tools are to help cleanup degenerate geometry and fill in missing areas of a mesh.


.. _bpy.ops.mesh.decimate:

Decimate Geometry
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Decimate Geometry`

The Decimate Geometry tool allows you to reduce
the vertex/face count of a mesh with minimal shape changes.

Ratio
   Ratio of triangles to reduce to.
Vertex Group
   Use the active vertex group as an influence.

   Weight
      Strength of the vertex group.
   Invert
      Inverts the vertex group.
Symmetry
   Maintain symmetry on either the *X*, *Y*, or *Z* axis.

.. seealso::

   This tool works similar to the :doc:`Decimate Modifier </modeling/modifiers/generate/decimate>`.


.. _bpy.ops.mesh.fill_holes:

Fill Holes
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Fill Holes`

This tool can take a large selection and detect the holes in the mesh, filling them in.

This is different from the face creation operator in three important respects:

#. Holes are detected, so there is no need to manually find and select the edges around the holes.
#. Holes can have a limit for the number of sides (so only quads or tris are filled in for example).
#. Mesh data is copied from surrounding geometry (UVs, vertex colors, multi-res, all layers),
   since manually creating this data is very time-consuming.


.. _bpy.ops.mesh.face_make_planar:

Make Planar Faces
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Make Planar Faces`

The *Make Planar Faces* iteratively flattens faces.
This can happen with faces over three vertices and
it is a common convention that faces should be kept planar.

Factor
   Distance to move the vertices each iteration.
Iterations
   Number of times to repeat the operation.


.. _bpy.ops.mesh.vert_connect_nonplanar:

Split Non-Planar Faces
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Split Non-Planar Faces`

This tool avoids ambiguous areas of geometry by splitting non-flat faces when they are bent beyond
a given limit.


.. _bpy.ops.mesh.vert_connect_concave:

Split Concave Faces
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Split Concave Faces`

This tool can be used to convert any :term:`Concave Face` to convex
by splitting the concave into two or more convex faces.


.. _bpy.ops.mesh.delete_loose:

Delete Loose
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Delete Loose`

This tool removes disconnected vertices and edges (optionally faces).


.. _bpy.ops.mesh.dissolve_degenerate:

Degenerate Dissolve
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Degenerate Dissolve`

This tool collapses / removes geometry which you typically will not want.

- Edges with no length.
- Faces with no areas (faces on a point or thin faces).
- Face corners with no area.


.. _bpy.ops.mesh.remove_doubles:

Merge by Distance
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Merge by Distance`,
               :menuselection:`Context Menu --> Merge by Distance`

Merge by Distance is a useful tool to simplify a mesh by merging the selected vertices that
are closer than a specified distance to each other.
An alternative way to simplify a mesh is to use the :doc:`Decimate Modifier </modeling/modifiers/generate/decimate>`.

Merge Distance
   Sets the distance threshold for merging vertices.
Unselected
   Allows vertices in the selection to be merged with unselected vertices.
   When disabled, selected vertices will only be merged with other selected ones.

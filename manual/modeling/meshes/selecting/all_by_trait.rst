
*******************
Select All by Trait
*******************

.. _bpy.ops.mesh.select_non_manifold:

Non-Manifold
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Non-Manifold`

Selects the :term:`Non-manifold` geometry of a mesh.
This entry is available when editing a mesh, in Vertex and Edge selection modes only.

Extend
   Lets you extend the current selection.
Wire
   Selects all the edges that do not belong to any face.
Boundaries
   Selects edges in boundaries and holes.
Multiple Faces
   Selects edges that belong to three or more faces.
Non Contiguous
   Selects edges that belong to exactly two faces with opposite normals.
Vertices
   Selects vertices that belong to *wire* and *multiple face* edges,
   isolated vertices, and vertices that belong to non-adjoining faces.


.. _bpy.ops.mesh.select_loose:

Loose Geometry
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Loose Geometry`

This selection depends on the currently selected :ref:`Selection Modes <bpy.types.ToolSettings.mesh_select_mode>`;
In vertex and edge selection mode it selects all vertices or edges that do not form part of a face.
In face selection mode it selects all faces that do not share edges with other faces.


.. _bpy.ops.mesh.select_interior_faces:

Interior Faces
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Interior Faces`

Selects faces where all edges have more than two faces.


.. _bpy.ops.mesh.select_face_by_sides:

Faces by Sides
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Faces by Sides`

Selects all faces that have a specified number of edges.


.. _bpy.ops.mesh.select_ungrouped:

Ungrouped Vertices
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Ungrouped Vertices`

Selects all vertices which are not part of
a :doc:`vertex group </modeling/meshes/properties/vertex_groups/index>`.

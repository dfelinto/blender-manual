.. _bpy.ops.mesh.polybuild:
.. _tool-mesh-poly-build:

**********
Poly Build
**********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Poly Build`

The *Poly Build* tool uses many built operators in an interactive way to add, delete, or move geometry.
This is extremely useful for retopology.


Tool Settings
=============

Create Quads
   Automatically split edges in triangles to maintain the quad topology.


Controls
========

Add Geometry :kbd:`Ctrl-LMB`
   Vertices or faces can be created by moving the cursor close to
   an element and using the hotkey to add a vertex or face.
   The tool first tries to create a face, however, if not enough geometry
   exists to create a face it will try to extrude a vertex to the cursor.
   When creating a face, the face can be previewed by holding :kbd:`Ctrl`.
Delete Mesh Elements :kbd:`Shift-LMB`
   Vertices, edges, and faces will be deleted by hovering over the element and using the hotkey.
   Elements with two or more connected elements will be :ref:`Dissolved <bpy.ops.mesh.dissolve>`.
   The element you are trying to delete will be highlighted in red while holding :kbd:`Ctrl`.
Moving Vertices :kbd:`LMB`
   Vertices can be moved by hovering over the vertex and
   using to hotkey to grab and move the vertex to the desired location.
   The vertex you are trying to move will be highlighted in blue while hovering over it.
Extruding Edges :kbd:`LMB`
   Edges can be :doc:`extruded </modeling/meshes/editing/edge/extrude_edges>`
   by moving the cursor close to an edge and using the hotkey to extrude the edge to the desired location.
   The edge you are trying to extrude will be highlighted in blue while hovering over it.

.. tip::

   It is useful to enable :ref:`vertex snapping <transform-snap-element>`
   and use :ref:`bpy.ops.mesh.remove_doubles` while tweaking vertices to combine them.

.. _bpy.ops.mesh.rip_move:
.. _tool-mesh-rip_region:

************
Rip Vertices
************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Rip Vertices`
   :Hotkey:    :kbd:`V`

Rip creates a "hole" in the mesh by making a copy of selected vertices and edges,
still linked to the neighboring non-selected vertices,
so that the new edges are borders of the faces on one side, and the old ones,
borders of the faces on the other side of the rip.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_before.png
          :width: 260px

          Selected vertex.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_after.png
          :width: 260px

          Hole created after using rip on vertex.

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_edges-before.png
          :width: 260px

          Edges selected.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_edges-after.png
          :width: 260px

          Result of rip with edge selection.

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_complexselection-before.png
          :width: 260px

          A complex selection of vertices.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_complexselection-after.png
          :width: 260px

          Result of rip operation.


Limitations
===========

Rip will only work when edges and/or vertices are selected.
Using the tool when a face is selected (explicitly or implicitly), will return an error
message *"Cannot perform ripping with faces selected this way"*.
If your selection includes edges or vertices that are not "between" two faces :term:`Manifold`,
it will also fail with the message *"No proper selection or faces include"*.

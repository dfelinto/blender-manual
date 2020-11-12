.. _bpy.ops.mesh.split:

*****
Split
*****

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split`
   :Hotkey:    :kbd:`Alt-M`


Selection
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split --> Selection`
   :Hotkey:    :kbd:`Y`

Splits (disconnects) the selection from the rest of the mesh.
The border edge to any non-selected elements are duplicated.

Note that the "copy" is left exactly at the same position as the original, so you must move it
:kbd:`G` to see it clearly...


.. _bpy.ops.mesh.edge_split:

Faces by Edges
==============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split --> Faces by Edges`

*Faces by Edges* is similar to the *Rip* tool. When two or more touching interior edges,
or a border edge is selected, a hole will be created,
and the selected edges will be duplicated to form the border of the hole.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_split_edges-before.png
          :width: 320px

          Selected edges.

     - .. figure:: /images/modeling_meshes_editing_mesh_split_edges-after.png
          :width: 320px

          Adjacent face moved to reveal hole left by split.


Faces & Edges by Vertices
=========================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split --> Faces & Edges by Vertices`

*Faces & Edges by Vertices* is similar to *Faces by Edges* except that
it also splits the vertices of the adjacent connecting edges.
This has the same functionality as manually ripping all faces and edges away from a vertex.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_split_faces-before.png
          :width: 320px

          Before.

     - .. figure:: /images/modeling_meshes_editing_mesh_split_faces-after.png
          :width: 320px

          After (also moving edges away).

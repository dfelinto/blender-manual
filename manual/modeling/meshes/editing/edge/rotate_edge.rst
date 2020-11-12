.. _modeling-meshes-editing-edges-rotate:
.. _bpy.ops.mesh.edge_rotate:

***********
Rotate Edge
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Rotate Edge CW / Rotate Edge CCW`

Rotating an edge clockwise (CW) or counterclockwise (CCW) spins an edge between two faces around their vertices.
This is very useful for restructuring a mesh's topology.

The tool operates on selected edges or the shared edge between selected faces.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_face-mode1.png
          :width: 320px

          Two adjacent faces selected.

     - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_face-mode2.png
          :width: 320px

          Selected edge rotated.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_flip-before.png
          :width: 320px

          Selected edge.

     - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_flip-after.png
          :width: 320px

          Edge, rotated CW.

.. warning::

   To rotate an edge based on faces you must select adjacent face pairs,
   otherwise Blender notifies you with an error message,
   *"Could not find any select edges that can be rotated"*. Using either *Rotate Edge CW*
   or *Rotate Edge CCW* will produce exactly the same results as if you had
   selected the common edge.

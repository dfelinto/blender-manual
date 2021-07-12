.. _bpy.ops.mesh.vert_connect:

********************
Connect Vertex Pairs
********************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Connect Vertex Pairs`

This tool connects selected vertices by creating edges between them and splitting the face.
It can be used on many faces at once.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-pairs_before.png
          :width: 180px

          Vertices before connecting.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-pairs_after.png
          :width: 180px

          After connecting vertices.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-pairs_after-faces.png
          :width: 180px

          Resulting face pair.

The main difference between this tool and :doc:`/modeling/meshes/editing/vertex/connect_vertex_path`
is that this tool ignores the selection order and connects all selected vertices that share a face.

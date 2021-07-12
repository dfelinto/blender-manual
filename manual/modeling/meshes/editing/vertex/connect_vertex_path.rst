.. _bpy.ops.mesh.vert_connect_path:

*******************
Connect Vertex Path
*******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Connect Vertex Path`
   :Shortcut:  :kbd:`J`

This tool connects vertices in the order they are selected, splitting the faces between them.
When there are only two vertices selected, a cut will be made across unselected faces,
a bit like the Knife tool; but this is limited to straight cuts across connected faces.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_pair-before.png

          Two disconnected vertices.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_pair-after.png

          Result of connecting.

Running a second time will connect the first/last endpoints.
When many vertices are selected, faces will be split by their selected vertices.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_multi-before.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_multi-after.png

          After.

Vertices not connected to any faces will create edges,
so this can be used as a way to quickly connect isolated vertices too.

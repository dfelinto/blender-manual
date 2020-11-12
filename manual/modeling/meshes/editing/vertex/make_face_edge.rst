.. _bpy.ops.mesh.edge_face_add:

***************************
New Edge/Face from Vertices
***************************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> New Edge/Face from Vertices`
   :Hotkey:    :kbd:`F`

This is a context-sensitive tool which creates geometry by filling in the selection.
When only two vertices are selected it will create an edge, otherwise it will create faces.

The typical use case is to select vertices and press :kbd:`F`,
yet Blender also supports creating faces from different selections to help to
quickly build up geometry.


Methods
=======

The following methods are used automatically depending on the context.


Isolated Vertices
-----------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_verts-simple-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_verts-simple-after.png
          :width: 200px

          After.


Isolated Edges
--------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_edge-simple-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_edge-simple-after.png
          :width: 200px

          After.


N-gon from Edges
----------------

When there are many edges Blender will make an n-gon.
Note that, this does not support holes,
to support holes you need to use the :ref:`modeling-meshes-editing-fill` Faces tool.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_ngon-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_ngon-after.png
          :width: 200px

          After.


Mixed Vertices/Edges
--------------------

Existing edges are used to make the face as well as an extra vertex.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_mix-simple-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_mix-simple-after.png
          :width: 200px

          After.


Edge-Net
--------

Sometimes you may have many connected edges without interior faces.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_net-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_net-after.png
          :width: 200px

          After.


Point Cloud
-----------

When there are many isolated vertices,
Blender will calculate the edges for an n-gon.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_cloud-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_cloud-after.png
          :width: 200px

          After.


Single Vertex Selection
-----------------------

With a single vertex selected on a boundary,
the face will be created along the boundary,
this saves manually selecting the other two vertices.
Notice this tool can run multiple times to continue creating faces.

.. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_create-boundary.png

.. seealso::

   For other ways to create faces see:

   - :ref:`Fill <modeling-meshes-editing-fill>`
   - :ref:`Grid Fill <modeling-meshes-editing-grid-fill>`
   - :ref:`Bridge Edge Loops <modeling-meshes-editing-bridge-edge-loops>`


.. _modeling-mesh-make-face-edge-dissolve:

Dissolve Existing Faces
-----------------------

When you have a region of existing faces, creating a face on this selection
will remove the shared vertices and edges, creating a single face.

This is simply a convenience for accessing :ref:`bpy.ops.mesh.dissolve_faces`.

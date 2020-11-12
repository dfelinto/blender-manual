.. _bpy.ops.transform.vert_slide:
.. _tool-mesh-vertex-slide:

**************
Slide Vertices
**************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Slide Vertices`
   :Hotkey:    :kbd:`Shift-V`

Vertex Slide will transform a vertex along one of its adjacent edges.
Use :kbd:`Shift-V` to activate tool.
The nearest selected vertex to the mouse cursor will be the control one.
Move the mouse along the direction of the desired edge to specify the vertex position.
Then press :kbd:`LMB` to confirm the transformation.

Even :kbd:`E`
   By default, the offset value of the vertices is a percentage of the edges length along which they move.
   When Even mode is active, the vertices are shifted by an absolute value.
Flipped :kbd:`F`
   When Flipped is active, vertices move the same distance from adjacent vertices,
   instead of moving from their original position.
Clamp :kbd:`Alt` or :kbd:`C`
   Toggle clamping the slide within the edge extents.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_slide-vertices_example-1.png
          :width: 200px

          Selected vertex.

     - .. figure:: /images/modeling_meshes_editing_vertex_slide-vertices_example-2.png
          :width: 200px

          Positioning vertex interactively.

     - .. figure:: /images/modeling_meshes_editing_vertex_slide-vertices_example-3.png
          :width: 200px

          Repositioned vertex.

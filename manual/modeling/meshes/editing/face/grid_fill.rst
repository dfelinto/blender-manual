.. _bpy.ops.mesh.fill_grid:
.. _modeling-meshes-editing-grid-fill:

*********
Grid Fill
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Grid Fill`

*Grid Fill* uses a pair of connected edge loops or a single, closed edge loop to fill in a grid
that follows the surrounding geometry.

The best predictable result can be achieved if you select two opposite edge loops
with an equal number of vertices. When a single, closed edge loop is selected,
the Span/Offset options allows you to adjust the way two opposite edge loops
are detected from one closed edge loop.

Span
   Specifies the number of columns in the grid.
Offset
   Defines the vertex that is considered to be the corner of the grid,
   by default, it's the active vertex. The Offset allows you to rotate the grid lines.
Simple Blending
   Use a simple interpolation algorithm to generate grid vertices from boundary loops,
   which does not tries to maintain the shape,
   useful for flat surfaces or times when keeping the shape gives odd results.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_grid-fill_before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_face_grid-fill_after.png
          :width: 320px

          Grid Fill result.

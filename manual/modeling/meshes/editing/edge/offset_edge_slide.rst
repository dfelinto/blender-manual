.. _bpy.ops.mesh.offset_edge_loops_slide:

*****************
Offset Edge Slide
*****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Edge --> Offset Edge Slide`
   :Hotkey:    :kbd:`Shift-Ctrl-R`

Add two edge loops on either side of selected loops.

Cap Endpoint
   Extends the loop by creating triangles at endpoints.
Factor
   Location of the loop relative to the center loop and the outside edge loops.
Even
   Only available for single edge loops.
   This matches the shape of the edge loop to one of the adjacent edge loops.
   (See :ref:`Edge Slide tool <modeling-meshes-editing-edge-slide>` for details.)
Flipped
   When Even is enabled, this flips the target edge loop to match.
   (See :ref:`Edge Slide tool <modeling-meshes-editing-edge-slide>` for details.)
Clamp
   Clamp within the edge extents.
Correct UVs
   Correct UV coordinates when transforming.

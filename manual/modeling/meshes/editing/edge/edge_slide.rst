.. _bpy.ops.transform.edge_slide:
.. _modeling-meshes-editing-edge-slide:
.. _tool-mesh-edge_slide:

**********
Edge Slide
**********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Slide`

Slides one or more edges across adjacent faces with a few restrictions involving the selection
of edges (i.e. the selection *must* define a valid loop, see below).

Even :kbd:`E`
   Forces the edge loop to match the shape of the adjacent edge loop.
   You can flip to the opposite vertex using :kbd:`F`. Use :kbd:`Alt-Wheel` to change the control edge.
Flipped :kbd:`F`
   When Even mode is active, this flips between the two adjacent edge loops the active edge loop will match.
Clamp :kbd:`Alt` or :kbd:`C`
   Toggle clamping the slide within the edge extents.
Factor
   Determines the amount of slide performed.
   Negative values correspond to slides toward one face, while positive ones, refer to the other one.
   It is also displayed in the 3D Viewport footer.
Mirror Editing
   Lets you propagate the operation to the symmetrical elements of the mesh (if present, in local X direction).
Correct UVs
   Corrects the corresponding UV coordinates, if these exist, to avoid image distortions.


Usage
=====

By default, the position of vertices on the edge loop move as a percentage of the distance
between their original position and the adjacent edge loop, regardless of the edges' lengths.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_before.png
          :width: 320px

          Selected edge loop.

     - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_after.png
          :width: 320px

          Repositioned edge loop.


Even Mode
---------

*Even* mode keeps the shape of the selected edge loop the same as one of the edge loops adjacent to it,
rather than sliding a percentage along each perpendicular edge.

In *Even* mode, the tool shows the position along the length of the currently selected edge
which is marked in yellow, from the vertex that has an enlarged red marker.
Movement of the sliding edge loop is restricted to this length. As you move the mouse
the length indicator in the header changes showing where along the length of the edge you are.

To change the control edge that determines the position of the edge loop,
use the :kbd:`Alt-Wheel` to scroll to a different edge.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_even.png
          :width: 320px

          Even Mode enabled.

     - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_even-flip.png
          :width: 320px

          Even Mode with Flip enabled.

Moving the mouse moves the selected edge loop towards or away from the start vertex,
but the loop line will only move as far as the length of the currently selected edge,
conforming to the shape of one of the bounding edge loops.


Limitations & Workarounds
-------------------------

There are restrictions on the type of edge selections that can be operated upon.
Invalid selections are:

Loop Crosses Itself
   This means that the tool could not find any suitable faces that were adjacent to the selected edge(s).
   An example that shows this is selecting two edges that share the same face.
   A face cannot be adjacent to itself.
Multiple Edge Loops
   The selected edges are not in the same edge loop, which means they do not have a common edge.
   You can minimize this error by always selecting edges end-to-end or in a "chain".
   If you select multiple edges just make sure they are connected.
   This will decrease the possibility of getting looping errors.
Border Edges
   When a single edge was selected in a single-sided object.
   An edge loop cannot be found because there is only one face.
   Remember, edge loops are loops that span two or more faces.

A general rule of thumb is that if multiple edges are selected they should be connected end-to-end
such that they form a continuous chain. This is *literally* a general rule because you
can still select edges in a chain that are invalid because some of the edges in the chain are
in different edge loops.

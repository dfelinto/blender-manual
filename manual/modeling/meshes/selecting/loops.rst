
************
Select Loops
************

.. _bpy.ops.mesh.loop_multi_select:

Edge Loops
==========

.. reference::

   :Mode:      Edit Mode (Vertex or Edge select mode)
   :Menu:      :menuselection:`Select --> Select Loops --> Edge Loops`
   :Shortcut:  :kbd:`Alt-LMB`, or :kbd:`Shift-Alt-LMB` for modifying existing selection.

Holding :kbd:`Alt` while selecting an edge selects a loop of edges that are connected in
a line end-to-end, passing through the edge under the mouse pointer.
Holding :kbd:`Shift-Alt` while clicking adds to the current selection.

.. note:: *Vertex* mode

   In *Vertex* select mode, you can also select edge loops, by using the same shortcuts,
   and clicking on the *edges* (not on the vertices).

.. figure:: /images/modeling_meshes_selecting_loops_edge-loops.png

   Longitudinal and latitudinal edge loops.

The left sphere shows an edge that was selected longitudinally. Notice how the loop is open.
This is because the algorithm hit the vertices at the poles and is terminated
because the vertices at the pole connect to more than four edges. However,
the right sphere shows an edge that was selected latitudinally and has formed a closed loop.
This is because the algorithm hit the first edge that it started with.


Edge Loops (All Boundaries)
---------------------------

All boundary edges can be selected by performing a second loop select action on a boundary edge.

This can be useful for selecting boundaries for meshes that include triangles and n-gons,
where loop select would not otherwise select the full boundary.

.. figure:: /images/modeling_meshes_selecting_loops_edge-boundary-loops.png

   The second loop select action is shown on the right.


.. _modeling-meshes-selecting-face-loops:

Face Loops
==========

.. reference::

   :Mode:      Edit Mode (Face or Vertex select modes)
   :Shortcut:  :kbd:`Alt-LMB` or :kbd:`Shift-Alt-LMB` for modifying existing selection.

In face select mode, holding :kbd:`Alt` while selecting an *edge* selects a loop of
faces that are connected in a line end-to-end, along their opposite edges.

In vertex select mode,
the same can be accomplished by using :kbd:`Ctrl-Alt` to select an edge,
which selects the face loop implicitly.

.. figure:: /images/modeling_meshes_selecting_loops_face-loops.png

   Face loop selection.

This face loop was selected by clicking with :kbd:`Alt-LMB` on an edge,
in *face* select mode.
The loop extends perpendicular from the edge that was selected.

.. figure:: /images/modeling_meshes_selecting_loops_face-loops-vertex.png

   :kbd:`Alt` versus :kbd:`Ctrl-Alt` in vertex select mode.

A face loop can also be selected in *Vertex* select mode.
Technically :kbd:`Ctrl-Alt-LMB` will select an *Edge Ring*,
however, in *Vertex* select mode, selecting an *Edge Ring* implicitly
selects a *Face Loop* since selecting opposite edges of a face implicitly selects
the entire face.


.. _modeling-meshes-selecting-edge-rings:

Edge Rings
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Loops --> Edge Rings`
   :Shortcut:  :kbd:`Ctrl-Alt-LMB`

In *Edge* select mode, holding :kbd:`Ctrl-Alt`
while selecting an edge (or two vertices) selects a sequence of edges that are not connected,
but on opposite sides to each other continuing along a :doc:`face loop </modeling/meshes/structure>`.

As with edge loops, you can also select edge rings based on current selection,
using either :menuselection:`Select --> Select Loops --> Edge Rings`.

.. note:: *Vertex* mode

   In *Vertex* select mode, you can use the same shortcuts when *clicking on the edges* (not on the vertices),
   but this will directly select the corresponding face loop...

.. _fig-mesh-select-advanced-loop-ring:

.. figure:: /images/modeling_meshes_selecting_loops_edge-ring.png

   A selected edge loop, and a selected edge ring.

In Fig. :ref:`fig-mesh-select-advanced-loop-ring` the same edge was clicked on,
but two different "groups of edges" were selected, based on the different tools.
One is based on edges during computation and the other is based on faces.

.. note:: Convert Selection to Whole Faces

   If the edge ring selection happened in Edge Select Mode, switching to Face Select Mode will erase the selection.

   This is because none of those faces had all its (four) edges selected,
   just two of them.

   Instead of selecting the missing edges manually or by using :kbd:`Shift-Alt-LMB` twice,
   it is easier to first switch to Vertex Select Mode, which will kind of "flood" the selection.
   A subsequent switch to Face Select Mode will then properly select the faces.


.. _bpy.ops.mesh.loop_to_region:

Select Loop Inner-Region
========================

.. reference::

   :Mode:      Edit Mode (Edge select mode)
   :Menu:      :menuselection:`Select --> Select Loops --> Select Loop Inner-Region`

*Select Loop Inner-Region* selects all faces that are inside a closed loop of edges.
While it is possible to use this operator in *Vertex* and *Face* selection modes, results may be unexpected.
Note that if the selected loop of edges is not closed,
then all connected edges on the mesh will be considered inside the loop.

.. figure:: /images/modeling_meshes_selecting_loops_inner-region1.png

   Loop to Region.

.. figure:: /images/modeling_meshes_selecting_loops_inner-region2.png

   This tool handles multiple loops fine, as you can see.

.. figure:: /images/modeling_meshes_selecting_loops_inner-region3.png

   This tool handles "holes" just fine as well.


.. _bpy.ops.mesh.region_to_loop:

Select Boundary Loop
====================

.. reference::

   :Mode:      Edit Mode (Edge select mode)
   :Menu:      :menuselection:`Select --> Select Loops --> Select Boundary Loop`

*Select Boundary Loop* does the opposite of *Select Loop Inner-Region*,
based on all regions currently selected, it selects only the edges at the border (contour) of these islands.
It can operate in any select mode, but when in *Face* mode it will switch to *Edge* select mode after running.

All this is much more simple to illustrate with examples:

.. figure:: /images/modeling_meshes_selecting_loops_boundary-loop.png

   Select Boundary Loop does the opposite and forces into Edge Select Mode.

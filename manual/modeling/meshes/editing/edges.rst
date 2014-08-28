
..    TODO/Review: {{review|}} .

Make Edge/Face
**************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Edges --> Make Edge/Face`
   | Hotkey:   :kbd:`F`


It will create an edge or some faces, depending on your selection. We have already discussed this tool in the :doc:`editing basics page </modeling/meshes/editing/basics#edge_and_face_creation>`.


Set Edge Attributes
*******************

Edges can have several different attributes that affect how certain other tools affect the
mesh.


Mark Seam and Clear Seam
========================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Mark Seam/Clear Seam` (or the same options in :guilabel:`Edge Specials` menu)
   | Hotkey:   :kbd:`ctrl-E-pad1` and :kbd:`ctrl-E-pad2`


Seams are a way to create separations, "islands", in UV maps. See the :doc:`UVTexturing section </textures/mapping/uv>` for more details. These commands set or unset this flag for selected edges.


Mark Sharp and Clear Sharp
==========================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Mark Seam/Clear Seam` (or the same options in :guilabel:`Edge Specials` menu)
   | Hotkey:   :kbd:`ctrl-E-pad1` and :kbd:`ctrl-E-pad2`


The :guilabel:`Sharp` flag is used by the :doc:`EdgeSplit modifier </modifiers/generate/edge_split>`, which is part of the smoothing technics. As seams, it is a property of edges, and these commands set or unset it for selected ones.


Adjust Bevel Weight
===================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Adjust Bevel Weight`
   | Hotkey:   :kbd:`ctrl-shift-E`


This edge property (a value between **0.0** and **1.0**) is used by the :doc:`Bevel modifier </modifiers/generate/bevel>` to control the bevel intensity of the edges. This command enters an interactive mode (a bit like transform tools), where by moving the mouse (or typing a value with the keyboard) you can set the (average) bevel weight of selected edges.


Crease SubSurf
==============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Crease SubSurf`
   | Hotkey:   :kbd:`shift-E`


This edge property (a value between **0.0** and **1.0**) is used by the
:doc:`Subsurf modifier </modifiers/generate/subsurf>` to control the sharpness of the edges in the subdivided mesh.
This command enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard) you can set the (average)
crease value of selected edges.
To clear the crease edge property, enter a value of **-1**.


Edge Slide
**********

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Slide Edge` (or the same option in :guilabel:`Edge Specials` menu)
   | Hotkey:   :menuselection:`[ctrl][E] --> [pad6]`


Slides one or more edges across adjacent faces with a few restrictions involving the selection
of edges (i.e. the selection must make sense, see below.)

:guilabel:`Even`:kbd:`E`
   Forces the edge loop to match the shape of the adjacent edge loop. You can flip to the opposite vertex using :kbd:`F`. Use :kbd:`Alt-wheel` to change the control edge.
:guilabel:`Flip` :kbd:`F`
   When Even mode is active, this flips between the two adjacent edge loops the active edge loop will match

:kbd:`lmb` confirms the tool, and :kbd:`rmb` or :kbd:`Esc` cancels.

This tool has a factor,
which is displayed in the 3D View footer and in the :guilabel:`Tool Shelf`
(after confirmation).
A numerical value between ``-1`` and ``1`` can be entered for precision.

In *Proportional* mode, :kbd:`wheel`,
or :kbd:`←` and :kbd:`→` changes the selected edge for calculating a proportion.
Unlike *Percentage* mode, *Proportional*

Holding :kbd:`ctrl` or :kbd:`shift` control the precision of the sliding.
:kbd:`ctrl` snaps movement to 10% steps per move and :kbd:`shift` snaps movement
to 1% steps. The default is 5% steps per move.


Usage
=====

By default, the position of vertices on the edge loop move as a percentage of the distance
between their original position and the adjacent edge loop, regardless of the edges' lengths.


.. figure:: /images/EdgeSlide1.jpg
   :width: 250px
   :figwidth: 250px

   selected edge loop


.. figure:: /images/EdgeSlide2.jpg
   :width: 250px
   :figwidth: 250px

   Repositioned edge loop


Even mode
---------

*Even* mode keeps the shape of the selected edge loop the same as one of the edge loops adjacent to it, rather than sliding a percentage along each perpendicular edge.

In *Even* mode, the tool shows the position along the length of the currently selected edge
which is marked in yellow, from the vertex that as an enlarged red marker.
Movement of the sliding edge loop is restricted to this length. As you move the mouse the
length indicator in the header changes showing where along the length of the edge you are.

To change the control edge that determines the position of the edge loop,
use the :kbd:`Alt-wheel` to scroll to a different edge.


.. figure:: /images/EdgeSlide3.jpg
   :width: 250px
   :figwidth: 250px

   Even mode enabled


.. figure:: /images/EdgeSlide4.jpg
   :width: 250px
   :figwidth: 250px

   Even mode with flip enabled


Moving the mouse moves the selected edge loop towards or away from the start vertex,
but the loop line will only move as far as the length of the currently selected edge,
conforming to the shape of one of the bounding edge loops.


Limitations & Workarounds
-------------------------

There are restrictions on the type of edge selections that can be operated upon.
Invalid selections are:

Loop crosses itself
   This means that the tool could not find any suitable faces that were adjacent to the selected edge(s). (*Loop crosses*) is an example that shows this by selecting two edges that share the same face. A face cannot be adjacent to itself.

Multiple edge loops
   The selected edges are not in the same edge loop, which means they don't have a common edge. You can minimize this error by always selecting edges end to end or in a "Chain". If you select multiple edges just make sure they are connected. This will decrease the possibility of getting looping errors.

Border Edge
   When a single edge was selected in a single sided object. An edge loop can not be found because there is only one face. Remember, edge loops are loops that span two or more faces.

A general rule of thumb is that if multiple edges are selected they should be connected end to
end such that they form a continuous chain. This is *literally* a general rule because you
can still select edges in a chain that are invalid because some of the edges in the chain are
in different edge loops.


Rotate Edge
***********

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Rotate Edge CW / Rotate Edge CCW`
   | Hotkey:   :menuselection:`[ctrl][E] --> Rotate Edge CW`   and :menuselection:`[ctrl][E] --> Rotate Edge CCW`


Rotating an edge clockwise or counter-clockwise spins an edge between two faces around their
vertices. This is very useful for restructuring a mesh's topology.
The tool can operate on one explicitly selected edge,
or on two selected vertices or two selected faces that implicitly share an edge between them.


.. figure:: /images/EdgeFlip1.jpg
   :width: 250px
   :figwidth: 250px

   selected edge


.. figure:: /images/EdgeFlip2.jpg
   :width: 250px
   :figwidth: 250px

   Edge, rotated CW


Using Face Selection
====================

To rotate an edge based on faces you must select two faces, (*Adjacent selected faces*),
otherwise Blender notifies you with an error message, "\ ``ERROR:
Could not find any select edges that can be rotated`` ". Using either :guilabel:`Rotate
Edge CW` or :guilabel:`Rotate Edge CCW` will produce exactly the same results as if you had
selected the common edge shown in (*Selected edge rotated CW and CCW.*).


Delete Edge Loop
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (:guilabel:`Vertex` or :guilabel:`Edge` select modes)
   | Menu:     :menuselection:`Mesh --> Delete --> Edge Loop`
   | Hotkey:   :menuselection:`[X]/[Del] --> [g]`


:guilabel:`Delete Edge Loop` allows you to delete a selected edge loop if it is between two other edge loops. This will create one face-loop where two previously existed.


.. admonition:: Note
   :class: note

   The :guilabel:`Edge Loop` option is very different to the :guilabel:`Edges` option, even if you use it on edges that look like an edge loop. Deleting an edge loop merges the surrounding faces together to preserve the surface of the mesh. By deleting a chain of edges, the edges are removed, deleting the surrounding faces as well. This will leave holes in the mesh where the faces once were.


Example
=======

The selected edge loop on the UV Sphere has been deleted and the faces have been merged with
the surrounding edges. If the edges had been deleted by choosing :guilabel:`Edges` from the
(:guilabel:`Erase` *Menu*)
there would be an empty band of deleted faces all the way around the sphere instead.


.. figure:: /images/DeleteEdgeLoop1.jpg
   :width: 300px
   :figwidth: 300px

   Selected edge loop


.. figure:: /images/DeleteEdgeLoop2.jpg
   :width: 300px
   :figwidth: 300px

   Edge loop deleted


Collapse
********

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Delete --> Edge Collapse`
   | Hotkey:   :menuselection:`[alt][M] --> [pad3]`


This takes a selection of edges and for each edge, merges its two vertices together.
This is useful for taking a ring of edges and collapsing it,
removing the face loop it ran through.


.. figure:: /images/Collapse1.jpg
   :width: 300px
   :figwidth: 300px

   Selected edge ring


.. figure:: /images/Collapse2.jpg
   :width: 300px
   :figwidth: 300px

   Edge ring collapsed


Edge Split
**********

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Edges --> Edge Split`
   | Hotkey:   :menuselection:`[Ctrl][E] --> Edge Split`


:guilabel:`Edge split` is similar to the rip tool. When two or more touching interior edges, or a border edge is selected when using :guilabel:`Edge split`, a hole will be created, and the selected edges are duplicated to form the border of the hole


.. figure:: /images/EdgeSplit1.jpg
   :width: 300px
   :figwidth: 300px

   Selected edges


.. figure:: /images/EdgeSplit2.jpg
   :width: 300px
   :figwidth: 300px

   Adjacent face moved to reveal hole left by split


Bridge Edge Loops
*****************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Edges --> Bridge Edge Loops`


:guilabel:`Bridge Edge Loops` connects multiple edge loops with faces.

Simple example showing 2 closed edge loops.


.. figure:: /images/mesh_bridge_simple_before.jpg
   :width: 300px
   :figwidth: 300px

   Input


.. figure:: /images/mesh_bridge_simple_after.jpg
   :width: 300px
   :figwidth: 300px

   Bridge result


Example of bridge tool between edge loops with different numbers of vertices.


.. figure:: /images/mesh_bridge_uneven_before.jpg
   :width: 300px
   :figwidth: 300px

   Input


.. figure:: /images/mesh_bridge_uneven_after.jpg
   :width: 300px
   :figwidth: 300px

   Bridge result


Example using the bridge tool to punch holes in face selections and connect them.


.. figure:: /images/mesh_bridge_faces_before.jpg
   :width: 300px
   :figwidth: 300px

   Input


.. figure:: /images/mesh_bridge_faces_after.jpg
   :width: 300px
   :figwidth: 300px

   Bridge result


Example showing how bridge tool can detect multiple loops and loft them in one step.


.. figure:: /images/mesh_bridge_multi_before.jpg
   :width: 300px
   :figwidth: 300px

   Input


.. figure:: /images/mesh_bridge_multi_after.jpg
   :width: 300px
   :figwidth: 300px

   Bridge result


Example of the subdivision option and surface blending with UV's.


.. figure:: /images/mesh_bridge_advanced_before.jpg
   :width: 300px
   :figwidth: 300px

   Input


.. figure:: /images/mesh_bridge_advanced_after.jpg
   :width: 300px
   :figwidth: 300px

   Bridge result



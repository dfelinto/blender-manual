
..    TODO/Review: {{review|partial=X|text= expand advanced selection tools|im=examples}} .

Advanced Selection
==================

The select menu in edit mode contains additional tool for selecting components:

:guilabel:`Mirror`
   Select mesh items at the mirrored location.
:guilabel:`Linked` :kbd:`ctrl-L`
   Selects all components that are connected to the current selection.
:guilabel:`Select Random`
   Selects a random group of vertices, edges, or faces, based on a percentage value.
:guilabel:`Checker Deselect`
   Deselect alternating faces, to create a checker like pattern.
:guilabel:`Select Every N Number of Vertices`
   Selects vertices that are multiples of N.
:guilabel:`Select Sharp Edges`

   This option will select all edges that are between two faces forming an angle less than a given value, which is asked you *via* a small pop-up dialog. The lower is this angle limit, the sharper will be the selected edges. At **180- **\ , **all** "manifold" (see below) edges will be selected.

:guilabel:`Linked Flat Faces` (\ :kbd:`Ctrl-Shift-Alt-F`\ )
   Select connected faces based on a threshold of the angle between them. This is useful for selecting faces that are planar.
:guilabel:`Select Non Manifold` (\ :kbd:`Ctrl-Shift-Alt-M`\ )
   Selects vertices that are not completely bound by geometry, including border edges, floating edges, and orphan vertices. Only available in Vertex and Edge mode.
:guilabel:`Interior Faces`
   Select faces where all edges have more than 2 faces.
:guilabel:`Side of Active`
   Selects all data on the mesh in a single axis
:guilabel:`Select Faces by Sides`
   Selects all faces that have a specified number of edges.
:guilabel:`Loose Geometry`
   Select all vertices or edges that do not form part of a face.


Select Similar
--------------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> Similar...`
   | Hotkey:   :kbd:`shift-G`


Select components that have similar attributes to the ones selected,
based on a threshold that can be set in tool properties after activating the tool.
Tool options change depending on the selection mode:

:guilabel:`Vertex Selection Mode`\ :
   :guilabel:`Normal`
      Selects all vertices that have normals pointing in similar directions to those currently selected.
   :guilabel:`Amount of Adjacent Faces`
      Selects all vertices that have the same number of faces connected to them.
   :guilabel:`Vertex Groups`
      Selects all vertices in the same :doc:`vertex group <modeling/meshes/vertex_groups>`\ .
   :guilabel:`Amount of connecting edges`
      Selects all vertices that have the same number of edges connected to them.


:guilabel:`Edge Selection Mode`\ :
   :guilabel:`Length`
      Selects all edges that have a similar length as those already selected.
   :guilabel:`Direction`
      Selects all edges that have a similar direction (angle) as those already selected.
   :guilabel:`Amount of Faces Around an Edge`
       Selects all edges that belong to the same number of faces.
   :guilabel:`Face Angles`
      Selects all edges that are between two faces forming a similar angle, as with those already selected.
   :guilabel:`Crease`
       Selects all edges that have a similar :guilabel:`Crease` value as those already selected. The :guilabel:`Crease` value is a setting used by the :doc:`Subsurf Modifier <modifiers/generate/subsurf>`\ .
   :guilabel:`Bevel`
      Selects all edges that have the same :guilabel:`Bevel Weight` as those already selected.
   :guilabel:`Seam`
      Selects all edges that have the same :guilabel:`Seam` state as those already selected. :guilabel:`Seam` is a true/false setting used in :doc:`UV-texturing <textures/mapping/uv>`\ .
   :guilabel:`Sharpness`
      Selects all edges that have the same :guilabel:`Sharp` state as those already selected. :guilabel:`Sharp` is a true/false setting (a flag) used by the :doc:`EdgeSplit Modifier <modifiers/generate/edge_split>`\ .


:guilabel:`Face Selection Mode`\ :
   :guilabel:`Material`
      Selects all faces that use the same material as those already selected.
   :guilabel:`Image`
      Selects all faces that use the same UV-texture as those already selected (see :doc:`UV-texturing <textures/mapping/uv>` pages).
   :guilabel:`Area`
      Selects all faces that have a similar area as those already selected.
   :guilabel:`Polygon Sides`
      Selects all faces that have the same number of edges.
   :guilabel:`Perimeter`
      Selects all faces that have a similar perimeter as those already selected.
   :guilabel:`Normal`
      Selects all faces that have a similar normal as those selected. This is a way to select faces that have the same orientation (angle).
   :guilabel:`Co-planar`
      Selects all faces that are (nearly) in the same plane as those selected.


Selecting Loops
---------------

You can easily select loops of components:


Edge Loops and Vertex Loops
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode → :guilabel:`Vertex` or :guilabel:`Edge` select mode
   | Menu:     :menuselection:`Select --> Edge Loop` or :menuselection:`Mesh --> Edges --> Edge Loop`
   | Hotkey:   :kbd:`alt-rmb` or :kbd:`ctrl-E` → :menuselection:`Edge Loop`


Holding :kbd:`alt` while selecting an edge selects a loop of edges that are connected in
a line end to end, passing through the edge under the mouse pointer.
Holding :kbd:`alt-shift` while clicking adds to the current selection.

Edge loops can also be selected based on an existing edge selection,
using either :menuselection:`Select --> Edge Loop`\ ,
or the :guilabel:`Edge Loop Select` option of the :guilabel:`Edge Specials` menu
(\ :kbd:`ctrl-E`\ ).


.. admonition:: :guilabel:`Vertex` mode
   :class: note

   In :guilabel:`Vertex` select mode, you can also select edge loops, by using the same hotkeys, *and clicking on the edges* (not on the vertices).


.. figure:: /images/Broken-Manual-Part-II-EdgeF.jpg

   Longitudinal and latitudinal edge loops.


The left sphere shows an edge that was selected longitudinally. Notice how the loop is open.
This is because the algorithm hit the vertices at the poles and terminated because the
vertices at the pole connect to more than four edges. However,
the right sphere shows an edge that was selected latitudinally and has formed a closed loop.
This is because the algorithm hit the first edge that it started with.


Face Loops
~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode → :guilabel:`Face` or :guilabel:`Vertex` select modes
   | Hotkey:   :kbd:`alt-rmb`


In face select mode, holding :kbd:`alt` while selecting an **edge** selects a loop of
faces that are connected in a line end to end, along their opposite edges.

In vertex select mode,
the same can be accomplished by using :kbd:`ctrl-alt` to select an edge,
which selects the face loop implicitly.


.. figure:: /images/Manual-Part-II-EdgeFaceTools-FaceLoopSel.jpg

   Face loop selection.


This face loop was selected by clicking with :kbd:`alt-rmb` on an edge,
in :guilabel:`face` select mode.
The loop extends perpendicular from the edge that was selected.


.. figure:: /images/Manual-Part-II-EdgeFace-LoopingEdge-Algors-Vertex-Select.jpg

   [alt] versus [ctrl][alt] in vertex select mode.


A face loop can also be selected in :guilabel:`Vertex` select mode.
Technically :kbd:`ctrl-alt-rmb` will select an :guilabel:`Edge Ring`\ ,
however in :guilabel:`Vertex` select mode, selecting an :guilabel:`Edge Ring` implicitly
selects a :guilabel:`Face Loop` since selecting opposite edges of a face implicitly selects
the entire face.


Edge Ring
~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode → :guilabel:`Edge` select mode
   | Menu:     :menuselection:`Select --> Edge Ring` or :menuselection:`Mesh --> Edges --> Edge Ring`
   | Hotkey:   :kbd:`ctrl-alt-rmb` or :kbd:`ctrl-E` → :menuselection:`Select --> Edge Ring`


In :guilabel:`Edge` select mode, holding :kbd:`ctrl-alt` while selecting an edge selects a sequence of edges that are not connected, but on opposite sides to each other continuing along a :doc:`face loop <modeling/meshes/mesh_structures>`\ .

As with edge loops, you can also select edge rings based on current selection,
using either :menuselection:`Select --> Edge Ring`\ ,
or the :guilabel:`Edge Ring Select` option of the :guilabel:`Edge Specials` menu
(\ :kbd:`ctrl-E`\ ).


.. admonition:: :guilabel:`Vertex` mode
   :class: note

   In :guilabel:`Vertex` select mode, you can use the same hotkeys when *clicking on the edges* (not on the vertices), but this will directly select the corresponding face loop…


.. figure:: /images/Manual-Part-II-EdgeFace-LoopingEdge-Algors-Select.jpg

   A selected edge loop, and a selected edge ring.


In (\ *A selected edge loop, and a selected edge ring*\ ),
the same edge was clicked on but two different "groups of edges" were selected,
based on the different commands.
One is based on edges during computation and the other is based on faces.


Path Selection
~~~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :kbd:`ctrl-rmb` and the menu item :menuselection:`Select` → :guilabel:`Shortest Path`


.. figure:: /images/Select_face_path.jpg
   :width: 200px
   :figwidth: 200px

   Select a face or vertex path with [ctrl][rmb]


Selects all geometry along the shortest path from the active vertex/edge/face to the one which
was selected.


Loop Inner-Region
~~~~~~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode → :guilabel:`Edge` select mode
   | Menu:     :menuselection:`Select --> Select Loop Inner-Region` or :menuselection:`Mesh --> Edges --> Select Loop Inner-Region`
   | Hotkey:   :kbd:`ctrl-E` → :menuselection:`Select Loop Inner-Region`


:guilabel:`Select Loop Inner-Region` selects all edges that are inside a closed loop of edges. While it is possible to use this operator in  :guilabel:`Vertex` and :guilabel:`Face` selection modes, results may be unexpected. Note that if the selected loop of edges is not closed, then all connected edges on the mesh will be considered inside the loop.


.. figure:: /images/Mesh.loop.select1.jpg
   :width: 400px
   :figwidth: 400px

   Loop to Region.


.. figure:: /images/Mesh.loop.select3.jpg
   :width: 400px
   :figwidth: 400px

   This tool handles multiple loops fine, as you can see.


.. figure:: /images/Mesh.loop.select5.jpg
   :width: 400px
   :figwidth: 400px

   This tool handles "holes" just fine as well.


Boundary Loop
~~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode → :guilabel:`Edge` select mode
   | Menu:     :menuselection:`Select --> Select Boundary Loop` or :menuselection:`Mesh --> Edges --> Select Boundary Loop`
   | Hotkey:   :kbd:`ctrl-E` → :menuselection:`Select Boundary Loop`


:guilabel:`Select Boundary Loop` is the "logical inverse" of :guilabel:`Select Loop Inner-Region`\ , based on all regions currently selected, it selects only the edges at the border of these regions. It can operate in any select mode, but will always switch to :guilabel:`Edge` select mode when run.

All this is much more simple to illustrates with examples:


.. figure:: /images/Mesh.region.select1.jpg
   :width: 400px
   :figwidth: 400px

   Select Boundary Loop does the opposite and forces into Edge Select Mode


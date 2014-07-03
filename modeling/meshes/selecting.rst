

..    TODO/Review: {{review|}} .


Selecting Mesh Components
=========================

There are many ways to select elements, and it depends on what :guilabel:`Mesh Select Mode`
you are in as to what selection tools are available.
First we will go through these modes and after that a look is taken at basic selection tools.


Selection Modes
---------------


Select Mode Header Widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure:: /images/25-Manual-Modeling-Meshes-Selection-mode-buttons.jpg
   :width: 190px
   :figwidth: 190px

   Edit mode selection buttons


In :guilabel:`Edit mode` there are three different selection modes.
You can enter the different modes by selecting one of the three buttons in the toolbar.

Using the buttons you can also use more than one selection mode at a time by
:kbd:`shift-lmb` clicking the buttons.

:guilabel:`Vertices`
   Selected vertices are drawn in orange, unselected vertices in black, and the active or last selected vertex in white.

:guilabel:`Edges`
   In this mode the vertices are not drawn. Instead the selected edges are drawn in orange, unselected edges black, and the active or last selected edge in white.

:guilabel:`Faces`
   In this mode the faces are drawn with a selection point in the middle which is used for selecting a face. Selected faces and their selection point are drawn in orange, unselected faces are drawn in black, and the active or last selected face is highlighted in white.

Almost all modification tools are available in all three mesh selection modes.
So you can :guilabel:`Rotate`\ , :guilabel:`Scale`\ , :guilabel:`Extrude`\ , etc. in all modes. Of
course rotating and scaling a *single* vertex will not do anything useful without setting
the pivot point to another location, so some tools are more or less applicable in some modes.


.. admonition:: Note
   :class: note

   The three selection mode buttons are only visible in :guilabel:`Edit mode`\ . The colors of selected, unselected and active components depend entirely on the current theme. Black, orange and white are from the default theme.


Select Mode Pop-up
~~~~~~~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :kbd:`ctrl-tab`


.. figure:: /images/25-Manual-Modeling-Meshes-Selection-mode.jpg
   :width: 152px
   :figwidth: 152px

   Mesh Select Mode menu


You can also choose a selection mode with the pop-up menu

:menuselection:`Select Mode --> Vertices`
   Press :kbd:`ctrl-tab` and select :guilabel:`Vertices` from the pop-up menu, or press :kbd:`ctrl-tab`\ :kbd:`1`\ .

:menuselection:`Select Mode --> Edges`
   Press :kbd:`ctrl-tab` and select :guilabel:`Edges` from the pop-up menu, or press :kbd:`ctrl-tab`\ :kbd:`2`\ .

:menuselection:`Select Mode --> Faces`
   Press :kbd:`ctrl-tab` and select :guilabel:`Faces` from the pop-up menu, or press :kbd:`ctrl-tab`\ :kbd:`3`\ .


Switching select mode
~~~~~~~~~~~~~~~~~~~~~

When switching modes in an "ascendant" way (i.e. from simpler to more complex), from
:guilabel:`Vertices` to :guilabel:`Edges` and from :guilabel:`Edges` to :guilabel:`Faces`\ ,
the selected parts will still be selected if they form a complete element in the new mode.

For example, if all four edges in a face are selected,
switching from :guilabel:`Edges` mode to :guilabel:`Faces` mode will keep the face selected.
All selected parts that do not form a complete set in the new mode will be unselected.

Hence, switching in a "descendant" way (i.e. from more complex to simpler),
all elements defining the "high-level" element (like a face) will be selected
(the four vertices or edges of a quadrangle, for example).

By holding :kbd:`ctrl` when selecting a higher selection mode,
all elements touching the current selection will be added,
even if the selection does not form a complete higher element.

See (\ :guilabel:`Vertices` *mode example*\ ), (\ :guilabel:`Edges` *mode example*\ ),
(\ :guilabel:`Faces` *mode example*\ ) and (\ *Mixed mode example*\ )
for examples of the different modes.


+-----------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/Manual-Part-II-EditModeVerticeModeExample.jpg|.. figure:: /images/Manual-Part-II-EditModeEdgeModeExample.jpg +
+                                                                 |                                                               +
+   Vertices mode example.                                        |   Edges mode example.                                         +
+-----------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/Manual-Part-II-EditModeFaceModeExample.jpg   |.. figure:: /images/Manual-Part-II-EditModeMixedModeExample.jpg+
+                                                                 |                                                               +
+   Faces mode example.                                           |   Mixed mode example.                                         +
+-----------------------------------------------------------------+---------------------------------------------------------------+


Selection Tools
---------------

The select menu in edit mode contains tools for selecting components.
These are described in more detail in the following pages.

:guilabel:`Border Select`
   Enables a rectangular region for selection
:guilabel:`Circle Select`
   Enables a circular shaped region for selection

:guilabel:`(De)select All` :kbd:`A`
   Select all or none of the mesh components.
:guilabel:`Invert Selection` :kbd:`ctrl-I`
   Selects all components that are not selected, and deselect currently selected components.
:guilabel:`Select Random`
   Selects a random group of vertices, edges, or faces, based on a percentage value.
:guilabel:`Checker Deselect`
   Deselect alternating faces, to create a checker like pattern.
:guilabel:`Select Sharp Edges`

   This option will select all edges that are between two faces forming an angle less than a given value, which is asked you *via* a small pop-up dialog. The lower is this angle limit, the sharper will be the selected edges. At **180- **\ , **all** "manifold" (see below) edges will be selected.

:guilabel:`Linked Flat Faces` (\ :kbd:`Ctrl-Shift-Alt-F`\ )
   Select connected faces based on a threshold of the angle between them. This is useful for selecting faces that are planar.
:guilabel:`Interior Faces`
   Select faces where all edges have more than 2 faces.

:guilabel:`Side of Active`
   Selects all data on the mesh in a single axis

:guilabel:`Select Faces by Sides`
   Selects all faces that have a specified number of edges.

:guilabel:`Select Non Manifold` (\ :kbd:`Ctrl-Shift-Alt-M`\ )
   Selects vertices that are not completely bound by geometry, including border edges, floating edges, and orphan vertices. Only available in Vertex mode.

:guilabel:`Loose`
   Select all vertices or edges that do not form part of a face.
:guilabel:`Similar`
   Select components based on how similar certain properties are to it.

:guilabel:`More` :kbd:`ctrl-num+`
   Propagates selection by adding components that are adjacent to selected elements.
:guilabel:`Less` :kbd:`ctrl-num-`
   Deselects components that form the bounds of the current selection

:guilabel:`Mirror`
   Select mesh items at the mirrored location.
:guilabel:`Linked` :kbd:`ctrl-L`
   Selects all components that are connected to the current selection.

:guilabel:`Vertex Path`
   Selects a vertex path between two selected vertices
:guilabel:`Edge Loop`
   Selects a loop of edges from a selected edge
:guilabel:`Edge Ring`
   Selects edges parallel to a selected edge in the same ring of faces
:guilabel:`Loop Inner-Region`
   Converts a closed selection of edges to the region of faces it encloses
:guilabel:`Boundary Loop`
   Converts a selection of faces to the ring of edges enclosing it



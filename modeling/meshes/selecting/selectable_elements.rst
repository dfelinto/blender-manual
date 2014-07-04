
Selectable Elements
===================

As we have seen in the :doc:`mesh structure page <modeling/meshes/mesh_structures>`, meshes are made of different element types (even though they are all inter-related: in a way, they are different "views", "representations", of the same basic data…), "vertices", "edges" and "faces".

Hence, you can select different parts of a mesh using one of these three types.
There is one key point to understand here: *when you select a type of element (e.g.
some edges), you* **implicitly** *select the other types of corresponding elements (e.g.
all vertices defining those edges, as well as faces fully defined by these same edges)*.
This is very important, as some tools only work on vertices, edges and/or faces:
if you use a "face" tool with a selection of vertices,
only the faces defined by these vertices will be affected.

In general, you will only select one type of element at a time, depending on the "select mode" you are using. However, you can successively add different elements to a same selection, switching between these select modes (see
FIXME(TODO: Internal Link;
[[#Selected elements after switching select mode|below]]
) for what is selected after switching select mode), or even use a "combined" select mode, also described below.


Select Modes
------------

You have two ways to switch between select modes:


Select Mode popup
~~~~~~~~~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :kbd:`ctrl-tab`


In :guilabel:`Edit` mode there are three different select modes for meshes; see
(:guilabel:`Select Mode` *menu*).


.. figure:: /images/Manual-Part-II-EditModeMenu_2.5.jpg

   Select Mode menu.


:menuselection:`Select Mode --> Vertices`
   Press :kbd:`ctrl-tab` and select :guilabel:`Vertices` from the popup menu, or press :kbd:`ctrl-tab`:kbd:`pad1`. The selected vertices are drawn in yellow and unselected vertices are drawn in a pink colour.
:menuselection:`Select Mode --> Edges`
   Press :kbd:`ctrl-tab` and select :guilabel:`Edges` from the popup menu, or press :kbd:`ctrl-tab`:kbd:`pad2`. In this mode the vertices are not drawn. Instead the selected edges are drawn in yellow and unselected edges are drawn in a black colour.
:menuselection:`Select Mode --> Faces`
   Press :kbd:`ctrl-tab` and select :guilabel:`Faces` from the popup menu, or press :kbd:`ctrl-tab`:kbd:`pad3`. In this mode the faces are drawn with a selection point in the middle which is used for selecting a face. Selected faces are drawn in yellow with the selection point in orange, unselected faces are drawn in black.

Almost all modification tools are available in all three modes. So you can :guilabel:`Rotate`,
:guilabel:`Scale`, :guilabel:`Extrude`, etc. in all modes.
Of course rotating and scaling a *single* vertex will not do anything useful,
so some tools are more or less applicable in some modes.


Select Mode header widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    Header of the :guilabel:`3D View`


.. figure:: /images/Manual-Part-II-EditModeButtonsLabeled_2.5.jpg

   Edit mode select mode buttons.


You can also enter the different modes by selecting one of the three buttons in the toolbar;
see (:guilabel:`Edit` *mode select buttons*).

Using the buttons you can also enter "\ **mixed** " or "combined" mode by
:kbd:`shift-lmb` clicking the buttons. This will allow you to select vertices,
edges and/or faces at the same time!


.. admonition:: Note
   :class: note

   The "Mode Selection" buttons are only visible for meshes in :guilabel:`Edit` mode.


Selected elements after switching select mode
---------------------------------------------

When switching modes in an "ascendant" way (i.e. from simpler to more complex), from
:guilabel:`Vertices` to :guilabel:`Edges` and from :guilabel:`Edges` to :guilabel:`Faces`,
the selected parts will still be selected if they form a complete set in the new mode.
For example, if all four edges in a face are selected,
switching from :guilabel:`Edges` mode to :guilabel:`Faces` mode will keep the face selected.
All selected parts that do not form a complete set in the new mode will be unselected.

Hence, switching in a "descendant" way (i.e. from more complex to simpler),
all elements defining the "high-level" element (like a face) will be selected
(the four vertices or edges of a quadrangle, for example).

See (:guilabel:`Vertices` *mode example*), (:guilabel:`Edges` *mode example*),
(:guilabel:`Faces` *mode example*) and (*Mixed mode example*)
for examples of the different modes.


+---------------------------------------------------------------------+-------------------------------------------------------------------+
+.. figure:: /images/Manual-Part-II-EditModeVerticeModeExample_2.5.jpg|.. figure:: /images/Manual-Part-II-EditModeEdgeModeExample_2.5.jpg +
+   :width: 300px                                                     |   :width: 300px                                                   +
+   :figwidth: 300px                                                  |   :figwidth: 300px                                                +
+                                                                     |                                                                   +
+   none Vertices mode example.                                       |   Edges mode example.                                             +
+---------------------------------------------------------------------+-------------------------------------------------------------------+
+.. figure:: /images/Manual-Part-II-EditModeFaceModeExample_2.5.jpg   |.. figure:: /images/Manual-Part-II-EditModeMixedModeExample_2.5.jpg+
+   :width: 300px                                                     |   :width: 300px                                                   +
+   :figwidth: 300px                                                  |   :figwidth: 300px                                                +
+                                                                     |                                                                   +
+   Faces mode example.                                               |   Mixed mode example.                                             +
+---------------------------------------------------------------------+-------------------------------------------------------------------+



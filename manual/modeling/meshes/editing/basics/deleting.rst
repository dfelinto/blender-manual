
..    TODO/Review: {{review|im = examples}} .


Deleting and Merging
********************

These tools can be used to remove components.


Delete
======

Delete (:kbd:`X` or :kbd:`Del`)
   Deletes selected vertices, edges, or faces. This operation can also be limited to:

   Vertices
      Delete all vertices in current selection, removing any faces or edges they are connected to.
   Edges
      Deletes any edges in the current selection. Removes any faces that the edge shares with it.
   Faces
      Removes any faces in current selection.
   Only Edges & Faces
      Limits the operation to only selected edges and adjacent faces.
   Only faces
      Removes faces, but edges within face selection are retained.
   Edge Collapse
      Collapses edges into single vertices. This can be used to remove a loop of faces.
   Edge Loop
      Deletes an edge loop.  If the current selection is not an edge loop, this operation does nothing.


Dissolve
========

Dissolve operations are also accessed from the delete menu. Instead of removing the geometry,
which may leave holes that you have to fill in again, dissolve will remove the geometry and fill in the surrounding geometry.

Dissolve
   Removes selected geometry, but keeps surface closed, effectively turning the selection into a single n-gon. Dissolve works slightly different based on if you have edges, faces or vertices selected. You can add detail where you need it, or quickly remove it where you don't.
Limited Dissolve
   Limited Dissolve reduces detail on planar faces and linear edges with an adjustable angle threshold.


.. figure:: /images/Bmesh_limited-dissolve.jpg
   :width: 400px
   :figwidth: 400px

   Example showing the how Limited Dissolve can be used.


   Face Split - dissolve option.
      When dissolving vertices into surrounding faces, you can often end up with very large, uneven ngons.
The face split option limits dissolve to only use the corners of the faces connected to the vertex.


.. figure:: /images/Bmesh_dissolve_face_split.jpg
   :width: 500px
   :figwidth: 500px

   Dissolve Face Split option. Left - the input, middle - regular dissolve, right - Face Split enabled


Convert Triangles to Quads
==========================

:guilabel:`Tris to Quads` :kbd:`alt-J`
This takes adjacent tris and removes the shared edge to create a quad.
This tool can be performed on a selection of multiple triangles.

This same action can be done on a selection of just 2 tris,
by selecting them and using the shortcut :kbd:`F`, to create a face.


Unsubdivide
===========

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Edges --> Unsubdivide`
   | Hotkey:   :menuselection:`[Ctrl][E] --> Unsubdivide`


Unsubdivide functions as the reverse of subdivide by attempting to remove edges that were the
result of a subdivide operation.
If additional editing has been done after the subdivide operation,
unexpected results may occur.

Iterations
   How many subdivisions to remove.


Merging
=======

Merging Vertices
----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Vertices --> Merge...`, :menuselection:`Specials --> Merge` or :menuselection:`Vertex Specials --> Merge`
   | Hotkey:   :kbd:`alt-M`


This tool allows you to merge all selected vertices into an unique one, deleting all others.
You can choose the location of the surviving vertex in the menu this tool pops up before
executing:

At First
   Only available in :guilabel:`Vertex` select mode, it will place the remaining vertex at the location of the first one selected.

At Last
   Only available in :guilabel:`Vertex` select mode, it will place the remaining vertex at the location of the last one selected (the active one).

At Center
   Available in all select modes, it will place the remaining vertex at the center of the selection.

At Cursor
   Available in all select modes, it will place the remaining vertex at the 3D Cursor.

Collapse
   This is a special option, as it might let "live" more than one vertex. In fact, you will have as many remaining vertices as you had "islands" of selection (i.e. groups of linked selected vertices). The remaining vertices will be positioned at the center of their respective "islands". It is also available *via* the :menuselection:`Mesh --> Edges --> Collapse` menu option...

Merging vertices of course also deletes some edges and faces. But Blender will do everything
it can to preserve edges and faces only partly involved in the reunion.


AutoMerge Editing
-----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> AutoMerge Editing`


The :guilabel:`Mesh` menu as a related toggle option: :guilabel:`AutoMerge Editing`.
When enabled,
as soon as a vertex moves closer to another one than the :guilabel:`Limit` setting
(:guilabel:`Mesh Tools` panel, see below), they are automatically merged.


Remove Doubles
--------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Editing` context → :guilabel:`Mesh Tools`
   | Menu:     :menuselection:`Mesh --> Vertices --> Remove Doubles`, :menuselection:`Specials --> Remove Doubles` or :menuselection:`Vertex Specials --> Remove Doubles`
   | Hotkey:   :menuselection:`[W] --> [4]` or :menuselection:`[ctrl][V] --> Remove doubles`


Remove Doubles is a useful tool to simplify a mesh by merging vertices that are closer than a specified distance to each other. An alternate way to simplify a mesh is to use the :doc:`Decimate modifier </modifiers/generate/decimate>`.

Merge Distance
   Sets the distance threshold for merging vertices, in Blender units.
Unselected
   Allows vertices in a selection to be merged with unselected vertices. When disabled, selected vertices will only be merged with other selected ones.



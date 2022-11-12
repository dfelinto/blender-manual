
*******************
Snap Utilities Line
*******************

Installation
============

- This add-on is bundled with Blender.
- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Snap Utilities Line to enable the script.


Make Line
=========

Creates edges and operationally faces by snapping to mesh elements.
When moving the cursor close to a face, edge or vertex, the cursor is snapped to the highlighted element.
It can also be snapped to center or perpendicular of an edge.
After selecting the first point you can specify the length of the line by typing a value and
confirming with :kbd:`Return`.

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Make Line`


Controls
========

**Axis Constrain** :kbd:`X`, :kbd:`Y`, :kbd:`Z`
  Constraint the cursor movement on the  X, Y, or Z axis.

**Edge Constrain** :kbd:`Shift`
   Constraint the cursor movement towards an edge.

   For the constrain work, you need to have your cursor over an edge.

   This is useful for creating parallel lines.

**Confirm Input** :kbd:`Return`
   Confirms the numerical value written in the header for the line length.

**Cut Line** :kbd:`LMB`
   Starts the lines drawing.

**Confirm** :kbd:`RMB`
   Single click stops the lines drawing.

   Double-clicks completes the tool's execution.

**Cancel** :kbd:`Esc`
   Cancel the operation.


Options
=======

**Create Faces**
   A face is created when:

   **1.** It detects the drawing of a closed segment.

   .. figure:: /images/addons_mesh_snap_utilities-creating-faces-1.jpg
      :align: center

   **2.** The last vertex of the segment binds to an edge that connects another vertex of the segment.

   .. figure:: /images/addons_mesh_snap_utilities-creating-faces-2.jpg
      :align: center

   **3.** It detects an isolated edge loop.

   .. figure:: /images/addons_mesh_snap_utilities-creating-faces-3.jpg
      :align: center

   **4.** We redraw existing edges to match the conditions mentioned above.

   .. figure:: /images/addons_mesh_snap_utilities-creating-faces-4.jpg
      :align: center


.. reference::

   :Category: Mesh
   :Description: Tool that allows accurate modeling through its own snapping system
   :Location: :menuselection:`3D Viewport --> Tools --> Line Tool`
   :File: mesh_snap_utilities_line folder
   :Author: Germano Cavalcante

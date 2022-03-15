
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

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Tool:      :menuselection:`Toolbar --> Make Line`

Creates edges and operationally faces by snapping to mesh elements.
When moving the cursor close to a face, edge or vertex, the cursor is snapped to the highlighted element.
It can also be snapped to center or perpendicular of an edge.
After selecting the first point you can specify the length of the line by typing a value and
confirming with :kbd:`Return`.


Controls
========

Axis Constrain :kbd:`X`, :kbd:`Y`, :kbd:`Z`
  Constraint the cursor movement on the  X, Y, or Z axis.

Edge Constrain :kbd:`Shift`
   Constraint the cursor movement towards an edge. For the constrain work, you need to have
   your cursor over an edge. This is useful for creating parallel lines.

Confirm Input :kbd:`Return`
   Confirms the numerical value written in the header for the line length.

Cut Line :kbd:`LMB`
   Starts the lines drawing.

Confirm :kbd:`RMB`
   Single click stops the lines drawing. Double-clicks completes the tool's execution.

:kbd:`Tab`
   Snap limited to only faces.

Cancel :kbd:`Esc`
   Cancel the operation.


Options
=======

Create Faces
   A face is created when:

   - It detects the drawing of a closed segment.
   - The last vertex of the segment binds to an edge that connects another vertex of the segment.
   - It detects an isolated edge loop.
   - Redrawn existing edges and the vertex of the last segment binds to an edge
     that connects another vertex of the segment.


.. reference::

   :Category:  Mesh
   :Description: Extends Blender Snap controls.
   :Location: :menuselection:`3D Viewport --> Tools --> Line Tool`
   :File: mesh_snap_utilities_line folder
   :Author: Germano Cavalcante

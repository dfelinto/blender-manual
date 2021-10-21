
*******************
Snap Utilities Line
*******************

.. reference::

   :Category:  Mesh
   :Description: Extends Blender Snap controls.
   :Location: :menuselection:`3D Viewport --> Tools --> Line Tool`
   :File: mesh_snap_utilities_line folder
   :Author: Germano Cavalcante


Installation
============

- This add-on is bundled with Blender.
- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Snap Utilities Line to enable the script.


Usage and Workflow
==================

Once activated, a new Snap Utilities Toool will be added to the viewport toolbar, so long as a mesh object is selected.

The tool is shown in both Object Mode and Edit Mode.

The basic workflow is to first select an object, select LINE tool, and perform the operation with the LMB, when satisfied, finalize the transaction with a double click of the RMB.


Using LINE tool
===============

After selecting the first point with the "RMB" you can specify the length of the line just by typing a value and pressing "Enter".

When approaching the cursor to a face, edge or vertex, the cursor is automatically snapped to the element - The cursor can also be snapped to center or perpendicular of an edge.

The controllers 'X', 'Y', 'Z' and 'Shift' constrain the cursor movement around the highlighted element.


Using constraint Shift
======================

The constrain ‘Shift’ is useful for making parallel lines. To the constrain work, you need to have your cursor over an edge.


Creating Faces
==============

In version 3.9, was implemented the option "create faces".

A face is created when:

- it detects the drawing of a closed segment
- the last vertex of the segment binds to an edge that connects another vertex of the segment
- it detects a isolated edge loop
- redrawn existing edges and the vertex of the last segment binds to an edge that connects another vertex of the segment


Controllers
===========

'X' = Constraint the cursor movement on the axis X

'Y' = Constraint the cursor movement on the axis Y

'Z' = Constraint the cursor movement on the axis Z

'Shift' = Constraint the cursor movement towards an edge

'Enter' = Confirms the numerical value written in the header for the line length

'LeftMouse' = starts the lines drawing

'RightMouse' = 1 click stops the lines drawing, 2 clicks completes the tool's execution

'TAB' = Snap limited only Faces

'ESC' = cancel

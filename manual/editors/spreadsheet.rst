
***********
Spreadsheet
***********

.. figure:: /images/editors_spreadsheet_interface.png
   :align: center

   The Spreadsheet editor.

The Spreadsheet editor is used to debug geometry attributes.


Header
======

Object Evaluation State
   Display the data of an object at different states of its evaluation.

   Final
      Display data from object with all modifiers applied.

   Original
      Display data from original object without any modifiers applied.

Geometry Component Type
   Part of the geometry to display data from.

   Mesh
      Mesh component containing point, corner, polygon and edge data.
   Point Cloud
      Point cloud component containing only point data.

Attribute Domain
   Attribute domain to display.

   Point
      Display attributes that are stored per point.
   Corner
      Display attributes that are stored per polygon corner.
   Polygon
      Display attributes that are stored per polygon.
   Edge
      Display attributes that are stored per edge.

Toggle Pin
   Usually, the editor displays data from the active object.
   When an object is pinned, its data remains visible, even if another object becomes active.

Selected Only
   This option is only available if the object is in Edit Mode.
   When checked, only data for the selected mesh elements is shown.


Main Region
===========

The main view allows you to view the actual spreadsheet.
Row indices and column names remain visible when scrolling down or to the side.


Status Bar
==========

The status bar shows how many rows and columns there are and how many have been filtered out.

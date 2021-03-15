
***********
Spreadsheet
***********

.. figure:: /images/editors_spreadsheet_interface.png
   :align: center

   The Spreadsheet editor.

The Spreadsheet editor is used to debug geometry attributes.

Header
======

Geometry Component Type
   Part of the geometry to display data from.

   Mesh
      Mesh component containing point, corner, polygon and edge data.
   Point Cloud
      Point cloud component containg only point data.

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
   This option is only available if the object is in edit mode.
   When checked, only data for the selected mesh elements is shown.

Main Region
===========

The main view allows you to view the actual spreadsheet.
Row indices and column names remain visible when scrolling down or to the side.

Status Bar
==========

The status bar shows how many rows and columns there are and how many have been filtered out.

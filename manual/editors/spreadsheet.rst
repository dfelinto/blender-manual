.. _bpy.ops.spreadsheet:
.. _bpy.types.SpaceSpreadsheet:

***********
Spreadsheet
***********

The Spreadsheet editor is used to debug geometry attributes.

.. figure:: /images/editors_spreadsheet_interface.png
   :align: center

   The Spreadsheet editor.


Header
======

.. _bpy.types.SpaceSpreadsheet.object_eval_state:

Object Evaluation State
   Display the data of an object at different states of its evaluation.

   :Final: Display data from object with all modifiers applied.
   :Original: Display data from original object without any modifiers applied.

.. _bpy.types.SpaceSpreadsheet.geometry_component_type:

Geometry Component Type
   Part of the geometry to display data from.

   :Mesh: Mesh component containing point, corner, face and edge data.
   :Point Cloud: Point cloud component containing only point data.
   :Instances: Display which objects and collections are instanced and their transforms.

.. _bpy.types.SpaceSpreadsheet.attribute_domain:

Attribute Domain
   Attribute domain to display.

   :Point: Display attributes that are stored per point.
   :Corner: Display attributes that are stored per face corner.
   :Face: Display attributes that are stored per face.
   :Edge: Display attributes that are stored per edge.

.. _bpy.ops.spreadsheet.toggle_pin:

Toggle Pin
   Usually, the editor displays data from the active object.
   When an object is pinned, its data remains visible, even if another object becomes active.

.. _bpy.types.SpaceSpreadsheet.show_only_selected:

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

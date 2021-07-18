.. _bpy.ops.spreadsheet:
.. _bpy.types.SpaceSpreadsheet:

***********
Spreadsheet
***********

The Spreadsheet editor is used to inspect geometry attributes.

.. figure:: /images/editors_spreadsheet_interface.png
   :align: center

   The Spreadsheet editor.


Header
======

.. _bpy.types.SpaceSpreadsheet.object_eval_state:

Object Evaluation State
   Display the data of an object at different states of its evaluation.

   :Evaluated: Display data from object with all modifiers applied.
   :Original: Display data from original object without any modifiers applied.

Breadcrumbs
   The breadcrumbs shows three key parts of the path the evaluated object
   takes before showing the information in the `Main Region`_.
   In the order from left to right, the first item displayed is the :term:`Active` object.
   The next two items are displayed when a geometry node's
   :ref:`Preview Toggle <bpy.ops.node.active_preview_toggle>` is enabled.
   The first of these next items is the name of the Geometry Nodes modifier,
   the last item shown is the name of the active node.

   Clicking the arrow between items hides the name of the active modifier.

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


Dataset Region
==============

The dataset region on the left allows choosing wich geometry component and geometry domain to view.
Each attribute domain also displays its size, for example the number of faces.

.. _bpy.types.SpaceSpreadsheet.geometry_component_type:

Geometry Component Type
   Part of the geometry to display data from.

   :Mesh: Mesh component containing point, corner, face and edge data.
   :Point Cloud: Point cloud component containing only point data.
   :Curve: Display curve data: the attributes on splines and control points.
   :Instances: Display which objects and collections are instanced and their transforms.

.. _bpy.types.SpaceSpreadsheet.attribute_domain:

Attribute Domain
   Attribute domain to display.

   :Vertex: Display attributes that are stored per vertex.
   :Edge: Display attributes that are stored per edge.
   :Face: Display attributes that are stored per face.
   :Face Corner: Display attributes that are stored per face corner.

.. _bpy.types.SpaceSpreadsheet.display_context_path_collapsed:


Status Bar
==========

The status bar shows how many rows and columns there are and how many have been filtered out.

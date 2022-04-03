.. index:: Geometry Nodes; Viewer
.. _bpy.types.GeometryNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/node-types_GeometryNodeViewer.webp
   :align: center
   :alt: The Viewer node.

   The Viewer node.

Using a *Viewer* node a geometry, and optionally a field evaluated it,
can be displayed in the :doc:`Spreadsheet Editor </editors/spreadsheet>`.
A node can be connected with a Viewer node by pressing :kbd:`Shift-Ctrl-LMB`,
while hovering the mouse over it, just like in the Compositor.


Inputs
======

Geometry
   Geometry that will be displayed in the Spreadsheet.

Value
   Field to be evaluated on the geometry.
   The type for this value is chosen automatically when the keyboard shortcut to link
   an output is pressed. However, if the type must be adjusted manually,
   it is available in the node editor Sidebar.


Properties
==========

This node has no properties.


Outputs
=======

This node has no outputs.

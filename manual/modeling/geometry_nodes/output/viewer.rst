.. index:: Geometry Nodes; Viewer
.. _bpy.types.GeometryNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/modeling_geometry-nodes_output_viewer_node.png
   :align: center

   The Viewer node.

Using a *Viewer* node a geometry, and optionally a field evaluated it,
can be displayed in the :doc:`Spreadsheet Editor </editors/spreadsheet>`. 
A node can be plugged into a viewer node by pressing :kbd:`Shift-Ctrl-LMB`,
while the mouse is hovered over it, just like in the Compositor.


Inputs
======

Geometry
   Geometry that will be displayed in the Spreadsheet.

Value
   Field to be evaluated on the geometry.
   The type for this value is chosen automatically when the keyboard shortcut to link
   an output is pressed. However if the type must be adjusted manually, it is available
   in the node editor properties region.


Properties
==========

This node has no properties.


Outputs
=======

This node has no outputs.

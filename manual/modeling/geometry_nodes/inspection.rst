.. index:: Geometry Nodes; Inspection

**********
Inspection
**********

Inspecting intermediate values in a geometry node group is useful while building/understanding one or when trying to figure out why something is not working.
Blender provides multiple tools to understand how a node group is working or why it is not working.

.. note::

   Generally, the inspection tools display data from the last time the node group has been evaluated.
   If it has not been evaluated, no information is available.

Socket Inspection
=================

.. figure:: /images/modeling_geometry-nodes_inspection_socket-inspection.png
   :align: center

   Socket Inspection.

Socket inspection shows information about the value in a socket during the last evaluation.
For primitive data types such as integer and float the actual value is shown.
For geometry sockets only some metadata about the geometry is stored.
That includes the set of geometry components and how many elements there are.

Attribute Search
================

.. figure:: /images/modeling_geometry-nodes_attribute-reference_search.png
   :align: center

   Attribute Search.

The attribute search appears when clicking on a string socket. It contains a list of all the attributes that are available in the geometry inputs of the same node.

Viewer Node
===========

The viewer node is used to display intermediate geometry in the spreadsheet.
For more information check :doc:`this </modeling/geometry_nodes/output/viewer>`.

Node Warnings
=============

.. figure:: /images/modeling_geometry-nodes_inspection_node-warning.png
   :align: center

   Node Warnings.

When the inputs to a node are invalid, it can have a warning.
Hovering over the warning icon shows the error message.

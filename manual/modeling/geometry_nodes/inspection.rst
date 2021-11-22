.. index:: Geometry Nodes; Inspection

**********
Inspection
**********

Inspecting intermediate values in a geometry node tree is useful while
building/understanding one or when trying to figure out why something is not working.
Blender provides multiple tools to understand how a node tree is working
or why it is not working.

.. note::

   Generally, the inspection tools display data from the last time the node tree has been evaluated.
   If it has not been evaluated, no information is available.


.. _socket-inspection:

Socket Inspection
=================

.. figure:: /images/modeling_geometry-nodes_inspection_socket-inspection.png
   :align: center

   Socket Inspection.

Socket inspection shows information about the value in a socket during the last evaluation.
For primitive data types such as integers, vectors, and strings the actual value is shown.
For geometry sockets only some data about the geometry is stored, including the set of
data types the geometry contains, and a count of their elements.

Socket values are only logged from when the node tree was executed, so a node must be
connected to the group output to have a value for inspection. Values are not logged during
rendering, to improve performance.


Attribute Search
================

.. figure:: /images/modeling_geometry-nodes_attribute-reference_search.png
   :align: center

   Attribute Search.

The attribute search is shown when clicking on an attribute input in the modifier.
It contains a list of all the attributes that were available at that point in
the modifier or node execution.


Viewer Node
===========

The Viewer node is used to display intermediate geometry in the Spreadsheet.
For more information see :doc:`/modeling/geometry_nodes/output/viewer`.


Node Warnings
=============

.. figure:: /images/modeling_geometry-nodes_inspection_node-warning.png
   :align: center

   Node Warning.

When the inputs to a node are invalid, it displays a warning in the title.
Hovering over the warning icon shows the error message. These warnings are only
generated when the node is executed, so a node must be connected to the group output
to have a warning.

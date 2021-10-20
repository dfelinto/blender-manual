.. index:: Geometry Nodes; Set Point Radius
.. _bpy.types.GeometryNodeSetPointRadius:

*********************
Set Point Radius Node
*********************

.. figure:: /images/modeling_geometry-nodes_point_set-point-radius_node.png
   :align: right

   The Set Point Radius node.

The *Set Point Radius* node controls the size each selected point cloud point should display with in the viewport.
The input node for this data is the :doc:`Radius </modeling/geometry_nodes/input/radius>` node.


Inputs
======

Geometry
   Standard geometry input.

Radius
   Float value indicating the radius of the point geometry at each point.

Selection
   Boolean input for selecting which points will have the radius value applied.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

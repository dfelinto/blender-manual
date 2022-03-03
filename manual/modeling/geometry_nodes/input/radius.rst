.. index:: Geometry Nodes; Radius
.. _bpy.types.GeometryNodeInputRadius:

***********
Radius Node
***********

.. figure:: /images/modeling_geometry-nodes_input_radius_node.png
   :align: right
   :alt: Radius node.

The *Radius* node outputs the radius value at each point on the evaluated geometry.
For curves, this value is used for things like determining the size of the mesh created in
the :doc:`Curve to Mesh </modeling/geometry_nodes/curve/curve_to_mesh>` node.
For point clouds, the value is used for the display size of the point in the viewport.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Radius
   Float value indicating radius at each point on the geometry.

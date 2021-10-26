.. index:: Geometry Nodes; Separate Components
.. _bpy.types.GeometryNodeSeparateComponents:

************************
Separate Components Node
************************

.. figure:: /images/modeling_geometry-nodes_geometry_separate-components_node.png
   :align: center

   The Separate Components node.

The *Separate Components* node splits a geometry into a separate output
for each type of data in the geometry. 


Inputs
======

Geometry
   Standard geometry input.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Mesh component of the input geometry.

Point Cloud
   Point cloud component of the input geometry.

Curve
   Curve component of the input geometry.

Volume
   Volume component of the input geometry.

Instances
   Instances component of the input geometry. Even if the instances contain geometry data with
   one of the other types, all instances will be added to this output. 
   A :doc:`/modeling/geometry_nodes/instances/realize_instances` can be added to move the data from
   geometry instances to their corresponding outputs.

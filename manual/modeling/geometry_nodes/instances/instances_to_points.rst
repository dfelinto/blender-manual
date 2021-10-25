.. index:: Geometry Nodes; Instances to Points
.. _bpy.types.GeometryNodeInstancesToPoints:

************************
Instances to Points Node
************************

.. figure:: /images/modeling_geometry-nodes_point_instances-to-points_node.png
   :align: right

   The Instances to Points node.

The *Instances to Points* node generates points on top-level instances' origins.

.. note::

   Top-level instances are those that are owned by the node's input geometry. Instances owned by other instances, i.e. nested instances, are not considered by this node.


Inputs
======

Instances
   Standard geometry input.

Selection
   The instances used to generate points.

Position
   Overrides the default position of generated point.

Radius
   Controls the specified points' radius.

Outputs
=======

Points
   Generated points.

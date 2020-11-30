.. index:: Nodes; Mesh; Point Distribute
.. _bpy.types.GeometryNodePointInstance:

**************
Point Distribute
**************

.. figure:: /images/modeling_modifiers_nodes_point-distribute.png
   :align: right

   Point Distribute Node.

The *Point Distribute* node distributes points on the surface of the input geometry object.

.. note::
   This node only works if it the modifier belongs to a point cloud object.


Inputs
======

Geometry
   Source geometry to distribute points on.
Density
   The point density for the point distribution.
   In other words, how many points there will be within one square meter.
Density Attribute
   Which attribute to use for influencing the point density.
   The input values are mapped between zero and the density defined above.


Outputs
=======

Geometry
   The generated point distribution.

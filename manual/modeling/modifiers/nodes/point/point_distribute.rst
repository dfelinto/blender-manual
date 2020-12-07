.. index:: Nodes; Mesh; Point Distribute
.. _bpy.types.GeometryNodePointDistribute:

****************
Point Distribute
****************

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

   .. note::
      Only mesh geometries are supported.

Minimum Distance
   The minimal distance points can have to each other.
   This option is only available on distribution methods that supports it.

Maximum Density
   The point density for the point distribution.
   In other words, how many points there will be within one square meter.

   .. note::
      This will be capped on distributions with the *Minimal Distance* option.
      If the Density is greater than what the minimal distance allows, then no new points will be added after this threshold has been passed.

Density Attribute
   Which attribute to use for influencing the point density.
   The input values are mapped between zero and the density defined above.

Seed
   The random seed to use when generating points.


Outputs
=======

Geometry
   The generated point distribution.

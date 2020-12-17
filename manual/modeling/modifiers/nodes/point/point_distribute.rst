.. index:: Nodes; Mesh; Point Distribute
.. _bpy.types.GeometryNodePointDistribute:

****************
Point Distribute
****************

.. figure:: /images/modeling_modifiers_nodes_point-distribute.png
   :align: right

   Point Distribute Node.

The *Point Distribute* node distributes points on the surface of the input geometry object.

Inputs
======

Geometry
   Standard geometry input.

   .. note::

      Only meshes are supported.

Distance Min
   The minimal distance points can have to each other.
   This option is only available on distribution methods that supports it.

Density Max
   The point density for the point distribution.
   In other words, how many points there will be within one square meter.

   .. note::
      This will be capped on distributions with the *Distance Min* option.
      If the density is greater than what the minimal distance allows, no new
      points will be added after this threshold has been passed.

Density Attribute
   Which attribute to use for influencing the point density.
   The input values are mapped between zero and the *Density*.


Properties
==========

Distribution Method
   Random
      Distribute points randomly on the surface.
   Poisson Disk
      Project points on the surface evenly with a Poisson disk distribution.

Seed
   The random seed to use when generating points.


Output
======

Geometry
   Generated points.

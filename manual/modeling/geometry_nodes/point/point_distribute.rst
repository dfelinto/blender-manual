.. index:: Geometry Nodes; Point Distribute
.. _bpy.types.GeometryNodePointDistribute:

****************
Point Distribute
****************

.. figure:: /images/modeling_geometry-nodes_point_point-distribute_panel.png
   :align: right

   The Point Distribute Node.

The *Point Distribute* node places points on the surface of the input geometry object.
Point and corner attributes of the input geometry are transferred to the generated points.
That includes vertex weights and UV maps.
Additionally, the generated points will have a *normal*, *id* and *rotation* attribute.


Inputs
======

Geometry
   Standard geometry input.

   .. note::

      The input geometry must contain a mesh with faces.

Distance Min
   The minimal distance points can have to each other.
   This option is only available on distribution methods that support it.

Density Max
   The point density for the point distribution. The units are number of points per square meter.
   This value is multiplied by the values from the *Density Attribute*.

   .. note::

      This will be capped on distributions by the *Distance Min* option.
      If the density is greater than what the minimal distance allows,
      no new points will be added after this threshold has been passed.

Density Attribute
   The name of the attribute to use for influencing the point density.
   The values of this attribute are multiplied by *Density Max* for the final density value.

Seed
   The random :term:`Seed` to use when generating points.

Properties
==========

Distribution Method
   Random
      Distribute points randomly on the surface. This is the fastest distribution method.

   Poisson Disk
      Distribute points randomly on the surface while taking a minimum distance into account.

Output
======

Geometry
   Generated points. Several attributes are created on the output points based on the input mesh:

   .. object:: id (int)

      An identifier for each point used for stability when the mesh is deformed,
      used in the :doc:`/modeling/geometry_nodes/attribute/attribute_randomize`
      and :doc:`/modeling/geometry_nodes/point/point_instance` nodes.

   .. object:: normal (vector)

      The :term:`Normal` of the triangle on which each point is scattered.

   .. object:: rotation (vector)

      An XYZ :term:`Euler` rotation built from the normal attribute for convenience.

.. index:: Nodes; Mesh; Point Distribute
.. _bpy.types.GeometryNodePointDistribute:

****************
Point Distribute
****************

.. figure:: /images/modeling_modifiers_nodes_point-distribute.png
   :align: right

   The Point Distribute Node.

The *Point Distribute* node distributes points on the surface of the input geometry object.


Inputs
======

Geometry
   Standard geometry input.

   .. note::

      The input geometry must contain a mesh with faces.

Distance Min
   The minimal distance points can have to each other.
   This option is only available on distribution methods that supports it.

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


Properties
==========

Distribution Method
   Random
      Distribute points randomly on the surface.

   Poisson Disk
      Distribute points more evenly on the XY plane, then project them to the mesh along the Z axis.

Seed
   The random :term:`Seed` to use when generating points.


Output
======

Geometry
   Generated points. Several attributes are created on the output points based on the input mesh:
      .. describe:: id (int)

         An identifier for each point used for stability when the mesh is deformed, used in the
         :doc:`/modeling/modifiers/nodes/attribute/attribute_randomize` and 
         :doc:`/modeling/modifiers/nodes/point/point_instance` nodes.

      .. describe:: normal (vector)

         The :term:`Normal` of the triangle on which each point is scattered.

      .. describe:: rotation (vector)
      
         An XYZ :term:`Euler` rotation built from the normal attribute for convenience.
.. index:: Geometry Nodes; UV Sphere
.. _bpy.types.GeometryNodeMeshUVSphere:

*********
UV Sphere
*********

.. figure:: /images/modeling_geometry-nodes_mesh-primitives_uv-sphere_node.png
   :align: right

   UV Sphere Node.

The *UV Sphere* node generates a spherical mesh mostly out of quads except for triangles at the top and bottom.


Inputs
======

Segments
   Horizontal resolution of the sphere.
   If this is smaller than three, no mesh is generated.

Rings
   Vertical resolution of the sphere.
   If this is smaller than three, no mesh is generated.

Radius
   Distance of vertices to the origin.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

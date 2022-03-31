.. index:: Geometry Nodes; UV Sphere
.. _bpy.types.GeometryNodeMeshUVSphere:

**************
UV Sphere Node
**************

.. figure:: /images/node-types_GeometryNodeMeshUVSphere.webp
   :align: right
   :alt: UV Sphere Node.

The *UV Sphere* node generates a spherical mesh mostly out of quads except for triangles at the top and bottom.


Inputs
======

Segments
   Horizontal resolution of the sphere.
   If this is smaller than three, no mesh is generated.

Rings
   Vertical resolution of the sphere.
   If this is smaller than two, no mesh is generated.

Radius
   Distance of vertices to the origin.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Standard geometry output.

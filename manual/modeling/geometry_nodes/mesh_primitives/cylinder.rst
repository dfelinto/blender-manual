.. index:: Geometry Nodes; Cylinder
.. _bpy.types.GeometryNodeMeshCylinder:

********
Cylinder
********

.. figure:: /images/modeling_geometry-nodes_mesh-primitives_cylinder_node.png
   :align: right

   Cylinder Node.

The *Cylinder* node generates a cylinder mesh.
It is similar to the cone node but always uses the same radius for the circles at the top and bottom.


Inputs
======

Vertices
   Number of points on the circle at the top and bottom.
   No geometry is generated if the number is below three.

Radius
   Distance of the vertices from the Z axis.
   If this is zero, the output will be a single line.

Depth
   Height of the cylinder.


Properties
==========

Fill Type
   How the circles at the top and bottom are filled with faces when their radius is larger than zero.

   :None: Do not fill the circles.
   :N-Gon: Fill the circles with a single face.
   :Triangles: Fill the circles with triangles connected to a new vertex on the Z axis.


Outputs
=======

Geometry
   Standard geometry output.

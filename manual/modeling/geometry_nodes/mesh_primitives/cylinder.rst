.. index:: Geometry Nodes; Cylinder
.. _bpy.types.GeometryNodeMeshCylinder:

*************
Cylinder Node
*************

.. figure:: /images/modeling_geometry-nodes_mesh-primitives_cylinder_node.png
   :align: right

   Cylinder node.

The *Cylinder* node generates a cylinder mesh.
It is similar to the Cone node but always uses the same radius for the circles at the top and bottom.


Inputs
======

Vertices
   Number of vertices on the circle at the top and bottom.
   No geometry is generated if the number is below three.

Side Segments
   Number of edges running vertically along the side of the cone.
   No geometry is generated if the number is below one.

Fill Segments
   Number of concentric rings used to fill the round faces at the top and bottom.
   No geometry is generated if the number is below one.

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
   :N-Gon: Fill the innermost segment of the circles with a single face.
   :Triangles: Fill the innermost segment of the circles with triangles connected to a new vertex on the Z axis.


Outputs
=======

Mesh
   Standard geometry output.

.. index:: Geometry Nodes; Cone
.. _bpy.types.GeometryNodeMeshCone:

****
Cone
****

.. figure:: /images/modeling_geometry-nodes_mesh-primitives_cone_node.png
   :align: right

   Cone Node.

The *Cone* node generates a cone mesh that is optionally truncated.


Inputs
======

Vertices
   Number of points on the circle at the top and bottom.
   No geometry is generated if the number is below three.

Radius Top
   The distance of the vertices in the top circle from the Z axis.
   If this is zero, the vertices in the circle are merged into one.

Radius Bottom
   Same as *Radius Top* but for the bottom circle.

Depth
   Height of the generated cone.

.. note::

   If the top and bottom radius is zero, this node will output a single line.


Properties
==========

Fill Type
   How the circles at the top and bottom are filled with faces when their radius is larger than zero.

   None
      Do not fill the circles.

   N-Gon
      Fill the circles with a single face.

   Triangles
      Fill the circles with triangles connected to a new vertex on the Z axis.


Outputs
=======

Geometry
   Standard geometry output.

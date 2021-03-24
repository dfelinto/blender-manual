.. index:: Geometry Nodes; Circle
.. _bpy.types.GeometryNodeMeshCircle:

******
Circle
******

.. figure:: /images/modeling_geometry-nodes_mesh-primitives_circle_node.png
   :align: right

   Circle Node.

The *Circle* node generates a circular ring of edges that is optionally filled with faces.


Inputs
======

Vertices
   Number of vertices on the circle.
   No geometry is generated when the number is below three.

Radius
   Distance of the vertices from the origin.


Properties
==========

Fill Type
   How the circle is filled with faces.

   None
      Output just the edge ring without any faces.

   N-Gon
      Fill the circle with a single face.

   Triangles
      Fill the circle with triangles connected to a new vertex at the origin.

Outputs
=======

Geometry
   Standard geometry output.

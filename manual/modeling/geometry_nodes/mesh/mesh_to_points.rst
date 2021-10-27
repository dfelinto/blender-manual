.. index:: Geometry Nodes; Mesh to Points
.. _bpy.types.GeometryNodeMeshtoPoints:

*******************
Mesh to Points Node
*******************

.. figure:: /images/modeling_geometry-nodes_mesh_mesh-to-points_node.png
   :align: right

   Mesh to Points node.

The *Mesh to Points* node generates a point cloud from a mesh.


Inputs
======

Mesh
   Standard Mesh input.

Selection
   The meshes used to generate a point cloud.

Position
   Positions of generated points.

Radius
   Radii of generated points.


Properties
==========

Mode
   :Vertices: Points are generated for each vertex.
   :Edges: Points are generated for each edge.
   :Faces: Points are generated for each face.
   :Corners: Points are generated for each corner.


Outputs
=======

Points
   Generated point cloud.

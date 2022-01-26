.. index:: Geometry Nodes; Face Neighbors
.. _bpy.types.GeometryNodeFaceNeighbors:

*******************
Face Neighbors Node
*******************

.. figure:: /images/modeling_geometry-nodes_input_face-neighbors_node.png
   :align: right

   Face Neighbors Node.

The *Face Neighbors* node outputs topology information relating to each face of a mesh.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Vertex Count
   This output is simply the number of sides of each face, or how many corners each face has.

Neighboring Face Count
   The number of faces that connect to this face with at least one edge. On a regular manifold
   mesh with only quads and triangles, this will be the same as the vertex count, otherwise it might
   be completely different.

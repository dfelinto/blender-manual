.. index:: Geometry Nodes; Face Set Boundaries
.. _bpy.types.GeometryNodeMeshFaceSetBoundaries:

************************
Face Set Boundaries Node
************************

.. figure:: /images/node-types_GeometryNodeMeshFaceSetBoundaries.png
   :align: right
   :alt: Face Set Boundaries node.

The *Face Set Boundaries Node* finds the edges which lie on the boundaries of 
specified regions. These edges could be used to mark seams for UV unwrapping, 
for example.


Inputs
======

Face Set
   Identifier for which group of faces this face belongs to. All contiguous faces
   with the same value are in the same region.

Properties
==========

This node has no properties.


Output
======

Boundary Edges
   Selection of the boundary edges of the different face sets. An edge is
   considered to be at the boundary if it lies on at least two faces with
   different identifiers.


Examples
========

.. figure:: /images/modeling_geometry-nodes_face-set-boundaries_voronoi-seams.png

Combined with the :doc:`UV Unwrap Node </modeling/geometry_nodes/uv/uv_unwrap>`,
this node is used to turn the face sets (right cube) into a UV map for a texture (left cube).

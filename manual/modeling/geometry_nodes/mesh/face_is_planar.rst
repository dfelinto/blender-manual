.. index:: Geometry Nodes; Face is Planar
.. _bpy.types.GeometryNodeInputMeshFaceIsPlanar:

*******************
Face is Planar Node
*******************

.. figure:: /images/node-types_GeometryNodeInputMeshFaceIsPlanar.png
   :align: right
   :alt: Face is Planar Node.

The *Face is Planar* node outputs whether every triangle of a
:term:`quads <Quad>` or :term:`N-gons <N-gon>` is on the same plane as all of the others, in
other words, if they have the same :doc:`normal </modeling/meshes/editing/mesh/normals>`.

For example, a non-planar face can be created by moving a single vertex in a face but not
the others. Triangles will always be planar.


Inputs
======

Threshold
    The distance a point can be from the surface before the face is no longer
    considered planar.


Properties
==========

This node has no properties.


Outputs
=======

Planar
   Whether each mesh face is planar.


Examples
========

.. figure:: /images/modeling_geometry-nodes_input_face-is-planar_simple.png
   :align: center

Combined with the :doc:`/modeling/geometry_nodes/material/set_material`,
this node is used to visualize all non-planar faces in a mesh.

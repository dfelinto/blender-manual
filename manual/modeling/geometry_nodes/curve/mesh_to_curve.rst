.. index:: Geometry Nodes; Mesh to Curve
.. _bpy.types.GeometryNodeMeshToCurve:

*************
Mesh to Curve
*************

.. figure:: /images/modeling_geometry-nodes_curve_mesh-to-curve_node.png
   :align: center

   The Mesh to Curve node.

The *Mesh to Curve* node converts all or a selection of edges to splines.
Vertices connected to exactly two edges will join the splines corresponding to both edges.
Vertices connected one or more than two edges become end points of splines.
Circular splines are supported as well.


Inputs
======

Mesh
   Standard geometry input.

Selection
   Optional selection attribute that determines which edges will be turned into splines.


Properties
==========

This node has no properties.


Outputs
=======

Curve
   Standard geometry output.

.. index:: Geometry Nodes; Convex Hull
.. _bpy.types.GeometryNodeConvexHull:

****************
Convex Hull Node
****************

.. figure:: /images/modeling_geometry-nodes_geometry_convex-hull_node.png

   The Convex Hull node.

The *Convex Hull* node outputs a convex mesh that is enclosing all points in the input geometry.

.. note::

   When the node is used on a geometry with instances, the algorithm will run once per instance,
   resulting in many convex hull meshes in the instance pieces of geometry. The *Realize Instances* node can
   be used to get a convex hull of an entire geometry.

.. important::

   Volumes are not supported by this node, and attributes are not automatically transferred to the result.


Inputs
======

Geometry
   Standard geometry inputs.


Properties
==========

This node has not properties.


Outputs
=======

Convex Hull
   Mesh that encloses all points in the input.

.. index:: Geometry Nodes; Spiral
.. _bpy.types.GeometryNodeCurveSpiral:

************
Curve Spiral
************

.. figure:: /images/modeling_geometry-nodes_curve-primitives_spiral_node.png
   :align: right

   Spiral Node.

The *Spiral* node generates a poly spline in a spiral shape.
It can be used to create springs or other similar objects.
By default the spiral twists in a clockwise fashion.


Inputs
======

Resolution
   Number of edges for each full rotation.

Rotations
   Number of times the spiral makes a full rotation.

Start Radius, End Radius
   Radius of the start point and end point of the spiral.
   The radius of the spiral changes linearly between the two values over the whole spiral.

Height
   Height of the spiral.

Reverse
   Boolean value that changes the direction from clockwise to counterclockwise when it is enabled.


Properties
==========

This node has no properties.


Outputs
=======

Curve
   Poly spline generated from the inputs.

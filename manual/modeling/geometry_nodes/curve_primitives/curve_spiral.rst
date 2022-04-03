.. index:: Geometry Nodes; Curve Spiral
.. _bpy.types.GeometryNodeCurveSpiral:

*****************
Curve Spiral Node
*****************

.. figure:: /images/node-types_GeometryNodeCurveSpiral.webp
   :align: right
   :alt: Curve Spiral Node.

   Curve Spiral Node.

The *Curve Spiral* node generates a poly spline in a spiral shape.
It can be used to create springs or other similar objects.
By default the spiral twists in a clockwise fashion.


Inputs
======

Resolution
   Number of points in one rotation of the spiral.

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

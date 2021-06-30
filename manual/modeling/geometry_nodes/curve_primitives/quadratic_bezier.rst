.. index:: Geometry Nodes; Quadratic Bezier
.. _bpy.types.GeometryNodeCurveQuadraticBezier:

****************
Quadratic Bezier
****************

.. figure:: /images/modeling_geometry-nodes_curve-primitives_quadratic-bezier_node.png
   :align: right

   Quadratic Bezier Node.

The *Quadratic Bezier* node generates a poly spline curve from the given control points.
The generated shape is a parabola.


Inputs
======

Resolution
   The number of edges on the curve.

Start, Middle, End
   Positions of the three control points.
   The generated curve passes through the two end points, and is tangent to the lines between
   the middle point and the two end points.



Properties
==========

This node has no properties.


Outputs
=======

Curve
   Poly spline generated from the inputs.

.. index:: Geometry Nodes; Bezier Segment
.. _bpy.types.GeometryNodeCurvePrimitiveBezierSegment:

****************
Bezier Segment
****************

.. figure:: /images/modeling_geometry-nodes_curve-primitives_bezier-segment_node.png
   :align: right

   Bezier Segment Node.

The *Bezier Segment* node generates a 2D bezier spline from the given control points and handles.


Inputs
======

Resolution
   The number of edges on the curve.

Start, End
   Positions of the start and end control point of the curve.

Start Handle, End Handle
   Positions of the handles used to define the shape of the curve. 



Properties
==========

Mode
   :Position:
      The handle inputs are the absolute positions of the handles in 3D space.
   :Offset: 
      The handle positions are relative to the control point on the curve.
      The handle inputs give the offset from the control points.


Outputs
=======

Curve
   Bezier spline generated from the inputs.

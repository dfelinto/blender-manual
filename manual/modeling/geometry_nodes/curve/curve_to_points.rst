.. index:: Geometry Nodes; Curve to Points
.. _bpy.types.GeometryNodeCurveToPoints:

********************
Curve to Points Node
********************

.. figure:: /images/modeling_geometry-nodes_curve_curve-to-points_node.png
   :align: right

   Curve to Points Node

The *Curve to Points* node generates a point cloud from a curve.


Inputs
======

Curve
   Standard curve input.

Count
   Number of points generated. This input is only available for *Count* mode.

Length
   Length of the curve. This input is only available for *Length* mode.

Properties
==========

Mode
   :Evaluated: Creates points from the curve's evaluated points based on the resolution attribute for NURBS and Bezier splines.
   :Count: Samples each spline by evenly distributing the specified number of points.
   :Length: Samples each spline by splitting it into segments with specified length.


Outputs
=======

Points
   Generated point cloud.


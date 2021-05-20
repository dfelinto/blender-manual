.. index:: Geometry Nodes; Resample Curve
.. _bpy.types.GeometryNodeResampleCurve:

**************
Resample Curve
**************

.. figure:: /images/modeling_geometry-nodes_curve_resample-curve_node.png
   :align: center

   The Resample Curve node.

The Resample Curve node creates a poly spline for each input spline.
In the new poly splines the control points will have uniform spacing.


Inputs
======

Geometry
   Standard geometry input.

Count
   Number of control points on the new splines.

Length
   Approximate length between the control points of the new splines.


Properties
==========

Mode
   How to specify the amount of samples.

   :Count:
      Sample the specified number of points along each spline.
   :Length:
      Calculate the number of samples by splitting each spline into segments with the specified length.
      The length will be rounded down so that a whole number of samples will fit in each input spline.


Outputs
=======

Geometry
   Standard geometry output.

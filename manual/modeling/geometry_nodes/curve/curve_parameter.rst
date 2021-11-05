.. index:: Geometry Nodes; Curve Parameter
.. _bpy.types.GeometryNodeCurveParameter:

********************
Curve Parameter Node
********************

.. figure:: /images/modeling_geometry-nodes_curve_curve-parameter_node.png
   :align: right

   Curve Parameter node.

The *Curve Parameter* node outputs how far along each spline a control point is, with a value between
zero and one. The output is different from dividing the index by the total number of control points,
because the control points might not be equally spaced along the curve.

The first value is zero, so the output corresponds to the length at the control point rather than
including the length of the following segment.

When used on the spline domain, the node outputs the portion of the total length of the curve (including
all splines) has been traversed at the start of each spline. The order of the curve's splines is visible
in the :doc:`Spreadsheet Editor </editors/spreadsheet>`.

.. warning::

   For NURBS and Bézier spline curves, keep in mind that the value retrieved from this node is
   the value at every control point, which may not correspond to the visible *evaluated* points.
   For NURBS splines the difference may be even more pronounced and the result may not be as expected.
   A :doc:`/modeling/geometry_nodes/curve/resample_curve` node can be used to create a poly spline,
   where there is a control point for every evaluated point.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Factor
   The portion of the total length of the spline at each control point.


Examples
========

.. figure:: /images/modeling_geometry-nodes_curve_curve-parameter_example.png
   :align: right

The parameter used to control the radius of the curve.
The beginning of the spline has a radius of 0, the end has a radius of 1.

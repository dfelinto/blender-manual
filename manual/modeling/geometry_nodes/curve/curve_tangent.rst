.. index:: Geometry Nodes; Curve Tangent
.. _bpy.types.GeometryNodeInputTangent:

******************
Curve Tangent Node
******************

.. figure:: /images/modeling_geometry-nodes_curve_curve-tangent_node.png
   :align: right

   Curve Tangent Node

The *Curve Tangent* node outputs the direction that a curve points in at each control point, depending
on the direction of the curve (which can be controlled with the 
:doc:`Reverse Curve node</modeling/geometry_nodes/curve/reverse_curve>`).
The output values are normalized vectors.

.. warning::

   For NURBS and Bezier spline curves, keep in mind that the value retrieved from this node is the
   value at every control point, which may not correspond to the visible *evaluated* points. For
   NURBS splines the difference may be even more pronounced and the result may not be as expected.
   A :doc:`/modeling/geometry_nodes/curve/resample_curve` node can be used to create a Poly spline,
   where there is a control point for every evaluated point.

Inputs
======

This node has no inputs.

Properties
==========

This node has no properties.

Outputs
=======

Tangent
   The direction of the curve at every control point.
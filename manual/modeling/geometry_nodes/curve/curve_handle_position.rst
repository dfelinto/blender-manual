.. index:: Geometry Nodes; Curve Handle Position
.. _bpy.types.GeometryNodeInputCurveHandlePositions:

**************************
Curve Handle Position Node
**************************

.. figure:: /images/modeling_geometry-nodes_curve_curve-handle-positions_node.png
   :align: right

   Curve Handle Position node.

The *Curve Handle Position* node outputs the position of each of a Bézier spline's handles.
If the curve does not contain Bézier splines, the node will output zero.

The node to set this data is the :doc:`/modeling/geometry_nodes/curve/set_handle_positions`.


Inputs
======

Relative
   Output the handle positions relative to the corresponding control point
   instead of in the local space of the geometry.

Properties
==========

This node has no properties.


Outputs
=======

Left
   The position of the each control point's left handle.

Right
   The position of the each control point's right handle.

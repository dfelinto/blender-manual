.. index:: Geometry Nodes; Set Spline Resolution
.. _bpy.types.GeometryNodeSetSplineResolution:

**************************
Set Spline Resolution Node
**************************

.. figure:: /images/modeling_geometry-nodes_curve_set-spline-resolution_node.png
   :align: right

   Set Spline Resolution Node

The *Set Spline Resolution* sets the value for how many evaluated points should be generated on the curve for
every control point. The node only has an effect on :term:`NURBS` and :term:`Bézier` splines. The evaluated points
are displayed in the viewport, used in the :doc:`Curve to Mesh </modeling/geometry_nodes/curve/curve_to_mesh>` node,
and optionally used in the :doc:`Resample Curve </modeling/geometry_nodes/curve/resample_curve>` node.

The resolution control the accuracy of operations like trimming or sampling a curve. 
Higher resolutions are more accurate, but slower.

The input node for this data is the :doc:`Spline Resolution node </modeling/geometry_nodes/curve/spline_resolution>`.


Inputs
======

Geometry
   Standard geometry input, containing a curve.

Selection
   Whether or not to change the resolution value on each spline. True values mean the value will be changed,
   false values mean the resolution will remain the same.

Resolution
   The number of evaluated points generated for each control point in NURBS and Bezier splines.

Properties
==========

This node has no properties.

Outputs
=======

Geometry
   Standard geometry output, containing a curve.

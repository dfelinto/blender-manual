.. index:: Geometry Nodes; Set Spline Resolution
.. _bpy.types.GeometryNodeSetSplineResolution:

**************************
Set Spline Resolution Node
**************************

.. figure:: /images/node-types_GeometryNodeSetSplineResolution.webp
   :align: right
   :alt: Set Spline Resolution node.

The *Set Spline Resolution* node sets the value for how many evaluated points should be generated on the curve for
every control point. It only has an effect on :term:`NURBS` and :term:`Bézier` splines. The evaluated points
are displayed in the viewport, used in the :doc:`/modeling/geometry_nodes/curve/curve_to_mesh` node,
and optionally used in the :doc:`/modeling/geometry_nodes/curve/resample_curve`.

The input node for this data is the :doc:`/modeling/geometry_nodes/curve/spline_resolution`.


Inputs
======

Curve
   Standard geometry input.

Selection
   Whether or not to change the resolution value on each spline. True values mean the value will be changed,
   false values mean the resolution will remain the same.

Resolution
   The number of evaluated points generated for each control point in NURBS and Bézier splines.
   It controls the accuracy of operations like trimming or sampling a curve.
   Higher resolutions are more accurate, but slower.


Properties
==========

This node has no properties.


Outputs
=======

Curve
   Standard geometry output.

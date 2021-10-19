.. index:: Geometry Nodes; Resample Curve
.. _bpy.types.GeometryNodeResampleCurve:

*******************
Resample Curve Node
*******************

.. figure:: /images/modeling_geometry-nodes_curve_resample-curve_node.png
   :align: center

   The Resample Curve node.

The Resample Curve node creates a poly spline for each input spline.
In the new poly splines, the control points will have uniform spacing.

.. tip::

   Use a field as an input to have a different count/length for each spline.


Inputs
======

Geometry
   Standard geometry input.

Count
   The number of control points on the new splines.

Length
   The approximate length between the control points of the new splines.
   
   .. tip::

      A :doc:`Resample Curve </modeling/geometry_nodes/curve/trim_curve>` node can be used with a multiple of the
      input length to make the distance between each sampled point exact, even when the length of the spline changes.



Properties
==========

Mode
   How to specify the amount of samples.

   :Count:
      Sample the specified number of points along each spline.
   :Length:
      Calculate the number of samples by splitting each spline into segments with the specified length.
      The length will be rounded down so that a whole number of samples will fit in each input spline.
   :Evaluated:
      Evaluate the spline's points based on the resolution attribute for NURBS and Bézier splines.
      Changes nothing for poly splines.


Outputs
=======

Geometry
   Standard geometry output.

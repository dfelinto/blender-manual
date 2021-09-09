.. index:: Geometry Nodes; Curve Trim
.. _bpy.types.GeometryNodeCurveTrim:

**********
Curve Trim
**********

.. figure:: /images/modeling_geometry-nodes_curve_curve-trim_node.png
   :align: center

   The *Curve Trim* node.

The *Curve Trim* node shortens each spline in the curve by removing sections at
the start and end of each spline.

Bézier splines will still be Bézier splines in the output, with the first and last control point and
its handles moved as necessary to preserve the shape.
NURBS splines will be transformed into poly splines in order to be trimmed.


Inputs
======

Curve
   Standard geometry input with a curve component.

Start
   The factor or length used to determine where to start each output spline.

End
   The factor or length used to determine where to end each output spline.


Properties
==========

Mode
   How to find endpoint positions for the trimmed spline.

   :Factor:
      Find the endpoint positions using a factor of each spline's length.
      The input values should be between 0 or 1.
   :Length:
      Find the endpoint positions using a length from the start of each spline.
      The input values should be between 0 and the length of the splines.


Outputs
=======

Curve
   Standard geometry output.

.. index:: Geometry Nodes; Spline Resolution
.. _bpy.types.GeometryNodeInputSplineResolution:

**********************
Spline Resolution Node
**********************

.. figure:: /images/modeling_geometry-nodes_curve_spline-resolution_node.png
   :align: right

   Spline Resolution Node

The *Spline Resolution* outputs the number of evaluated curve points that will be generated for
every control point on the spline. This node works for NURBS and Bezier splines, for poly splines, there
is a one-to-one correspondence between original points and evalauted points, so the resulution will not
have a real value.

On Bezier splines, the resolution does not have an effect on segments in between vector handles, since
there are no extra evaluated points between the neighboring control points.


Inputs
======

This node has no inputs.

Properties
==========

This node has no properties.

Outputs
=======

Resolution
   The integer resolution value for each spline.
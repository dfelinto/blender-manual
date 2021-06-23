.. index:: Geometry Nodes; Curve to Point
.. _bpy.types.GeometryNodeCurveToPoints:

***************
Curve to Points
***************

.. figure:: /images/modeling_geometry-nodes_curve_curve-to-points_node.png
   :align: center

   The Curve to Points node.

The *Curve to Points* node samples points on all splines of a curve.
The generated points have a ``tangent``, ``normal`` and ``rotation`` attribute that can be used for instancing.

.. note::

   The radius of the generated points the radius of the curve divided by 10.


Inputs
======

Geometry
   Standard geometry input.

Count
   Number of points to sample on each spline.

Length
   Approximate distance between the sampled points on each spline.


Properties
==========

Mode
   :Evaluated:
      Output the points that make up the visible curve.
      This takes the built-in ``resolution`` attribute into account.
      It is the fastest method but in most cases the points will not have an equal distance.
   :Count:
      Sample the given amount of points on each spline. The points will have an equal distance along the spline.
   :Length:
      Calculate the number of samples by splitting each spline into segments with the specified length.
      The length will be rounded down so that a whole number of samples will fit in each input spline.


Outputs
=======

Geometry
   Standard geometry output.

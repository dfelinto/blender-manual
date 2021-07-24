.. index:: Geometry Nodes; Curve Endpoints
.. _bpy.types.GeometryNodeCurveEndpoints:

***************
Curve Endpoints
***************

.. figure:: /images/modeling_geometry-nodes_curve_curve-endpoints_node.png
   :align: right

   The Curve Endpoints node.

The *Curve Endpoints* node creates a point cloud containing either the start or end points from every spline.
The generated points have a ``tangent``, ``normal`` and ``rotation`` attribute that can be used for instancing.

.. note::

   The radius of the generated points is the radius of the curve divided by 10.


Inputs
======

Geometry
   Standard geometry input with a curve component.


Properties
==========

This node has no properties.


Outputs
=======

Start Points
   The points from the starts of each spline.

End Points
   The points from the ends of each spline.



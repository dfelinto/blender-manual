.. index:: Geometry Nodes; Star
.. _bpy.types.GeometryNodeCurveStar:

****
Star
****

.. figure:: /images/modeling_geometry-nodes_curve-primitives_star_node.png
   :align: right

   Star Node.

The *Star* node generates a poly spline in a star pattern by connecting alternating points of two circles.
The points on the inner circle are offset by a rotation so that they lie in between the points on the outer circle.
This offset can be changed with the twist input.


Inputs
======

Points
   Number of points on each of the circles.

Inner Radius, Outer Radius
   Radii of the two circles.
   The inner radius can be bigger than the outer radius.

Twist
   Angle offset of the inner circle.
   The twist value rotates the points on the circle corresponding with the inner radius
   counterclockwise by the given angle.


Properties
==========

This node has no properties.


Outputs
=======

Curve
   Poly spline generated from the inputs.

.. index:: Geometry Nodes; Set Curve Normal
.. _bpy.types.GeometryNodeSetCurveNormal:

*********************
Set Curve Normal Node
*********************

.. figure:: /images/node-types_GeometryNodeSetCurveNormal.webp
   :align: right
   :alt: Set Curve Normal node.

The *Set Curve Normal* controls the method used to calculate curve normals for every curve.

The node doesn't set the normals directly, those are calculated later as necessary.
Combined with the :doc:`tilt </modeling/geometry_nodes/curve/curve_tilt>` attribute value
at each control point, this will define the final normals accessible with the
:doc:`/modeling/geometry_nodes/input/normal`.

Internally this node adjusts the values of the ``normal_mode`` attribute on each curve.


Inputs
======

Curve
   Standard geometry input, containing curves.

Selection
   Whether or not to change the value on each curve.


Properties
==========

Mode
   The method for evaluation of the curve's normals

   :Minumum Twist:
      The final normals are calculated to have the smallest twist around
      the curve tangent across the whole curve.
   :Z-Up:
      The final normals are calculated so that they is perpendicular to the Z axis and the tangent.
      If a series of points is vertical, the X axis is used


Outputs
=======

Curve
   Standard geometry output.

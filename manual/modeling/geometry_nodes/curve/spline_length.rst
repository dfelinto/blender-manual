.. index:: Geometry Nodes; Spline Length
.. _bpy.types.GeometryNodeSplineLength:

******************
Spline Length Node
******************

.. figure:: /images/modeling_geometry-nodes_curve_spline-length_node.png
   :align: right

   Spline Length Node

The *Spline Length* node outputs the total length of each spline. This is different than the
:doc:`Curve Length </modeling/geometry_nodes/curve/curve_length>` node, which adds up the total
length for all of the curve's splines.

The output values correspond to the spline domain, but the node can be used to output a value for every
curve control point as well.


Inputs
======

This node has no inputs.

Properties
==========

This node has no properties.

Outputs
=======

Length
   The length of each spline.
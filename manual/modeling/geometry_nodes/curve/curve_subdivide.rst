.. index:: Geometry Nodes; Curve Subdivide
.. _bpy.types.GeometryNodeCurveSubdivide:

***************
Curve Subdivide
***************

.. figure:: /images/modeling_geometry-nodes_curve_curve-subdivide_node.png
   :align: center

   The Curve Subdivide node.

The *Curve Subdivide* node cuts spline segments without changing their shape.


Inputs
======

Geometry
   Standard geometry input.

Cuts
   Number of times each segment is cut.


Properties
==========

Cuts Type
   :Integer:
      Cut all segments with the same number of cuts.
   :Attribute:
      Use an attribute to determine the number of cuts for each segment.
      The number of cuts of a segment is determined by the attribute value of the previous point.


Outputs
=======

Geometry:
   Standard geometry output.

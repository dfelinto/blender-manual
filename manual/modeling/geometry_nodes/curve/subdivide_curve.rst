.. index:: Geometry Nodes; Subdivide Curve
.. _bpy.types.GeometryNodeSubdivideCurve:

********************
Subdivide Curve Node
********************

.. figure:: /images/modeling_geometry-nodes_curve_curve-subdivide_node.png
   :align: center

   The Subdivide Curve node.

The *Subdivide Curve* node cuts spline segments without changing their shape.


Inputs
======

Geometry
   Standard geometry input.

Cuts
   Number of times each segment is cut.
   When the input is a field, the number of cuts for a segment is determined by
   the value of the field when evaluated at the previous point.

Outputs
=======

Geometry:
   Standard geometry output.

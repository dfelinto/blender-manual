.. index:: Geometry Nodes; Set Spline Cyclic
.. _bpy.types.GeometryNodeSetSplineCyclic:

**********************
Set Spline Cyclic Node
**********************

.. figure:: /images/modeling_geometry-nodes_curve_set-spline-cyclic_node.png
   :align: right

   Set Spline Cyclic Node

The *Set Spline Cyclic* controls whether each spline will loop back on itself.
Each spline has the same number of control points whether or not it is set as cyclic, but
when displaying in the viewport and for operations with other nodes, a connection will be made
between the first and last control points.
The input node for this data is the :doc:`</modeling/geometry_nodes/curve/is_spline_cyclic>`.



Inputs
======

Geometry
   Standard geometry input, containing a curve.

Selection
   Whether or not to change the cyclic value on each spline. True values mean the value will be changed,
   false values mean the value will remain the same.

Cyclic
   Whether or not to join the first and last points of each spline.

Properties
==========

This node has no properties.

Outputs
=======

Geometry
   Standard geometry input, containing a curve.

.. index:: Geometry Nodes; Is Spline Cyclic
.. _bpy.types.GeometryNodeInputSplineCyclic:

*********************
Is Spline Cyclic Node
*********************

.. figure:: /images/modeling_geometry-nodes_curve_is-spline-cyclic_node.png
   :align: right

   Is Spline Cyclic node.

The *Is Spline Cyclic* controls whether each of the curve splines start and endpoints form a connection.
The output corresponds to the built-in ``cyclic`` attribute on the curve spline domain.
The node to set this data is the :doc:`Set Spline Cyclic </modeling/geometry_nodes/curve/set_spline_cyclic>` node.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Cyclic
   Whether the spline is cyclic.

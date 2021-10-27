.. index:: Geometry Nodes; Reverse Curve
.. _bpy.types.GeometryNodeReverseCurve:

******************
Reverse Curve Node
******************

.. figure:: /images/modeling_geometry-nodes_curve_curve-reverse_node.png
   :align: center

   The Reverse Curve node.

The *Reverse Curve* node swaps the start and end of splines.
The shape of the splines is not changed.

.. tip::

   When used on the *Profile* input of the :doc:`/modeling/geometry_nodes/curve/curve_to_mesh`,
   this node fill flip the normals of the resulting mesh.


Inputs
======

Curve
   Standard geometry input.

Selection
   The points whose splines are reversed.


Properties
==========

This node has no properties.


Outputs
=======

Curve
   Standard geometry output.

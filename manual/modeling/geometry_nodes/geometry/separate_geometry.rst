.. index:: Geometry Nodes; Separate Geometry
.. _bpy.types.GeometryNodeSeparateGeometry:

**********************
Separate Geometry Node
**********************

.. figure:: /images/modeling_geometry-nodes_point_point-separate_node.png
   :align: right

   The Separate Geometry node.

The *Point Separate* node produces two geometry outputs. Based on the *Mask* input,
the point cloud component of the input geometry is split between the two outputs.

.. tip::

   This node can be combined with
   the :doc:`Compare Floats </modeling/geometry_nodes/utilities/compare_floats>` node
   for a more precise control of which points are separated to a given output geometry.


Inputs
======

Mask
   The name of the attribute used to calculate which geometry output each point will belong to.
   Any value of true will move the point to the second output,
   and any value of false will move the point to the first output.
   If the attribute data type is not Boolean, the value will be implicitly converted,
   such that negative values are false and positive values are true.


Properties
==========

This node has no properties.


Outputs
=======

Geometry 1
   Points with a *Mask* attribute value of "false" will be moved to the first output.

Geometry 2
   Points with a *Mask* attribute value of "true" will be moved to the second output.

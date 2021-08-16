.. index:: Geometry Nodes; Point Separate
.. _bpy.types.GeometryNodePointSeparate:

**************
Point Separate
**************

.. figure:: /images/modeling_geometry-nodes_point_point-separate_node.png
   :align: right

   The Point Separate node.

The *Point Separate* node produces two geometry outputs. Based on the *Mask* input,
the point cloud component of the input geometry is split between the two outputs.

.. tip::

   This node can be combined with
   the :doc:`Attribute Compare </modeling/geometry_nodes/attribute/attribute_compare>` node
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

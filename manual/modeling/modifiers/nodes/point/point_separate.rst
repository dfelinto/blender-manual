.. index:: Nodes; Point Separate
.. _bpy.types.GeometryNodePointSeparate:

**************
Point Separate
**************

The *Point Separate* produces two output geometries. Based on the *threshold* and the input *attribute*,
the point cloud component of the input geometry is split between the two outputs.

.. figure:: /images/modeling_modifiers_nodes_point_separate.png

   The Point Separate node.

.. Don't show this yet because there are no other data types in the geometry socket at this point.
.. .. note::

..    Every other data type in the geometry besides the point cloud will be moved to both of the 
..    outputs unchanged. For example, if the geometry contains a mesh component, the same mesh will
..    be moved to both outputs, unaffected by the split.

.. tip::

  This node can be combined with the 
  :doc:`Attribute Compare </modeling/modifiers/nodes/attribute/attribute_compare>`
  node for more precise control of which points are separated to a given output geometry.



Inputs
=======

Mask
   The name of the attribute used to calculate which geometry output each point will belong to.
   Any value of "true" will move to the second output, and any value of "false" will move the point
   to the first output.

   If the attribute has any data type besides boolean, the value will be implicitly converted, so a
   value of exactly zero is false, and any other value is true.

Outputs
=======

Geometry 1
   Points with a mask attribute value of "true" will be moved to the first input.

Geometry 2
   Points with a mask attribute value of "false" will be moved to the first input.
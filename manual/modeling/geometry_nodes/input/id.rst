.. index:: Geometry Nodes; ID
.. _bpy.types.GeometryNodeInputID:

*******
ID Node
*******

.. figure:: /images/modeling_geometry-nodes_input_input-id_node.png
   :align: right

   ID node.

The *ID* node gives an integer value indicating the stable random ID of each element on the point domain,
which is stored in the *id* attribute.

The node to set this data is the :doc:`/modeling/geometry_nodes/geometry/set_id` node.

.. node::

   Unlike other built-in attribtutes, the *id* attribute does not always exist. In that case, this
   node will output zero.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Index
   Integer value.

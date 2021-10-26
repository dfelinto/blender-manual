.. index:: Geometry Nodes; Position
.. _bpy.types.GeometryNodeInputPosition:

*************
Position Node
*************

.. figure:: /images/modeling_geometry-nodes_input_position_node.png
   :align: right

   Position node.

The *Position* node outputs a vector of each point of the geometry the node is connected to.

The node can work on geometry domains besides points. In that case, the position data will be
automatically interpolated to the new domain. For example, when used as part of the input to
the mesh :doc:`edge split </modeling/geometry_nodes/mesh/split_edges>` node, the position for each edge
will be the average position of the edges two vertices.

For instances, the output is the origin of each instance. However, if the node is for a geometry node
that adjusts data inside instances, the position output of this node will be in the local space of
each instance.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Position
   Vector that indicates the location of each element of the geometry.

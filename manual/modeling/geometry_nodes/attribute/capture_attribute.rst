.. index:: Geometry Nodes; Capture Attribute
.. _bpy.types.GeometryNodeCaptureAttribute:

**********************
Capture Attribute Node
**********************

.. figure:: /images/node-types_GeometryNodeCaptureAttribute.webp
   :align: right
   :alt: Capture Attribute node.

   Capture Attribute node.

The *Capture Attribute* node stores the result of a field on a geometry,
and outputs the data as a node socket so it can be used by other nodes.

The result is stored on the geometry just like a regular attribute with
a name, but instead of referencing it with a name, it is retrieved whenever
the socket is connected to the input of a node. Later on when evaluating the node tree,
the attribute will be removed automatically if it is no longer used.

This node is essential because field input nodes like the :doc:`/modeling/geometry_nodes/input/radius`
work in the context of the node they are connected to. Meaning that in order to pass data like ``radius``
to a geometry that doesn't have radius, an explicit node link with the output of this node must be used.

.. note::

   Because this node stores an :ref:`anonymous attribute <anonymous-attributes>` in the geometry,
   it's essential to use the geometry output for further operations in the node tree.
   The anonymous attribute will not exist for any other geometry besides the output.


Inputs
======

Geometry
   Standard geometry input.

Value
   Float or Vector input to evaluate.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

Attribute
   The result of the evaluated field, stored on the geometry.


Examples
========

.. figure:: /images/modeling_geometry-nodes_attribute_capture-attribute_example.png

Here, a noise texture is evaluated in along the path of the curve in one dimension
and rendered with a shader. The capture node is required because the output of
the :doc:`/modeling/geometry_nodes/curve/curve_to_mesh` does not have a "curve parameter",
since it is a mesh and not a curve. So, the :doc:`/modeling/geometry_nodes/curve/spline_parameter`
must be evaluated while the geometry is still a curve.

Internally, after the noise texture is evaluated on the curve,
it is automatically copied to the mesh result of the Curve to Mesh node.
This means that anywhere *Attribute* output of this node can be connected along
the same stream of geometry nodes, the internal attribute will be available.

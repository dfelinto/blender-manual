.. index:: Geometry Nodes; Attribute Mix
.. _bpy.types.GeometryNodeAttributeMix:

*************
Attribute Mix
*************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-mix_node.png
   :align: right

   Attribute Mix Node.

Mix attributes to create a new attribute.


Inputs
======

Geometry
   Standard geometry input.

A, B
   The first and second input to the mix operation.
   This can be an attribute name or a value.

Result
   Name of the attribute where the computed result is stored.
   The output attribute type is color by default.
   When the result attribute exists already, its type is not changed.


Properties
==========

Blend Type
   Operation that is performed on the inputs.

Factor, A, B
   Input type for the corresponding socket.


Output
======

Geometry
   Standard geometry output.

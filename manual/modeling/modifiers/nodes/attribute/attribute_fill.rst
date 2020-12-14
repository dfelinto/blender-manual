.. index:: Nodes; Point Separate
.. _bpy.types.GeometryNodeAttributeFill:

**************
Attribute Fill
**************

The *Attribute Fill* node simply sets the value for every element of the attribute with the input
name to the input value. If the attribute doesn't exist yet, it will be created.


.. figure:: /images/modeling_modifiers_nodes_attribute_fill.png

   The Attribute Fill node.

Properties
==========

Data Type
   The type of data to fill the attribute with.

Inputs
======

Geometry
   The geometry that is modified.

Attribute
   The name of the attribute to fill with the value.

Value
   A value of the data type to fill the attribute with.


Output
======

Geometry
   The same geometry as the input with a modified attribute.

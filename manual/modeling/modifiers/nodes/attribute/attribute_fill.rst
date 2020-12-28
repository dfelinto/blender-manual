.. index:: Nodes; Point Separate
.. _bpy.types.GeometryNodeAttributeFill:

**************
Attribute Fill
**************

.. figure:: /images/modeling_modifiers_nodes_attribute_fill.png
   :align: right
   :width: 200px

   The Attribute Fill node.

The *Attribute Fill* node sets the value for every element of the attribute
with the input name to the input value.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   The name of the attribute to fill with the value.
    If the attribute doesn't exist yet, it will be created.

Value
   A value of the data type to fill the attribute with.


Properties
==========

Data Type
   The type of data to fill the attribute with.


Output
======

Geometry
   Standard geometry output.

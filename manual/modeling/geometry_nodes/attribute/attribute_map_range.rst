.. index:: Geometry Nodes; Attribute Map Range
.. _bpy.types.GeometryNodeAttributeMapRange:

*******************
Attribute Map Range
*******************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-map_node.png
   :align: right

   The Attribute Map node.

The *Map Range* node remaps an attribute's value from a range to a target range.


Inputs
======

Attribute
   The input attribute whose value is to be remapped.
Result
   Name of the attribute where the computed result it stored.
   If an attribute with this name does not exist yet,
   a new attribute with the same data type of the *Attribute* is used.
   If it does exist, the values of the existing attribute are overridden.
From Min
   The lower bound of the range to remap from.
From Max
   The higher bound of the range to remap from.
To Min
   The lower bound of the target range.
To Max
   The higher bound of the target range.
Steps
   The number of values allowed between *To Max* and *To Max* when using *Stepped Linear* interpolation.
   A higher value will give a smoother interpolation while lower values will progressively quantize the input.
Clamp
   If enabled, the output is clamped to the target range.


Properties
==========

Attribute
   The name of the attribute to map with the value.

Data Type
   This determines the data type of the result attribute.
   This also changes the Min and Max inputs to match the data type.

Interpolation Type
   The mathematical method used to transition between gaps in the numerical inputs.

   :Linear: Linear interpolation between From Min and From Max values.
   :Stepped Linear: Stepped linear interpolation between From Min and From Max values.
   :Smooth Step: Smooth Hermite edge interpolation between From Min and From Max values.
   :Smoother Step: Smoother Hermite edge interpolation between From Min and From Max values.


Outputs
=======

Geometry
   Standard geometry output.


Example
=======

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-map_example.png

   Attribute Map node used to adjust a vertex group.

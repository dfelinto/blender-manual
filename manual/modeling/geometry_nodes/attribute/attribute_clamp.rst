.. index:: Geometry Nodes; Attribute Clamp
.. _bpy.types.GeometryNodeAttributeClamp:

***************
Attribute Clamp
***************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-clamp_node.png
   :align: right

   The Attribute Clamp node.

This node inputs one attribute and clamps the values and writes these to the result attribute.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   Name of the attribute that is to be clamped.

Result
   Name of the attribute where the computed result it stored.
   If an attribute with this name does not exist yet, a new attribute is added.
   If it does exist, the values of the attribute are overridden.

Min
   Minimum value. This socket changes according to data type selected.

Max
   Maximum value. This socket changes according to data type selected.


Properties
==========

Data Type
   This determines the data type of the result attribute.
   This also changes the Min and Max inputs to match the data type.

Operation
   This determines how the data is clamped.

   :Min Max: Constrain value between min and max.
   :Range: Constrain value between min and max, swapping inputs when min is greater than max.


Output
======

Geometry
   Standard geometry output.

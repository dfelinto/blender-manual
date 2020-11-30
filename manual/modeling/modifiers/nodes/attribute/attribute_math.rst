.. index: Nodes; Attribute; Attribute Math
.. _bpy.types.GeometryNodeAttributeMath:

**************
Attribute Math
**************

Modify an attribute with a math operation.

.. figure:: /images/modeling_modifiers_nodes_attribute-math.png
   :align: right

   Attribute Math Node.

Inputs
======

Geometry
   The geometry that is modified.

A
   The first input to the math operation.
   This is either an attribute name or number input.

B
   The second input to the math operation.
   This is either an attribute name or number input.

Result
   Name of the attribute where the computed result it stored.
   A new attribute with that name is added, if it does not exist yet.
   If it does exist, the existing attribute is overridden.

Properties
==========

Operation
   The math function to execute.

   .. note::
      This node only supports math operations on floats (not on vectors).

Type A / Type B
   Attribute
      The input is a text field that expects an attribute name.
   Float
      The input is a number field.

Output
======

Geometry
   The same geometry as the input with a modified attribute.

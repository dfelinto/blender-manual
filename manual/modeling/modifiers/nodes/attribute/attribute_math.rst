.. index:: Nodes; Attribute; Attribute Math
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
   Standard geometry input.

A, B
   The first and second input to the math operation.
   This is either an attribute name or numeric value.

Result
   Name of the attribute where the computed result it stored.
   A new attribute with that name is added, if it does not exist yet.
   If it does exist, the existing attribute is overridden.


Properties
==========

Operation
   The math function to perform.

   .. note::

      Attributes are converted implicitly to the float data type.

Type A, B
   Attribute
      The input is a text field that expects an attribute name.

   Float
      The input is a number field.


Output
======

Geometry
   Standard geometry output.

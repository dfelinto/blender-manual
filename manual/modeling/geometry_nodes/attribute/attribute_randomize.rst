.. index:: Geometry Nodes; Attribute Randomize
.. _bpy.types.GeometryNodeAttributeRandomize:

************************
Attribute Randomize Node
************************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-randomize_node.png
   :align: right
   :width: 200px

   Attribute Randomize Node.

The *Attribute Randomize* node replaces the values in an attribute
with random values within the given range.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   Name of the attribute to fill with random values.
   If there is no attribute with the given name, a new one is created.

Min
   The random value will be at least this value.

Max
   The random value will be no more than this value.

Seed
   :term:`Seed` to change the random sequence.


Properties
==========

Type
   Type of data stored in the attribute.

   :Float: Single (floating-point) value.
   :Vector: Array of three (floating-point) values.
   :Boolean: A true or false value.

Operation
   How new random attribute values relate to the existing attribute values.

   :Replace/Create: Replace the value and data type of an existing attribute, or create a new one.
   :Add: Add the random values to the existing attribute values.
   :Subtract: Subtract random values from the existing attribute values.
   :Multiply: Multiply the existing attribute values with the random values.


Outputs
=======

Geometry
   Standard geometry output.

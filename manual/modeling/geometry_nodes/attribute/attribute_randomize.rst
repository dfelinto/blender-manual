.. index:: Geometry Nodes; Attribute Randomize
.. _bpy.types.GeometryNodeAttributeRandomize:

*******************
Attribute Randomize
*******************

.. figure:: /images/modeling_modifiers_nodes_attribute-randomize.png
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
   The random value will be at least those values.

Max
   The random values will be no more than those values.

Seed
   :term:`Seed` to change the random sequence.


Properties
==========

Type
   Type of data stored in the attribute.

   Float
      Single (floating-point) value.

   Vector
      Array of three (floating-point) values.

   Boolean
      A true or false value.


Outputs
=======

Geometry
   Standard geometry output.

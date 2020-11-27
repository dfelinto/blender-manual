.. index:: Nodes; Attribute; Random Attribute
.. _bpy.types.GeometryNodeRandomAttribute:

****************
Random Attribute
****************

Populate an attribute randomly within a given range.

.. figure:: /images/modeling_modifiers_nodes_random-attribute.png
   :align: right

   Random Attribute Node.

Inputs
======

Attribute
   Name of the attribute to populate randomly.

Min
   The random value will be at least those values.

Max
   The random values will be no more than those values.

Seed
   Change the random sequence.

Properties
==========

Type
   Type of data stored in attribute

   Float
      Single (floating point) value.

   Vector
      Array of 3 (floating point) values.

Outputs
=======

Geometry
   Geometry with the attribute populated. If there was no
   attribute with the given name, a new one is created.

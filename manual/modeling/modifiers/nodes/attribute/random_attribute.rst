.. index:: Nodes; Attribute; Random Attribute
.. _bpy.types.GeometryNodeRandomAttribute:

****************
Random Attribute
****************

Populate an attribute randomly within a given range.

.. figure:: /images/modeling_modifiers_nodes_random_attribute.png
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

Domain
   Geometry component that will store the attribute (Vertex, Point)

   Vertex
      Store the attribute in the mesh vertices.

   Point
      Store the attribute in the points of point clouds.


Outputs
=======

Geometry
   Geometry with the attribute populated. If there was no
   attribute with the given name, a new one is created.

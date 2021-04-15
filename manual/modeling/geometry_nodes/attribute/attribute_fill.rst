.. index:: Geometry Nodes; Attribute Fill
.. _bpy.types.GeometryNodeAttributeFill:

**************
Attribute Fill
**************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-fill_node.png
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

Domain
   Domain of the output attribute.

   :Auto: Chooses the domain of the attribute if it exists already, otherwise it uses the *Point* domain.
   :Point: Store the resulting attribute per point.
   :Edge: Store the resulting attribute per edge.
   :Face: Store the resulting attribute per face.
   :Face Corner: Store the resulting attribute per face corner.

Data Type
   The type of data to fill the attribute with.


Output
======

Geometry
   Standard geometry output.

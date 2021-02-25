.. index:: Geometry Nodes; Attribute Separate XYZ

**********************
Attribute Separate XYZ
**********************

.. figure:: /images/modeling_modifiers_nodes_attribute-separate-xyz.png
   :align: right

   Attribute Separate XYZ Node.

The *Attribute Separate XYZ Node* splits a vector into its individual components.


Inputs
======

Geometry
   Standard geometry input.

Vector
   The vector to split into components. This can be a vector attribute or a vector.

Result X, Result Y, Result Z
   The names of the attributes to store the components of the input vector.
   A new attribute with that name is added if it does not exist yet.
   If it does exist, the values of the existing attribute are overridden.

   The resulting components will be float attributes.


Properties
==========

Type
   Attribute
      The input is a text field that expects an attribute name.
      The type of the attribute should be vector.
   Vector
      The input is a vector of three float numbers.


Output
======

Geometry
   Standard geometry output.


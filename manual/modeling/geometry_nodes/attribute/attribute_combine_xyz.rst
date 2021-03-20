.. index:: Geometry Nodes; Attribute Combine XYZ

*********************
Attribute Combine XYZ
*********************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-combine-xyz_panel.png
   :align: right

   Attribute Combine XYZ Node.

The *Attribute Combine XYZ Node* combines a vector attribute from individual components.


Inputs
======

Geometry
   Standard geometry input.

X, Y, Z
   The inputs to the components of the vector.
Result
   The name of the attribute where the computed vector is stored.
   A new attribute with that name is added if it does not exist yet.
   If it does exist, the values of the existing attribute are overridden.

.. note::

   The resulting vector is not normalized.


Properties
==========

X, Y, Z
   Attribute
      The input is a text field that expects an attribute name.
   Float
      The input is a float number.


Output
======

Geometry
   Standard geometry output.


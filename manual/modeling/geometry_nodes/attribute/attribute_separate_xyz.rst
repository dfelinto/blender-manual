.. index:: Geometry Nodes; Attribute Separate XYZ

***************************
Attribute Separate XYZ Node
***************************

.. warning::

   This node is considered legacy and will be removed in Blender 4.0.

   Please use the :doc:`/modeling/geometry_nodes/vector/separate_xyz` instead.

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-separate-xyz_node.png
   :align: right

   Attribute Separate XYZ Node.

The *Attribute Separate XYZ Node* splits a vector into its individual components.


Inputs
======

Geometry
   Standard geometry input.

Vector
   The vector to split into components. This can be an attribute name or a vector.

Result X, Result Y, Result Z
   The names of the attributes to store the components of the input vector.
   A new attribute with that name is added if it does not exist yet.
   If it does exist, the values of the existing attribute are overridden.


Properties
==========

Type
   :Attribute: The input is a text field that expects an attribute name.
   :Vector: The input is a vector of three float numbers.


Output
======

Geometry
   Standard geometry output.

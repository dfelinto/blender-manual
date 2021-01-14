.. index:: Geometry Nodes; Point
.. _bpy.types.GeometryNodePointScale:

***********
Point Scale
***********

.. figure:: /images/modeling_modifiers_nodes_point-scale.png
   :align: right

   The Point Scale node.

The *Point Scale Node* changes the *scale* attribute of every point in the geometry
by the specified amount, either from the attribute input or a vector input. 

This node is provided for convenience, as it's equivalent to using the
:doc:`Attribute Vector Math Node </modeling/modifiers/nodes/attribute/attribute_vector_math>`
with the *multiply* operation and the *scale* attribute.

The *scale* attribute is used by the
:doc:`Point Instance Node </modeling/modifiers/nodes/point/point_instance>`
to determine the size of every instanced object or collection.

Properties
==========

Type
    Attribute
       Use the values from the attribute to move each point by a different amount.
    Vector
       Use a single vector to translate every single point. Equivalent to the 
       :doc:`Transform Node </modeling/modifiers/nodes/geometry/transform>`.

Inputs
======

Geometry
   Standard geometry input.

Translation
   The attribute or vector input.

Output
======

Geometry
   Standard geometry output.

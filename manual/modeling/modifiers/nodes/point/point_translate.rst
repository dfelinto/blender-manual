.. index:: Geometry Nodes; Point
.. _bpy.types.GeometryNodePointTranslate:

***************
Point Translate
***************

.. figure:: /images/modeling_modifiers_nodes_point-translate.png
   :align: right

   The Point Translate node.

The *Point Translate Node* moves every point of the geometry by the specified amount,
either from the attribute input or a vector input.
This node is provided for convenience, as it's equivalent to using the
:doc:`Attribute Vector Math Node </modeling/modifiers/nodes/attribute/attribute_vector_math>`
with the *Addition* operation and the *position* attribute.


Inputs
======

Geometry
   Standard geometry input.

Translation
   The attribute or vector input.


Properties
==========

Type
   Attribute
      Use the values from the attribute to move each point by a different amount.
   Vector
      Use a single vector to translate every single point.
      Equivalent to the :doc:`Transform Node </modeling/modifiers/nodes/geometry/transform>`.


Output
======

Geometry
   Standard geometry output.

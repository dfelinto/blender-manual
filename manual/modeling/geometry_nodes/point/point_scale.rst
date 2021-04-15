.. index:: Geometry Nodes; Point
.. _bpy.types.GeometryNodePointScale:

***********
Point Scale
***********

.. figure:: /images/modeling_geometry-nodes_point_point-scale_node.png
   :align: right

   The Point Scale node.

The *Point Scale* node changes the *scale* attribute of every point in the geometry
by the specified amount, either from the attribute input or a vector input.
This node is provided for convenience, as it's equivalent to using
the :doc:`Attribute Vector Math Node </modeling/geometry_nodes/attribute/attribute_vector_math>`
with the *Multiply* operation and the *scale* attribute.

The *scale* attribute is used by the :doc:`Point Instance Node </modeling/geometry_nodes/point/point_instance>` to
determine the size of every instanced object or collection.


Inputs
======

Geometry
   Standard geometry input.

Translation
   The attribute or vector input.


Properties
==========

Type
   :Attribute:
      Use the values from the attribute to move each point by a different amount.
   :Float:
      Use a single value to translate every single point. This is a shortcut for assigning the same value
      for the X, Y, and Z components of the vector input, and allows adjusting the scale in a uniform way.
   :Vector:
      Use a single vector to translate every single point.
      Equivalent to the :doc:`Transform Node </modeling/geometry_nodes/geometry/transform>`.


Output
======

Geometry
   Standard geometry output.

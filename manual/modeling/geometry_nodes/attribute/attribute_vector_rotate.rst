.. index:: Geometry Nodes; Attribute Vector Rotate
.. _bpy.types.GeometryNodeAttributeVectorRotate:

***********************
Attribute Vector Rotate
***********************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-vector-rotate_node.png
   :align: right
   :width: 300px

   The Attribute Vector Rotate Node.

The *Attribute Vector Rotate Node* provides the ability to rotate a vector attribute around a pivot point (*Center*).


Inputs
======

Geometry
   Standard geometry input.

Vector
   The name of the vector attribute that will be rotated.

Center
   Point to rotate around.

Axis
   The axis used for the *Axis Angle* mode.

Angle
   The name of the attribute used for the rotation angle.

Rotation
   The rotation for the *Euler* mode.

Invert
   Inverts the rotation angle.


Properties
==========

Mode
   The type of angle input.

   :X, Y, Z Axis:
      Rotates the vector around the given axis.
      The amount of rotation is defined by the *Angle* input.
   :Axis Angle:
      Rotates the vector around any arbitrary axis defined by the *Axis* input vector attribute.
      The amount of rotation is defined by the *Angle* input attribute.
   :Euler:
      Rotates the vector about the *Center* input values with the *Rotation*
      input vector values to control the amount of rotation on each axis.

Vector, Center, Axis, Angle, Rotation
   :Attribute: A text field to input an attribute name.
   :Vector: The input is a vector of three float numbers.
   :Float: The input is a number field.


Output
======

Geometry
   Standard geometry output.

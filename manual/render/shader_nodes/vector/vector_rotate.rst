.. _bpy.types.ShaderNodeVectorRotate:

******************
Vector Rotate Node
******************

.. figure:: /images/render_shader-nodes_vector_vector-rotate_node.png
   :align: right

   Vector Rotate Node.

The *Vector Rotate Node* provides the ability to rotate a vector around a pivot point (*Center*).


Inputs
======

Vector
   Vector to be rotated.

Center
   Point to rotate around.


Properties
==========

Type
   Axis Angle
      Rotates the vector around an axis defined by the *Axis* input vector
      and the amount of rotation is defined by the *Angle* input.
   X, Y, Z Axis
      Rotates the vector around the defined axis and
      the amount of rotation is defined by the *Angle* input.
   Euler
      Rotates the vector about the *Center* and defined by the *Rotation*
      input vector to control the amount of rotation on each axis.
Invert
   Inverts the rotation angle.


Outputs
=======

Vector
   The rotated vector.


Examples
========

.. figure:: /images/render_shader-nodes_vector_vector-rotate_example.png
   :align: right

   Vector Rotate node example.

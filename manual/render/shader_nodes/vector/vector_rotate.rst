.. _bpy.types.ShaderNodeVectorRotate:

.. Editors Note: This page gets copied into:
.. - :doc:`</modeling/geometry_nodes/vector/vector_rotate>`

.. --- copy below this line ---

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
   The type of angle input.

   :X, Y, Z Axis:
      Rotates the vector around the defined axis and
      the amount of rotation is defined by the *Angle* input.
   :Axis Angle:
      Rotates the vector around any arbitrary axis defined by the *Center* input vector.
      The amount of rotation is defined by the *Angle* input.
   :Euler:
      Rotates the vector about a center point defined by the *Center* input vector.
      The amount of rotation on each axis is defined by the *Rotation* input vector.
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

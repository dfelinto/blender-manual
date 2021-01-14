.. index:: Geometry Nodes; Point
.. _bpy.types.GeometryNodeAlignRotationToVector:

************************
Align Rotation to Vector
************************

.. figure:: /images/modeling_modifiers_nodes_align-rotation-to-vector.png
   :align: right

   The Align Rotation to Vector node.

The *Align Rotation to Vector* node rotates points into the given direction.
It does so by modifying the *rotation* attribute.

Properties
==========

Axis
   Local axis of the object that is to be rotated towards the vector input.

Factor
   Type of the *Factor* input socket.

Vector
   Type of the *Vector* input socket.

Inputs
======

Geometry
   Standard geometry input.

Factor
   Determines how much the points are rotated towards the vector.
   Zero effectively disables the node and one means that the points are aligned with the vector perfectly.

Vector
   The direction vector that points should be rotated to.
   The vector is in the local space of the object that is being modified.
   When it is all zeros for a point, it is not rotated at all.

Outputs
=======

Geometry
   Standard geometry output.

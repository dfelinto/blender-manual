.. index:: Geometry Nodes; Align Euler to Vector
.. _bpy.types.GeometryNodeAlignEulerToVector:

**************************
Align Euler to Vector Node
**************************

.. figure:: /images/modeling_geometry-nodes_point_align-euler-to-vector_node.png
   :align: center

   The Align Euler to Vector node.

The *Align Euler to Vector* node rotates an Euler rotation into the given direction.


Inputs
======

Rotation
   The :term:`Euler` rotation to align.

   .. important::

      This input has to be a rotation input. Be careful not to connect a direction vector
      like the :doc:`normal </modeling/geometry_nodes/input/normal>`.

Factor
   Determines how much the points are rotated towards the vector.
   Zero effectively disables the node and one means that the points are aligned with the vector perfectly.

Vector
   The direction vector that points should be rotated to.
   The vector is in the local space of the object that is being modified.
   When it is all zeros for a point, it is not rotated at all.


Properties
==========

Axis
   Local axis of the object that is to be rotated towards the vector input.

Pivot
   The local axis to rotate around.

   :Auto:
      The best rotation angle is computed automatically.
      This minimizes the angle of rotation.
   :X, Y, Z:
      Rotate around a specific local axis.


Outputs
=======

Rotation
   The rotated Euler rotation.

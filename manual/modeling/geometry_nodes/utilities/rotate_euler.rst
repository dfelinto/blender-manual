.. index:: Geometry Nodes; Rotate Euler
.. _bpy.types.GeometryNodeRotateEuler:

*****************
Rotate Euler Node
*****************

.. figure:: /images/modeling_geometry-nodes_utilities_rotate-euler_node.png
   :align: right

   The Rotate Euler Node

The *Rotate Euler* node rotates an euler rotation.


Inputs
======

Rotation
   The euler rotation to rotate.

Rotate By
   Specifies how much an euler rotation is rotated. This input is only available when the rotation type is set to *Euler*.

Axis
	This axis to rotate around. This input is only available when the rotation type is set to *Axis Angle*.

Angle
	The angle to rotate by around the specified axis. This input is only available when the rotation type is set to *Axis Angle*.

Properties
==========

Rotation Type
   :Axis Angle: Use separate axis and angle inputs to control the rotation.
   :Euler: Use an euler input to control the rotation.

Space
   :Object: Rotate an euler rotation in the evaluated object's space.
   :Local: Rotate an euler rotation in local space.

Outputs
=======

Rotation
   The rotated euler rotation.

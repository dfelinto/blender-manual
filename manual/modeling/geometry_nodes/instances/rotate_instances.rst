.. index:: Geometry Nodes; Rotate Instances
.. _bpy.types.GeometryNodeRotateInstances:

*********************
Rotate Instances Node
*********************

.. figure:: /images/modeling_geometry-nodes_instances_rotate-instances_node.png
   :align: right

   The Rotate Instances node.

The *Rotate Instances* node rotates geometry instances in local or global space.

The :doc:`/modeling/geometry_nodes/instances` page contains more information about geometry instances.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field used to determine if an instance will be rotated.

Rotation
   The :term:`Euler` rotation to rotate the instances by.

Pivot Point
   The position around which each instance is rotated. If the *Local Space* input is true,
   the location is relative to the initial transform of the instance.

Local Space
   If enabled, the instances are rotated in local space. In other words,
   they are rotated around the axes described by the initial transform of each instance.
   When the input is disabled, the pivot point and rotation are specified in
   the local space of the modifier object.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

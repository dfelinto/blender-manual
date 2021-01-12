.. index:: Geometry Nodes; Object Info
.. _bpy.types.GeometryNodeObjectInfo:

***********
Object Info
***********

.. figure:: /images/modeling_modifiers_nodes_object-info.png
   :align: right

   Object Info Node.

The *Object Info* node gets information from objects.
This can be useful to bring an external object to control parameters in the geometry node tree,
either directly by using its geometry, or via its transformation parameters.


Inputs
======

Object
   Object to get the properties from.


Properties
==========

This node has no properties.


Outputs
=======

Location
   Location of the object in world space.
Rotation
   Rotation of the object in world space.
Scale
   Scale of the object in world space.

Geometry
   Geometry of the object in world space with all its modifiers applied.

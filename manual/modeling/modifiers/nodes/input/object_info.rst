.. index:: Nodes; Input; Object Info
.. _bpy.types.GeometryNodeObjectInfo:

***********
Object Info
***********

The *Object Info* node gets information from objects.

.. figure:: /images/modeling_modifiers_nodes_object_info.png

   Object Info Node.

This can be useful to bring an external object to control parameters in the geometry node tree,
either directly by using its geometry, or via its transformation parameters.


Inputs
======

Object
    Object to get the properties from.

.. note::

   An object input is always required.


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

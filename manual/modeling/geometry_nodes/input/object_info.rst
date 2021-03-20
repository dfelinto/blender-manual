.. index:: Geometry Nodes; Object Info
.. _bpy.types.GeometryNodeObjectInfo:

***********
Object Info
***********

.. figure:: /images/modeling_geometry-nodes_input_object-info_node.png
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

Transform Space
   The transformation of the vector and geometry outputs.

   Original
      Output the geometry relative to the input object transform, and the location,
      rotation and scale relative to the world origin.
   Relative
      Bring the input object geometry, location, rotation and scale into the modified object,
      maintaining the relative position between the two objects in the scene.


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

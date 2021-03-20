.. index:: Geometry Nodes; Transform
.. _bpy.types.GeometryNodeTransform:

*********
Transform
*********

.. figure:: /images/modeling_geometry-nodes_geometry_transform_panel.png
   :align: right

   The Transform node.

The *Transform Node* allows you to move, rotate or scale the geometry.
The transformation is applied to the entire geometry, and not per element.
For example, rotation with this node will change the location of each point
rather than changing the rotation of individual points. For that, the *Point Rotate* node can be used.


Inputs
======

Geometry
   Standard geometry input.

Translation
   Translates the geometry in the local space of the modified object.
Rotation
   Euler rotation in local space.
Scale
   Scale to transform the geometry in local space.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.

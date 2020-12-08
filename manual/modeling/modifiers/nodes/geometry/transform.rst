.. index:: Nodes; Transform
.. _bpy.types.GeometryNodeTransform:

*********
Transform
*********

.. figure:: /images/modeling_modifiers_nodes_transform.png
   :align: right

   Transform modifier node.

The *Transform Node* allows you to move, rotate or scale the geometry.
The transformation is applied to the entire geometry, and not per element.
For example, you can not rotate individual point cloud points with this node.


Inputs
======

Geometry
   Standard geometry input.

Translation
   Translates the geometry in local space of the modified object.
Rotation
   Euler rotation in local space.
Scale
   Scale to transform the geometries in local space.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.

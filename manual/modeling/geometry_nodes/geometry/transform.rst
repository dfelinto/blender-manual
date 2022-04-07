.. index:: Geometry Nodes; Transform
.. _bpy.types.GeometryNodeTransform:

**************
Transform Node
**************

.. figure:: /images/node-types_GeometryNodeTransform.webp
   :align: right
   :alt: Transform node.

The *Transform Node* allows you to move, rotate or scale the geometry.
The transformation is applied to the entire geometry, and not per element.
The :doc:`/modeling/geometry_nodes/geometry/set_position` is used for moving
individual points of a geometry. For transforming instances individually, the instance
:doc:`translate </modeling/geometry_nodes/instances/translate_instances>`,
:doc:`rotate </modeling/geometry_nodes/instances/translate_instances>`, or
:doc:`scale </modeling/geometry_nodes/instances/translate_instances>`
nodes can be used.


Inputs
======

Geometry
   Standard geometry input.

Translation
   Translation of the entire geometry in the local space of the modified object.

Rotation
   Euler rotation in the local space of the modified object.

Scale
   Scale for the geometry in the local space of the modified object.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.

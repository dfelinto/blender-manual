.. index:: Nodes; Mesh; Point Instance
.. _bpy.types.GeometryNodePointInstance:

**************
Point Instance
**************

.. figure:: /images/modeling_modifiers_nodes_point-instance.png
   :align: right

   The Point Instance Node.

The *Point Instance* node instances an element to each of the points present in the input geometry.
It works for both point cloud and mesh vertices.

.. warning::

   Because the output geometry is only a set of instances objects or collections, the *Attribute* nodes
   will not work on the output of this node. The location, rotation, and scale of individual points should
   be adjusted before this node.


Inputs
======

Geometry
   Standard geometry input.
   The **location**, **rotation**, and **scale** or **radius** attributes affect the transform of each instanced
   object.

Object
   The object to instantiate.


Properties
==========

Type
   Object
      Instance a single object on each point.
   Collection
      Instance either an entire collection or a random choice from its objects or sub-collections.

Whole Collection
   When instancing collections, this property chooses between instancing the entire collection or
   a random choice of its objects and sub-collections.

Seed
   When "Whole Collection" is turned off, a :term:`Seed` to affect the choice of the collection's children.


Outputs
=======

Geometry
   Standard geometry output.

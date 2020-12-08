.. index:: Nodes; Mesh; Point Instance
.. _bpy.types.GeometryNodePointInstance:

**************
Point Instance
**************

.. figure:: /images/modeling_modifiers_nodes_point-instance.png
   :align: right

   Point Instance Node.

The *Point Instance* node instances an element to each of the points present in the input geometry.
It works for both point cloud and mesh vertices.

.. note::

   This node only works if the modifier belongs to a point cloud object.


Inputs
======

Geometry
   Standard geometry input.
Object
   The object to instantiate.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

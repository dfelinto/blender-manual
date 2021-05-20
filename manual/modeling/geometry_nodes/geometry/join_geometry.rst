.. index:: Geometry Nodes; Join Geometry
.. _bpy.types.GeometryNodeJoinGeometry:

*************
Join Geometry
*************

The *Join Geometry* node merges separately generated pieces of geometry into a single one.
If the geometry inputs contain different types of data, the output will also contain different data types.

.. figure:: /images/modeling_geometry-nodes_geometry_join-geometry_node.png

   The Join Geometry node.

.. note::

   The node cannot handle the case when more than one geometry input has a volume component.


Materials
=========

When multiple mesh inputs contain different materials, the material slots from each mesh geometry
are merged so that the output mesh will contain all the input materials.
   

Inputs
======

Geometry
   Pieces of geometry that will be joined. Multiple inputs are allowed.
   When the node is muted, only the first link will be passed through.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.

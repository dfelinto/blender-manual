.. index:: Geometry Nodes; Join Geometry
.. _bpy.types.GeometryNodeJoinGeometry:

*************
Join Geometry
*************

The *Join Geometry* node merges separately generated pieces of geometry into a single one.
If the inputted pieces contain different types of geometry, the output will contain multiple types of geometry.

.. figure:: /images/modeling_geometry-nodes_geometry_join-geometry_node.png

   The Join Geometry node.

.. note::

   The node cannot handle the case when more than one geometry input has a volume component.


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

.. index:: Geometry Nodes; Separate Components
.. _bpy.types.GeometryNodeSeparateComponents:

************************
Separate Components Node
************************

.. figure:: /images/modeling_geometry-nodes_geometry_separate-components_node.png
   :align: center

   The Separate Components node.

The *Separate Components* node splits a geometry into its separate components.

.. note::

   If the input contains multiple volume instances, only the first volume component is moved to the output currently.


Inputs
======

Geometry
   Standard geometry input.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Mesh component of the input geometry.

Point Cloud
   Point cloud component of the input geometry.

Curve
   Curve component of the input geometry.

Volume
   Volume component of the input geometry.

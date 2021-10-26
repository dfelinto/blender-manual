.. index:: Geometry Nodes; Realize Instances
.. _bpy.types.GeometryNodeRealizeInstances:

**********************
Realize Instances Node
**********************

.. figure:: /images/modeling_geometry-nodes_instances_realize-instances_node.png
   :align: right

   Realize Instances Node

The *Realize Instances* node makes any instances (efficient duplicates of the same geometry) into real
geometry data. This makes it possible to affect each instance uniquely, whereas without this node, the
exact same changes are applied to every instance of the same geometry. However, performance can become
much worse when the input contains many instances of complex geometry, which is a fundamental limitation
when procedurally processing geometry.

.. note::

   If the input contains multiple volume instances, only the first volume component is moved to the output.


Inputs
======

Geometry
   Standard geometry input.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

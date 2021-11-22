.. index:: Geometry Nodes; Translate Instances
.. _bpy.types.GeometryNodeTranslateInstances:

************************
Translate Instances Node
************************

.. figure:: /images/modeling_geometry-nodes_instances_translate-instances_node.png
   :align: right

   The Translate Instances node.

The *Translate Instances* node moves top-level geometry instances in local or global space.

The :doc:`/modeling/geometry_nodes/instances` page contains more information about geometry instances.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field used to determine if an instance will be translated.

Translation
   The vector to translate the instances by.

Local Space
   If enabled, the instances are translated relative to their initial rotation.
   Otherwise they are translated in the local space of the modifier object.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

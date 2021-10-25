.. index:: Geometry Nodes; Capture Attribute
.. _bpy.types.GeometryNodeCaptureAttribute:

**********************
Capture Attribute Node
**********************

.. figure:: /images/modeling_geometry-nodes_attribute_capture-attribute_node.png
   :align: right

   Capture Attribute Node

The *Capture Attribute* node stores the result of a field on a geometry, and outputs the data as a node
socket so it can be used by other nodes.


Inputs
======

Geometry
   Standard geometry input

Value
   Float or Vector input to evaluate 


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   The standard geometry output

Attribute
   The result of the evaluated field, stored on the geometry.
   
.. index:: Geometry Nodes; Attribute Remove
.. _bpy.types.GeometryNodeAttributeRemove:

****************
Attribute Remove
****************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-remove_node.png
   :align: right
   :width: 200px

   The Attribute Remove node.

The *Attribute Remove* node removes a number of given attributes from each element of the given Geometry.


Inputs
======

Geometry
   Standard geometry input.

Attribute (Multi-Input)
   The name of the attribute to remove.
   Multiple attributes can be removed at once by connecting
   multiple :doc:`String Input </modeling/geometry_nodes/input/string>` nodes.
   Built-in attributes and attributes that don't exist can't be removed.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.

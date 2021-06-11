.. index:: Geometry Nodes; Delete Geometry
.. _bpy.types.GeometryNodeDeleteGeometry

***************
Delete Geometry
***************

.. figure:: /images/modeling_geometry-nodes_geometry_delete-geometry_node.png

   The Delete Geometry node.

The *Delete Geometry* node removes the part of the geometry that is selected.

For meshes, which elements are deleted depeds on the domain of the input seletion attribute.
For example, if it is a face selection, faces are removed.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Name of the attribute that is used as selection. Typically this is a boolean attribute.
   If this is empty, the node does nothing.

Invert
   Invert the selection to keep everything that is selected.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.

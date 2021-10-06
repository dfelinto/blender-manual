.. index:: Geometry Nodes; Delete Geometry
.. _bpy.types.GeometryNodeDeleteGeometry:

********************
Delete Geometry Node
********************

.. figure:: /images/modeling_geometry-nodes_geometry_delete-geometry_node.png

   The Delete Geometry node.

The *Delete Geometry* node removes the selected part of a geometry.
For meshes, which elements are deleted depends on the domain of the input selection attribute.
For example, if it is a face selection, faces are removed.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Name of the attribute that is used as selection. Typically this is a Boolean attribute.
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

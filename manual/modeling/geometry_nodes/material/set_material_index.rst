.. index:: Geometry Nodes; Set Material Index
.. _bpy.types.GeometryNodeSetMaterialIndex:

***********************
Set Material Index Node
***********************

.. figure:: /images/modeling_geometry-nodes_material_set-material-index_node.png
   :align: right
   :alt: Set Material Index node.

The *Set Material Index* node sets the material index for a geometry.

The node to get this data is the :doc:`Material Index </modeling/geometry_nodes/material/material_index>` node.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Whether to change the material index for each face.
   True values mean the material index will be changed, false values mean it will remain the same.

Material Index
   The new material index.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

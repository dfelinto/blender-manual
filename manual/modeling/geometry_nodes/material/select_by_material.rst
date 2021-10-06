.. index:: Geometry Nodes; Select by Material
.. _bpy.types.GeometryNodeSelectByMaterial:

***********************
Select by Material Node
***********************

.. figure:: /images/modeling_geometry-nodes_material_select-by-material_node.png

   The Select by Material node.

The *Select by Material* node creates a new face selection attribute.
All faces that use a particular material are added to the selection.


Inputs
======

Geometry
   Standard geometry input.

Material
   Material to select. If this is empty, all faces without a material are selected.

Selection
   Name of the selection attribute that is created.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

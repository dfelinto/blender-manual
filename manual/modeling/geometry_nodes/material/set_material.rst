.. index:: Geometry Nodes; Set Material
.. _bpy.types.GeometryNodeSetMaterial:

*****************
Set Material Node
*****************

.. figure:: /images/modeling_geometry-nodes_set-material_node.png
   :align: right

   The Set Material node.

The *Set Material* changes the material assignment in the specified selection,
by adjusting the ``material_index`` attribute. If the material is already used
on the geometry, the existing material index will be reused.

.. note::

   This node adjusts mesh and volume data, other data types do not support materials.
   However, volumes only support a single material, so this input will be ignored for volumes.


Inputs
======

Geometry
   Standard geometry input containing a mesh.

Material
   The material to apply to the geometry.

Selection
   Whether to change the material of each face.
   True values mean the material will be changed, false values mean it will remain the same.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

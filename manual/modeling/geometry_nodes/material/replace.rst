.. index:: Geometry Nodes; Material Replace
.. _bpy.types.GeometryNodeMaterialReplace:

****************
Material Replace
****************

.. figure:: /images/modeling_geometry-nodes_material_material-replace_node.png
   :align: right
   :width: 300px

   The Material Replace Node.

The *Material Replace* node swaps one material with another.
Replacing a material with this node is more efficient than creating a selection of all faces
with the old material and then using the *Material Assign* node.

.. note::

   Currently this node only adjusts mesh data.


Inputs
======

Geometry
   Standard geometry input.

Old
   Material that is going to be replaced.

New
   Material that is replacing the old material.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

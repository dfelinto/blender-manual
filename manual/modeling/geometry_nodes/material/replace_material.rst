.. index:: Geometry Nodes; Replace Material
.. _bpy.types.GeometryNodeReplaceMaterial:

*********************
Replace Material Node
*********************

.. figure:: /images/modeling_geometry-nodes_material_replace_node.png
   :align: right
   :width: 300px
   :alt: Replace Material Node.

The *Replace Material* node swaps one material with another.
Replacing a material with this node is more efficient than creating a selection of all faces
with the old material with the :doc:`/modeling/geometry_nodes/material/material_selection`
and then using the :doc:`/modeling/geometry_nodes/material/set_material`.

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

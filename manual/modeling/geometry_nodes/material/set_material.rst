.. index:: Geometry Nodes; Set Material
.. _bpy.types.GeometryNodeSetMaterial:

*****************
Set Material Node
*****************

.. figure:: /images/modeling_geometry-nodes_material_assign_node.png
   :align: right
   :width: 300px

   The Set Material Node.

The *Set Material* changes the material assignment in the specified selection,
by adjusting the ``material_index`` attribute. If the material is already used
on the geometry, the existing material index will be reused.

.. note::

   Currently this node only adjusts mesh data.


Inputs
======

Geometry
   Standard geometry input containing a mesh.

Material
   The material to apply to the geometry.

Selection
   The name of an attribute to use to determine which parts of the geometry to assign the material to.
   The attribute will be implicitly converted to a Boolean data type if it isn't a Boolean already.
   On meshes, the attribute will be used on the face domain.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

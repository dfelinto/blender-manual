.. index:: Geometry Nodes; Material Assign
.. _bpy.types.GeometryNodeMaterial Assign:

***************
Material Assign
***************

.. figure:: /images/modeling_geometry-nodes_material_assign.png
   :align: right
   :width: 300px

   The Material Assign Node.

The *Material Assign* changes the material assignment in the specified selection.

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

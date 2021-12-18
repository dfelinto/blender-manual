.. index:: Geometry Nodes; Edge Split
.. _bpy.types.GeometryNodeEdgeSplit:

****************
Split Edges Node
****************

.. figure:: /images/modeling_geometry-nodes_mesh_split-edges_node.png
   :align: right

   The Split Edges node.

Like the :doc:`/modeling/modifiers/generate/edge_split`, the *Split Edges* node splits and duplicates edges
within a mesh, breaking 'links' between faces around those split edges.


Inputs
======

Mesh
   Standard geometry input.

Selection
   A standard Boolean selection input to determine which edges will be split.

.. note::

   Because of mesh topology requirements, sometimes more or fewer edges than are selected will be split.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Standard geometry output.

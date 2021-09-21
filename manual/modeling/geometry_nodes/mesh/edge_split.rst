.. index:: Geometry Nodes; Edge Split
.. _bpy.types.GeometryNodeEdgeSplit:

**********
Edge Split
**********

.. figure:: /images/modeling_geometry-nodes_mesh_edge-split_node.png
   :align: right

   The Edge Split Node.

Like the :doc:`/modeling/modifiers/generate/edge_split`, the *Edge Split* node splits and duplicates edges
within a mesh, breaking 'links' between faces around those split edges.

.. note::

   Splitting edges effectively breaks the mesh topology.


Inputs
======

Geometry
   Standard geometry input.

Edge Angle
   When enabled, an edge will be split if the angle between its
   two adjacent faces is greater than the *Angle*.
Angle
   On 0: all edges are split. On 180: no edges are split.
Sharp Edges
   When enabled, edges will be split if they were :ref:`marked as sharp <bpy.ops.mesh.mark_sharp>`.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.

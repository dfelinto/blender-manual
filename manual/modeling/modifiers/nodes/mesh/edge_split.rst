.. index:: Nodes; Mesh; Edge Split
.. _bpy.types.GeometryNodeEdgeSplit:

**********
Edge Split
**********

.. figure:: /images/modeling_modifiers_nodes_edge-split.png
   :align: right

   Edge Split Node.

The *Edge Split* node splits, duplicates edges within a mesh,
breaking 'links' between faces around those split edges.

The edges to split can be determined from the edge angle (i.e. angle between faces forming that edge),
and/or edges marked as sharp.

.. note::
   Splitting edges effectively breaks the mesh topology.


Inputs
======

Geometry
   Source geometry to split edges from.
Edge Angle
   When enabled, edges will be split if the angle between its
   two adjacent faces is greater than the *Split Angle*.
Angle
   On 0: all edges are split. On 180: no edges are split.
Sharp Edges
   When enabled, edges will be split if they were :ref:`marked as sharp <bpy.ops.mesh.mark_sharp>`.


Outputs
=======

Geometry
   The geometry with the edges split.

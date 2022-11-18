.. index:: Geometry Nodes; Vertex of Corner
.. _bpy.types.GeometryNodeVertexOfCorner:

*********************
Vertex of Corner Node
*********************

.. figure:: /images/node-types_GeometryNodeVertexOfCorner.webp
   :align: right
   :alt: Vertex of Corner node.

The *Vertex of Corner* node outputs the index of the vertex that a face corner is
attached to.


Inputs
======

Corner Index
   The index of the face corner.

   .. note::
      By default this uses the :doc:`index </modeling/geometry_nodes/input/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the face corner domain.


Properties
==========

This node has no properties.


Outputs
=======

Vertex Index
   The index of the vertex that the face corner is attached to.

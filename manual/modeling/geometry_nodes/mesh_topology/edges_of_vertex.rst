.. index:: Geometry Nodes; Edges of Vertex
.. _bpy.types.GeometryNodeEdgesOfVertex:

********************
Edges of Vertex Node
********************

.. figure:: /images/node-types_GeometryNodeEdgesOfVertex.webp
   :align: right
   :alt: Edges of Vertex node.

The *Edges of Vertex* node retrieves the edges connected to each vertex. Each vertex is connected 
to several edges. The node first collects a list of those edges, then sorts them based on the
*Sort Weight* input. The *Total* output is the number of edges in that list, and the *Edge Index*
output is one of those edges chosen with the *Sort Index* input.

One example use is finding the "most vertical" edge connected to each vertex.


Inputs
======

Vertex Index
   The index of the input vertex.

   .. note::
      By default this uses the :doc:`index </modeling/geometry_nodes/input/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the vertex domain.

Weights
   Values used to sort the edges connected to the vertex.
   By default the edges are sorted by index, so the edges with the smallest indices come first.

Sort Index
   Which of the sorted edges to use for the *Edge Index* output. If the value is larger than
   the total number of connected edges, it will wrap around to the beginning.


Properties
==========

This node has no properties.


Outputs
=======

Edge Index
   An edge connected to the face, chosen by the *Sort Index* input.

Total
   The number of edges connected to the vertex.


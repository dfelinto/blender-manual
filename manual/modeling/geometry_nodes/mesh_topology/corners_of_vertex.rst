.. index:: Geometry Nodes; Corners of Vertex
.. _bpy.types.GeometryNodeCornersOfVertex:

**********************
Corners of Vertex Node
**********************

.. figure:: /images/node-types_GeometryNodeCornersOfVertex.webp
   :align: right
   :alt: Corners of Vertex node.

The *Corners of Vertex* node retrieves face corners attached to each vertex.
The node first gathers a list of the corners of all faces connected to the vertex.
That list is then sorted based on the values of the *Sort Weight* input.
The *Total* output is the number of connected faces/corners, and the *Corner Index*
output is one of those corners, chosen with the *Sort Index* input.


Inputs
======

Vertex Index
   The index of the input vertex.

   .. note::
      By default this uses the :doc:`index </modeling/geometry_nodes/input/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the vertex domain.

Weights
   Values used to sort the corners connected to the vertex.
   By default the corners are sorted by index, so the corners with the smallest indices come first.

Sort Index
   Which of the sorted corners to use for the *Corner Index* output. If the value is larger than
   the total number of connected face corners, it will wrap around to the beginning.


Properties
==========

This node has no properties.


Outputs
=======

Corner Index
   An corner connected to the face, chosen by the *Sort Index* input.

Total
   The number of faces or face corners connected to the vertex.


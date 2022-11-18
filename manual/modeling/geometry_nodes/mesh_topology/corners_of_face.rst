.. index:: Geometry Nodes; Corners of Face
.. _bpy.types.GeometryCornersOfFace:

********************
Corners of Face Node
********************

.. figure:: /images/node-types_GeometryCornersOfFace.webp
   :align: right
   :alt: Corners of Face node.

The *Corners of Face* node gives access to specific corners of input faces.


Inputs
======

Face Index
   The index of the input face.

   .. note::
      By default this uses the :doc:`index </modeling/geometry_nodes/input/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the face domain.

Weights
   Values used to sort the face's corners.
   By default the corners are sorted by index, so the corners with the smallest indices come first.

Sort Index
   Which of the sorted corners to use for the *Corner Index* output. If the value is larger than
   the total number of corners, it will wrap around to the beginning.


Properties
==========

This node has no properties.


Outputs
=======

Corner Index
   The index of one of the face's corners, chosen by the *Sort Index* input.

Total
   The number of corners in the face, or its side count.

.. index:: Geometry Nodes; Face of Corner
.. _bpy.types.GeometryNodeFaceOfCorner:

*******************
Face of Corner Node
*******************

.. figure:: /images/node-types_GeometryNodeFaceOfCorner.webp
   :align: right
   :alt: Face of Corner node.

The *Face of Corner* node retrieves the face a face corner is part of.


Inputs
======

Corner Index
   The index of the input face corner.

   .. note::
      By default this uses the :doc:`index </modeling/geometry_nodes/input/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the face corner domain.


Properties
==========

This node has no properties.


Outputs
=======

Face Index
   The index of the face the corner is a part of.

Index in Face
   The index of the corner, starting from the first corner in the face.
   Each face is comprised of a list of face corners, this output is the distance
   from the start of that list. If the corner is the first in the face, the value
   will be zero. If it comes last, the value will be one less than the number of
   corners in the face.

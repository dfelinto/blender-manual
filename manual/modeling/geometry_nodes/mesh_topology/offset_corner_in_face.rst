.. index:: Geometry Nodes; Offset Corner in Face
.. _bpy.types.GeometryNodeOffsetCornerInFace:

**************************
Offset Corner in Face Node
**************************

.. figure:: /images/node-types_GeometryNodeOffsetCornerInFace.webp
   :align: right
   :alt: Offset Corner in Face node.

The *Offset Corner in Face* node retrieves other corners in the same face as
the input face corner. This is like "rotating" the input corner around in its face.

Conceptually the operation is similar to the 
:doc:`/modeling/geometry_nodes/curve_topology/offset_point_in_curve`.


Inputs
======

Corner Index
   The index of the input face corner
   
   .. note::
      By default this uses the :doc:`index </modeling/geometry_nodes/input/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the face corner domain.

Offset
   The number of corners to move around the face before finding the result, 
   circling around the start of the face if necessary


Properties
==========

This node has no properties.


Outputs
=======

Corner Index
   The index of the offset face corner.

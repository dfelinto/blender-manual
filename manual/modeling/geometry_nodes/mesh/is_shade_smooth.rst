.. index:: Geometry Nodes; Is Shade Smooth
.. _bpy.types.GeometryNodeInputShadeSmooth:

********************
Is Shade Smooth Node
********************

.. figure:: /images/node-types_GeometryNodeInputShadeSmooth.webp
   :align: right
   :alt: Is Shade Smooth Node.

The *Is Shade Smooth* node outputs true for each face of the mesh if that face
is marked to render smooth shaded. Otherwise, if the face is marked to render as flat
shaded, so the node outputs false.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Smooth
   Boolean value that indicates whether the normals of each face corner on the final mesh
   are smoothed with normal of all adjacent faces or not.

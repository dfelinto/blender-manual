.. index:: Geometry Nodes; Set Shade Smooth
.. _bpy.types.GeometryNodeSetShadeSmooth:

*********************
Set Shade Smooth Node
*********************

.. figure:: /images/node-types_GeometryNodeSetShadeSmooth.webp
   :align: right
   :alt: Set Shade Smooth node.

   Set Shade Smooth node.

The *Set Shade Smooth* node controls whether the mesh's faces look smooth in the viewport and renders.
The input node for this data is the :doc:`Is Shade Smooth </modeling/geometry_nodes/mesh/is_shade_smooth>` node.


Inputs
======

Mesh
   Standard geometry input.

Shade Smooth
   When true, the selected faces will be marked to render smooth shaded.
   Otherwise the faces will be rendered flat shaded.

Selection
   Boolean input for selecting which faces will have the Shade Smooth value applied.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Standard geometry output.

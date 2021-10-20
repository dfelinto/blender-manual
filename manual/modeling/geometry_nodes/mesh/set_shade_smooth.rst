.. index:: Geometry Nodes; Set Shade Smooth
.. _bpy.types.GeometryNodeSetShadeSmooth:

*********************
Set Shade Smooth Node
*********************

.. figure:: /images/modeling_geometry-nodes_mesh_set-shade-smooth_node.png
   :align: right

   The Set Shade Smooth node.

The *Set Shade Smooth* node controls whether the mesh's faces look smooth in the viewport and renders.
The input node for this data is the :doc:`Is Shade Smooth </modeling/geometry_nodes/mesh/is_shade_smooth>` node.


Inputs
======

Geometry
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

Geometry
   Standard geometry output.

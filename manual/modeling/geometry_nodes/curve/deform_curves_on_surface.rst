.. index:: Geometry Nodes; Deform Curves on Surface
.. _bpy.types.GeometryNodeDeformCurvesOnSurface:

*****************************
Deform Curves on Surface Node
*****************************

.. figure:: /images/node-types_GeometryDeformCurvesOnSurface.png
   :align: center
   :alt: Deform Curves on Surface node.


The *Deform Curves on Surface* node translates and rotates each curve based on the
difference in its root position. The root position is defined by UV coordinates stored
on each curve and the :term:`UV Map` selected for the purpose in the 
:ref:`Curves surface settings <bpy.types.Curves.surface>`.

The transformation is calculated based on the difference of the original mesh 
(before shape keys and modifiers are evaluated), and the final mesh.

Unlike other geometry nodes, this node has quite a few implicit inputs:

- The original and evaluated mesh are retrieved from the modifier object's :ref:`surface <bpy.types.Curves.surface>` 
  property. This means the node only works for curves objects.
- The original and evaluated UV map are also retrieved from the object's surface property.
- A 3D vector attribute named ``rest_position``, used for calculating tangents for rotating
  curves that are consistent with the tangents calculated on the original mesh (the rotation
  needs to be calculated from the normal and tangent of the original and evaluated meshes). 
- A 2D vector attribute on the curve domain named ``surface_uv_coordinate`` to store the
  location of the root positions on the surface mesh's UV map.

In future development, this node will be generalized so the setup is more flexible.


Inputs
======

Curves
   Standard curves input.


Properties
==========

This node has no properties.


Outputs
=======

Curves
   Standard curves output.

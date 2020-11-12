.. _bpy.types.ShaderNodeDisplacement:

*****************
Displacement Node
*****************

.. figure:: /images/render_shader-nodes_vector_displacement_node.png
   :align: right

   Displacement Node.

The *Displacement* node is used to displace the surface along the surface normal,
to add more detail to the geometry. Both procedural textures and baked displacement maps
can be used.

For best results the mesh must be subdivided finely to bring out the detail
in the displacement texture.

It is also possible to use the displacement as bump mapping only by changing the material
settings, so that no high resolution mesh is needed.

.. seealso::

   :doc:`Material Displacement </render/materials/components/displacement>`
   for more details on displacement workflows.


Inputs
======

Height
   Distance to displace the surface along the normal.
   This is where a texture node can be connected.
Midlevel
   Neutral displacement value that causes no displacement.
   With the default 0.5, any lower values will cause the surfaces to be pushed inwards,
   and any higher values will push them outwards.
Scale
   Increase or decrease the amount of displacement.
Normal
   Standard normal input.


Properties
==========

Space
   Object Space means the displacement scales along with the object.
   When using World Space the object scale is ignored.


Outputs
=======

Displacement
   Displacement offset to be connected into the Material Output.


Examples
========

.. figure:: /images/render_materials_components_displacement_example.jpg

   Bump only, displacement only, and displacement and bump combined.

.. _bpy.types.ShaderNodeBump:

*********
Bump Node
*********

.. figure:: /images/render_shader-nodes_vector_bump_node.png
   :align: right

   Bump Node.

The *Bump* node generates a perturbed normal from a height texture, for bump mapping.
The height value will be sampled at the shading point and two nearby points
on the surface to determine the local direction of the normal.


Inputs
======

Strength
   Strength of the bump mapping effect, interpolating between no bump mapping and full bump mapping.
Distance
   Multiplier for the height value to control the overall distance for bump mapping.
Height
   Scalar value giving the height offset from the surface at the shading point; this is where you plug in textures.
Normal
   Standard normal input.


Properties
==========

Invert
   Invert the bump mapping, to displace into the surface instead of out.


Outputs
=======

Normal
   Standard normal output.


Examples
========

.. figure:: /images/render_shader-nodes_vector_bump_node-setup.png

The above node setup will only bump the diffuse part of the shader,
simulating a bumpy diffuse surface coated with a smooth glossy "glaze" layer.

.. figure:: /images/render_shader-nodes_vector_bump_example.jpg

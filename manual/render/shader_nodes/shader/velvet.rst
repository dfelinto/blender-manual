.. _bpy.types.ShaderNodeBsdfVelvet:

***********
Velvet BSDF
***********

.. figure:: /images/render_shader-nodes_shader_velvet_node.png
   :align: right

   Velvet BSDF.

:guilabel:`Cycles Only`

The *Velvet* :abbr:`BSDF (Bidirectional scattering distribution function)`
is used to add reflection to materials such as cloth.
It is meant to be used together with other shaders (such as a *Diffuse Shader*)
and is not particularly useful on its own.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Sigma
   Variance of the normal distribution,
   controlling the sharpness of the peak. It can be thought of as a kind of *roughness*.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.


Properties
==========

This node has no properties.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::
   :widths: auto

   * - .. figure:: /images/render_shader-nodes_shader_velvet_example.jpg

          The Velvet shader example.

     - .. figure:: /images/render_shader-nodes_shader_velvet_behavior.svg
          :width: 308px

          The Velvet shader behavior.

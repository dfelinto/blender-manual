.. _bpy.types.ShaderNodeBsdfToon:

*********
Toon BSDF
*********

.. figure:: /images/render_shader-nodes_shader_toon_node.png
   :align: right

   Toon BSDF.

:guilabel:`Cycles Only`

The *Toon* :abbr:`BSDF (Bidirectional scattering distribution function)`
is used to create *Diffuse* and *Glossy* materials with cartoon light effects.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Size
   Parameter between 0.0 and 1.0 that gives an angle of reflection between 0° and 90°.
Smooth
   This value specifies an angle over which a smooth transition from full to no reflection happens.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.


Properties
==========

Component
   Diffuse
      Use shading based on the Diffuse BSDF.
   Glossy
      Use shading based on the Glossy BSDF for specular reflection.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. figure:: /images/render_shader-nodes_shader_toon_example.jpg

   Example of Toon Shader.

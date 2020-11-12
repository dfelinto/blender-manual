.. _bpy.types.ShaderNodeBsdfGlossy:

***********
Glossy BSDF
***********

.. figure:: /images/render_shader-nodes_shader_glossy_node.png
   :align: right

   Glossy BSDF.

The *Glossy* :abbr:`BSDF (Bidirectional scattering distribution function)`
node is used to add reflection with microfacet distribution, used for materials such as metal or mirrors.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Roughness
   Input for the surface roughness resulting in sharp to blurry reflections.
Normal
   Normal used for shading.


Properties
==========

Distribution
   Microfacet distribution to use.

   Sharp
      Results in perfectly sharp reflections like a mirror. The *Roughness* value is not used.
   GGX
      GGX microfacet distribution.
   Multiple-scattering GGX :guilabel:`Cycles Only`
      Takes multiple bounce (scattering) events between microfacets into account.
      This gives a more energy conserving results, which would otherwise be visible as excessive darkening.
   Beckmann :guilabel:`Cycles Only`
      Beckmann microfacet distribution.
   Ashikhmin-Shirley :guilabel:`Cycles Only`
      Ashikhmin-Shirley microfacet distribution.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::
   :widths: auto

   * - .. figure:: /images/render_shader-nodes_shader_glossy_example.jpg

          Sharp Glossy example.

     - .. figure:: /images/render_shader-nodes_shader_glossy_behavior-sharp.svg
          :width: 308px

          Sharp Glossy behavior.

   * - .. figure:: /images/render_shader-nodes_shader_glossy_rough.jpg

          Rough Glossy example.

     - .. figure:: /images/render_shader-nodes_shader_glossy_behavior.svg
          :width: 308px

          Rough Glossy behavior.

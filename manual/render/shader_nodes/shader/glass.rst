.. _bpy.types.ShaderNodeBsdfGlass:

**********
Glass BSDF
**********

.. figure:: /images/render_shader-nodes_shader_glass_node.png
   :align: right

   Glass BSDF.

The *Glass* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to add a Glass-like shader mixing refraction and reflection at grazing angles.
Like the transparent shader, only pure white will make it transparent.
The glass shader tends to cause noise due to caustics.
Since the Cycles path tracing integrator is not very good at rendering caustics,
it helps to combine this with a transparent shader for shadows;
for :ref:`more details see here <render-cycles-reducing-noise-glass-and-transp-shadows>`.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is transmitted for each wavelength.
Roughness
   Influences sharpness of the refraction; perfectly sharp at 0.0 and smoother with higher values.
IOR
   Index of refraction (:term:`IOR`) defining how much the ray changes direction. At 1.
   0 rays pass straight through like transparent; higher values give more refraction.
Normal
   Normal used for shading.


Properties
==========

Distribution
   Microfacet distribution to use.

   :Sharp:
      Results in perfectly sharp reflections like a mirror. The *Roughness* value is not used.
   :GGX: GGX microfacet distribution.
   :Multiple-scattering GGX: :guilabel:`Cycles Only`
      Takes multiple bounce (scattering) events between microfacets into account.
      This gives a more energy conserving results, which would otherwise be visible as excessive darkening.
   :Beckmann: :guilabel:`Cycles Only`
      Beckmann microfacet distribution.
   :Ashikhmin-Shirley: :guilabel:`Cycles Only`
      Ashikhmin-Shirley microfacet distribution.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::
   :widths: auto

   * - .. figure:: /images/render_shader-nodes_shader_glass_example.jpg

          Sharp Glass example.

     - .. figure:: /images/render_shader-nodes_shader_glass_behavior-sharp.svg
          :width: 308px

          Sharp Glass behavior.

   * - .. figure:: /images/render_shader-nodes_shader_glass_example-rough.jpg

          Rough Glass example.

     - .. figure:: /images/render_shader-nodes_shader_glass_behavior.svg
          :width: 308px

          Rough Glass behavior.

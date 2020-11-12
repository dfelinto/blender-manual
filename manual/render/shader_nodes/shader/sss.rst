.. _bpy.types.ShaderNodeSubsurfaceScattering:

*********************
Subsurface Scattering
*********************

.. figure:: /images/render_shader-nodes_shader_sss_node.png
   :align: right

   Subsurface Scattering Shader.

The *Subsurface Scattering* node is used to add simple subsurface multiple scattering,
for materials such as skin, wax, marble, milk and others. For these materials,
rather than light being reflect directly off the surface, it will penetrate the surface and
bounce around internally before getting absorbed or leaving the surface at a nearby point.

How far the color scatters on average can be configured per RGB color channel. For example,
for skin, red colors scatter further, which gives distinctive red-colored shadows,
and a soft appearance.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Scale
   Global scale factor for the scattering radius.
Radius
   Average distance that light scatters below the surface.
   Higher radius gives a softer appearance, as light bleeds into shadows and through the object.
   The scattering distance is specified separately for the RGB channels,
   to render materials such as skin where red light scatters deeper.
   The X, Y and Z values are mapped to the R, G and B values, respectively.
Sharpness
   Used only with *Cubic* falloff.
   Values increasing from 0 to 1 prevents softening of sharp edges and reduces unwanted darkening.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.
Texture Blur
   How much of the texture will be blurred along with the lighting,
   mixing the texture at the incoming and outgoing points on the surface.
   Note that the right choice depends on the texture.
   Consider for example a texture created from a photograph of skin,
   in this case the colors will already be pre-blurred and texture blur could be set to 0.
   Even for hand-painted textures, no blurring or minimal blurring might be appropriate,
   as a texture artist would likely paint in softening already.
   One would usually not even know what an unblurred skin texture looks like; we always see it blurred.
   For a procedural texture on the other hand this option would likely have a higher value.


Properties
==========

Method
   Rendering method to simulate subsurface scattering.

   Christensen-Burley
      Is an approximation to physically-based volume scattering.
      Gives less blurry results than Cubic and Gaussian functions.
   Random Walk :guilabel:`Cycles Only`
      Provides the most accurate results for thin and curved objects.
      This comes at the cost of increased render time or noise for more dense media like skin,
      but also better geometry detail preservation.
      Random Walk uses true volumetric scattering inside the mesh,
      which means that it works best for closed meshes.
      Overlapping faces and holes in the mesh can cause problems.
   Cubic
      Is a sharp falloff useful for many simple materials. The function is :math:`(radius - x)^3`.
   Gaussian
      Gives a smoother falloff following a normal distribution,
      which is particularly useful for more advanced materials that use measured
      data that was fitted to one or more such Gaussian functions.
      The function is :math:`e^{-8x^2/ radius^2}`,
      such that the radius roughly matches the maximum falloff distance.
      To match a given measured variance *v*, set :math:`radius = sqrt(16 × v)`.


Outputs
=======

BSSRDF
   :abbr:`BSSRDF (Bidirectional subsurface scattering distribution function)` shader output.


Examples
========

.. figure:: /images/render_shader-nodes_shader_sss_example.jpg

   Random Walk subsurface scattering.

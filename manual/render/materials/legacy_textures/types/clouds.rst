.. _bpy.types.CloudsTexture:

******
Clouds
******

Clouds represent Perlin noise. In addition, each noise-based Blender texture
(with the exception of Voronoi and simple noise) has a *Noise Basis* setting that allows
the user to select which algorithm is used to generate the texture. This is often used for
Clouds, Fire, Smoke. Well-suited to be used as a Bump map, giving an overall irregularity to the material.

.. figure:: /images/render_materials_legacy-textures_types_clouds_panel.png

   Clouds Texture panels.


Options
=======

Grayscale
   The standard noise, gives an intensity.
Color
   The noise gives an RGB value.
Noise
   *Soft* or *Hard*, changes contrast and sharpness.
Size
   The dimension of the Noise table.
Depth
   The depth of the *Clouds* calculation.
   A higher number results in a long calculation time, but also in finer details.

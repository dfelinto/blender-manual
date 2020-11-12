.. _bpy.types.SceneEEVEE.volumetric:

***********
Volumetrics
***********

Eevee simulate volumetric scattering by evaluating all volume objects inside the view frustum.

For this it uses several 3D textures which have a high video memory usage.
The texture dimensions can be tweaked using the *Tile Size* and *Samples* parameters.

Object volumes have some :ref:`limitations <eevee-limitations-volumetrics>`.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Render --> Volumetrics`

Start
   Start distance of the volumetric effect.

End
   End distance of the volumetric effect.

Tile Size
   Controls the quality of the volumetric effects. Lower size increases video memory usage and quality.
   This is the size in pixels of a volumetric cell.

Samples
   Number of samples to compute volumetric effects. Higher count increases video memory usage and quality.
   These samples are distributed along the view depth (view Z axis).

Distribution
   Blend between linear and exponential sample distribution. Higher values puts more samples near the camera.


.. _bpy.types.SceneEEVEE.volumetric_light:

Volumetric Lighting
===================

Let the volume scattering scatter light in the scene.
Unnecessary if no Volume Scatter is present in the scene.

Light Clamping
   Clamp light contribution of the volume scattering effect. Reduces flickering and noise.
   Set to 0.0 to disable clamping.


.. _bpy.types.SceneEEVEE.volumetric_shadow:

Volumetric Shadows
==================

Approximate light absorption of the surrounding volume objects. This makes the volumes more opaque to light.
This is a very computationally expensive option and has limitations.

Samples
   Number of samples to compute volumetric shadowing.

.. seealso:: :ref:`Limitations <eevee-limitations-volumetrics>`.

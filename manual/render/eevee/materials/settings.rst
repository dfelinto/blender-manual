
*****************
Material Settings
*****************

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Material --> Settings`


Backface Culling
================

Backface Culling hides the back side of faces in the final render.


.. _bpy.types.Material.blend_method:

Blend Mode
==========

After calculating the color of a surface, the blend mode defines how it is added to the color buffer.
Depending on this, the final color will be different.

.. note::

   Alpha Blending is considered a "Transparent" blend mode
   and has implications regarding screen space effects.

Opaque
   The previous color will be overwritten by the surface color.
   The alpha component is ignored. This is the fastest option.

Alpha Clip
   The previous color will be overwritten by the surface color,
   but only if the alpha value is above the clip threshold.

Alpha Hashed
   The previous color will be overwritten by the surface color,
   but only if the alpha value is above a random clip threshold.
   This statistical approach is noisy but is able to approximate alpha blending without any sorting problem.
   Increasing the sample count in the render settings will reduce the resulting noise.

Alpha Blending
   Use alpha blending to overlay the surface color on top of the previous color.


Sorting Problem
---------------

When writing to the color buffer using transparent blend modes,
the order in which the color blending happens is important as it can change the final output color.
As of now Eevee does not support per-fragment (pixel) sorting or per-triangle sorting.
Only per-object sorting is available and is automatically done on all transparent surfaces based on object origin.

.. note::

   This per-object sorting has already a cost and having thousands of
   these objects in a scene will greatly degrade performance.

Show Backside
   If enabled, all transparent fragments will be rendered.
   If disabled, only the front-most surface fragments will be rendered.
   Disable this option to ensure correct appearance of transparency from any point of view.
   Then using *Alpha Blending* this option should be disabled because with *Alpha Blending*,
   the order in which triangles are sorted is important.


Shadow Mode
===========

Type of shadows used for a transparent surface.
Eevee does not support colored shadow maps.

Half transparent shadows can be produced by using hashed transparent shadows and
a larger Soft value on the shadow map.

.. note::

   This option does not change the behavior of contact shadows which are traced using the depth buffer.
   If the material is writing to the depth buffer
   (in other words, if the blend mode is set to either *Opaque*, *Alpha Clip* or *Alpha Hashed*),
   contact shadows will be casted by the surface material regardless of the *Transparent Shadow* type.

None
   The surface will not cast any shadow.

Opaque
   The surface will cast shadows like an opaque surface.

Clip
   The surface will cast shadows like an opaque surface,
   but only areas where the alpha value is above the clip threshold.

Hashed
   The surface will cast shadows like an opaque surface,
   but only areas where the alpha value is above a random threshold.


Screen Space Refraction
=======================

Enabling Screen Space Refraction on a surface means that refraction BSDFs
will do a raytrace against the depth buffer to find the most accurate refracted color.
This has a big performance cost if the surface covers a lot of pixels.

Screen Space Reflections and Ambient Occlusion are not compatible with Screen Space Refraction.
They will be disabled on the surfaces that use it.
Surfaces that use Screen Space Refraction will not appear in Screen Space Reflections at the right place.
Surfaces that use Screen Space Refraction will not cast Ambient Occlusion onto other surfaces.

If this option is disabled or if the Screen Space Refraction raytrace fails,
the refracted ray will use the color of the nearest probe.

Screen Space Refraction
   Enables screen space refraction.

Refraction Depth
   If Refraction Depth is not 0.0, all refraction BSDFs in the shader will act as if
   the object is a thin slab of the refraction material having this thickness.
   This will model a second refraction event that will double the absorption color and
   start the refraction ray after this second event.

   This option greatly increases the quality of thin glass objects.


.. _bpy.types.Material.use_sss_translucency:

Subsurface Translucency
=======================

Eevee's Subsurface Scattering algorithm works by blurring the irradiance in screen space.
This means that if no visible part of the surface is lit, the effect disappears.

However, true Subsurface Scattering goes beneath the surface and can travel a large distance.
This is why a human ear lit from behind appears red on the front side.

That is what this effect mimics. This translucency approximation only works
with lights that have shadow maps and only on Subsurface BSDFs (not the Translucency BSDFs).
It does not work with indirect lighting. The soft parameter of the shadow maps also affects this effect.


Pass Index
==========

Index number for the *Material Index* :doc:`render pass </render/layers/passes>`.
This can be used to give a mask to a material which then can be read with
the :doc:`ID Mask Node </compositing/types/converter/id_mask>` in the Compositor.

.. _bpy.types.SceneEEVEE.shadow:

*******
Shadows
*******

Eevee uses Shadow Mapping techniques to properly shadow the light coming directly from light objects.

A shadow map is a texture that stores the nearest occluder from the light position.
Eevee also filters the shadow maps in order to smooth out the pixelated appearance.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Shadows`

Cube Size
   Size of the shadow cubemaps used to shadow Point, Area and Spot lights.
   Higher shadow map size will give higher precision and sharper shadows.

Cascade Size
   Size of one cascade used by *Cascaded Shadow Maps*. This is only for Sun lights.

High Bitdepth
   This option can help reduce some artifacts due to float imprecision inside the shadow maps.
   This option effectively double the memory usage of shadow maps and will slow down their update.

Soft Shadows
   Randomize the shadow maps origin to create soft shadows. It needs a lot of samples to get rid of the banding.

Light Threshold
   The minimum amount of light for a light to contribute for lighting.
   This light threshold does not take the light shape into account and may not suit every case.
   That is why Blender provides a :ref:`per-light override <bpy.types.Light.cutoff_distance>`
   where you can just set the cut off distance.

   The influence distance is also used as shadow far clip distance, which might affect how shadows looks.
   This influence distance does not affect sun lights that still have a far clip distance.

   .. seealso::

      :doc:`Custom Limit </render/eevee/lighting>`.

.. note::

   The Soft Shadows method is not physically based and will not match Cycles for very large lights.

.. tip::

   A 512 px cubemap has 6 × 512 × 512 pixels in it.
   Tweaking the *Size* parameters can have a big impact on memory consumption and performance.

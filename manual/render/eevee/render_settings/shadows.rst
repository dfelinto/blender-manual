.. _bpy.types.SceneEEVEE.shadow:

*******
Shadows
*******

These settings influence shadows which appear on objects because there is another object (the occluder) between them and a Light.
Eevee uses a technique called Shadow Mapping to calculate these shadows.
A shadow map is calculated by looking around from the position of each Light and finding the objects which are closest to the Light.
These objects are called the nearest occluders.
Everything which is behind (or, you can say, covered by) the nearest occluders will be in shadow.

The shadow map is a cube (hence the term "cubemap") and the Light is in the middle of this cube. The cube has six sides and each side is divided into a grid. You can set the resolution of the grid (for example, 512 × 512 pixels) with the *Cube Size* setting below. During shadow calculation, the nearest occluders are only searched at grid points but not between grid points. Because of this, the edge of the calculated shadow will appear pixelated at low Cube Size settings.

.. note::

   Settings for the shadows and illumination caused by light bouncing between objects (indirect lighting) can be found on the Indirect Lighting tab.


.. reference::

   :Panel:     :menuselection:`Render --> Shadows`

Cube Size
   Number of pixels on one side of the shadow cubemap (see above) used to calculate the shadow of Point, Area and Spot lights.
   If you want to make the edge of shadows less pixelated, then increase this value.
   But be aware that this increases memory usage and decreases performance since a 512 px cubemap has 6 × 512 × 512 pixels in it.

Cascade Size
   Size of one cascade used by *Cascaded Shadow Maps*. This is only for Sun lights.

High Bitdepth
   This option can help reduce some artifacts due to float imprecision inside the shadow maps.
   This option effectively doubles the memory usage of shadow maps and will slow down their update.

Soft Shadows
   Randomize the shadow map's origin to create soft shadows. It needs a lot of samples to get rid of the banding.

Light Threshold
   The minimum amount of light for a light to contribute for lighting.
   This light threshold does not take the light shape into account and may not suit every case.
   That is why Blender provides a :ref:`per-light override <bpy.types.Light.cutoff_distance>`
   where you can just set the cut off distance.

   The influence distance is also used as shadow far clip distance, which might affect how shadows look.
   This influence distance does not affect sun lights that still have a far clip distance.

   .. seealso::

      :ref:`Custom Distance <bpy.types.Light.cutoff_distance>`.

.. note::

   The Soft Shadows method is not physically based and will not match Cycles for very large lights.


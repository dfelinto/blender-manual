.. _bpy.types.SceneEEVEE.sss:

*********************
Subsurface Scattering
*********************

This effect mimics real subsurface scattering by blurring the diffuse lighting in screen space.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Subsurface Scattering`

Samples
   Number of samples to compute the scattering effect.

Jitter Threshold
   For the effect to be efficient, samples need to be coherent and not random.
   This can lead to a cross shaped pattern when the scattering radius is high.
   Increasing the Jitter Threshold will rotate the samples below this radius percentage
   in a random pattern in order to hide the visible pattern.
   This affects the performance if the scattering radius is large.

.. note::

   :ref:`Subsurface Translucency <bpy.types.Material.use_sss_translucency>`
   needs to be enabled in order to make the light go through an object
   (like simulating a human ear lit from behind).

   This option only works with shadowed lights and does not work with indirect lighting.

.. seealso:: :ref:`Limitations <eevee-limitations-sss>`.

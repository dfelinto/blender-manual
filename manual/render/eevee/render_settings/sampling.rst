.. _bpy.types.SceneEEVEE.taa_samples:
.. _bpy.types.SceneEEVEE.taa_render_samples:

********
Sampling
********

Eevee uses a process called Temporal Anti-Aliasing (TAA) which reduces :term:`Aliasing`.
TAA is sample based so the more samples the more aliasing is reduced at the cost of performance.

.. reference::

   :Panel:     :menuselection:`Render --> Sampling`

Viewport
   The number of samples to use in the 3D Viewport.
   When setting this to zero the viewport will be resampled continuously.
Render
   The number of samples to use in the final render.

.. _bpy.types.SceneEEVEE.use_taa_reprojection:

Viewport Denoising
   Reduces noise while moving the viewport or during animation playback.


********
Sampling
********

.. reference::

   :Panel:     :menuselection:`Render --> Sampling`

The integrator is the rendering algorithm used to compute the lighting.
Cycles currently supports a path tracing integrator with direct light sampling.
It works well for various lighting setups,
but is not as suitable for caustics and some other complex lighting situations.

Rays are traced from the camera into the scene,
bouncing around until they find a light source such as a light, an object emitting light,
or the world background. To find lights and surfaces emitting light,
both indirect light sampling (letting the ray follow the surface BSDF)
and direct light sampling (picking a light source and tracing a ray towards it) are used.

.. _bpy.types.CyclesRenderSettings.preview_samples:

Viewport Samples
   Number of samples for viewport rendering. Setting this value to zero
   enables indefinite sampling of the viewport.

.. _bpy.types.CyclesRenderSettings.samples:

Render Samples
   Number of paths to trace for each pixel in the final render. As more samples are taken,
   the solution becomes less noisy and more accurate.

.. _bpy.types.CyclesRenderSettings.time_limit:

Time Limit
   Renders scene until time limit or sample count is reached. When the time is set to 0,
   the sample count is used to determine when the render stops.

   .. note:: The time limit does not include pre-render processing time, only render time.


.. _bpy.types.CyclesRenderSettings.use_adaptive_sampling:

Adaptive Sampling
=================

With adaptive sampling Cycles automatically reduces the number of samples in areas that have little noise,
for faster rendering and more even noise distribution.
For example hair on a character may need many samples, but the background may need very few.

With adaptive sampling it is also possible to render images with a target amount of noise.
This is done by settings the *Noise Threshold*, typical values are in the range from 0.1 to 0.001.
Then render samples can then be set to a high value,
and the renderer will automatically choose the appropriate amount of samples.

.. _bpy.types.CyclesRenderSettings.adaptive_threshold:
.. _bpy.types.CyclesRenderSettings.preview_adaptive_threshold:

Noise Threshold
   The error threshold to decide whether to continue sampling a pixel or not.
   Typical values are in the range from 0.1 to 0.001, with lower values meaning less noise.
   Setting it to exactly 0 lets Cycles guess an automatic value for it based on the total sample count.

.. _bpy.types.CyclesRenderSettings.adaptive_min_samples:
.. _bpy.types.CyclesRenderSettings.preview_adaptive_min_samples:

Min Samples
   The minimum number of samples a pixel receives before adaptive sampling is applied.
   When set to 0 (default), it is automatically set to a value determined by the *Noise Threshold*.


.. _render-cycles-settings-viewport-denoising:

Denoising
=========

Denoising removes noise while previewing scenes in *Rendered* mode in the 3D Viewport or for final renders.

.. _bpy.types.CyclesRenderSettings.use_denoising:
.. _bpy.types.CyclesRenderSettings.denoiser:

Render
   Denoising for the final render can be enabled or disabled with the checkbox.
   For denoising the image after rendering with the :doc:`Denoising node </compositing/types/filter/denoise>`,
   the :ref:`Data Render Passes <render_layers_passes_data>` also adapt to the selected denoiser.

   :Open Image Denoise:
      Uses Intel's `Open Image Denoise <https://www.openimagedenoise.org/>`__,
      an AI denoiser which runs on the CPU.
   :OptiX:
      Uses an artificial intelligence algorithm to remove noise from renders.
      It is based on the :ref:`render-cycles-gpu-optix` acceleration engine
      and therefore has the same GPU requirements as rendering with Optix.

.. _bpy.types.CyclesRenderSettings.use_preview_denoising:
.. _bpy.types.CyclesRenderSettings.preview_denoiser:

Viewport
   Denoising for the *Rendered* mode in the 3D Viewport can be enabled or disabled for with the checkbox.

   :Automatic:
      Uses the faster available denoiser for 3D Viewport rendering
      (*OptiX* if available, otherwise *OpenImageDenoise*).
   :OpenImageDenoise:
      Uses Intel's `Open Image Denoise <https://www.openimagedenoise.org/>`__,
      an AI denoiser which runs on the CPU.
   :OptiX:
      Uses an artificial intelligence algorithm to remove noise from renders.
      It is based on the :ref:`render-cycles-gpu-optix` acceleration engine
      and therefore has the same GPU requirements as rendering with Optix.

.. _bpy.types.CyclesRenderSettings.preview_denoising_start_sample:

Start Sample
   Sample to start :ref:`denoising <render-cycles-settings-viewport-denoising>` in the 3D Viewport.

.. _bpy.types.CyclesRenderSettings.preview_denoising_input_passes:
.. _bpy.types.CyclesRenderSettings.denoising_input_passes:

Input Passes
   Controls which :doc:`Render Pass </render/layers/passes>` the denoiser should use as input,
   which can have different effects on the denoised image.
   Generally, the more passes the denoiser has to denoise the better the result.
   It is recommended to at least use *Albedo* as *None* can blur out details,
   especially at lower sample counts.

   :None: Denoises the image using color data.
   :Albedo: Denoises the image using color and albedo data.
   :Albedo + Normal: Denoises the image using color, albedo, and normal pass data.

.. _bpy.types.CyclesRenderSettings.preview_denoising_prefilter:
.. _bpy.types.CyclesRenderSettings.denoising_prefilter:

Prefilter
   Controls whether or not prefiltering is applied to *Input Passes* for use when denoising.
   Visible only when using *OpenImageDenoise*.

   :None:
      Does not apply any prefiltering to the input passes. This option retains the most detail and
      is the fastest, but assumes the input passes are noise free which may require a high sample count.
      If the input passes aren't noise free, then noise will remain in the image after denoising.
   :Fast:
      Assumes the input passes are not noise free, yet does not apply prefiltering to the input passes.
      This option is faster than *Accurate* but produces a blurrier result.
   :Accurate:
      Prefilters the input passes before denoising to reduce noise. This option usually produces
      more detailed results than *Fast* with increased processing time.


.. _bpy.types.CyclesRenderSettings.use_guiding:

Path Guiding
============

Path guiding helps reduce noise in scenes where finding a path to light is difficult for
regular path tracing, for example when a room is lit through a small door opening.
Important light directions are learned over time, improving as more samples are taken.
Guiding is supported for surfaces with diffuse BSDFs and volumes with isotropic
and anisotropic scattering.

.. note::

   - Path guiding is only available when rendering on a CPU.

   - While path guiding helps render caustics in some scenes, it is not designed for complex caustics
     as they are harder to learn and guide.

.. _bpy.types.CyclesRenderSettings.guiding_training_samples:

Training Samples
   The maximum number of samples to use for training. A value of 0 will keep training until
   the end of the render. Usually 128 to 256 training samples is enough for accurate guiding.
   Higher values can lead to a minor increases in guiding quality but with increased render times.

.. _bpy.types.CyclesRenderSettings.use_surface_guiding:

Surface
   Enable path guiding for the diffuse component of surfaces.

.. _bpy.types.CyclesRenderSettings.use_volume_guiding:

Volume
   Enable path guiding inside volumes.


Lights
======

.. _bpy.types.CyclesRenderSettings.light_sampling_threshold:

Light Threshold
   Probabilistically terminates light samples when the light contribution
   is below this threshold (more noise but faster rendering).
   Zero disables the test and never ignores lights.
   This is useful because in large scenes with many light sources,
   some lights might only contribute a small amount to the final image,
   and increase render times. Using this setting can decrease the render times
   needed to calculate the rays which in the end have very little effect on the image.


Advanced
========

.. _bpy.types.CyclesRenderSettings.seed:

Seed
   Seed value for integrator to get different noise patterns.

   .. _bpy.types.CyclesRenderSettings.use_animated_seed:

   Use Animated Seed (clock icon)
      Changes the seed for each frame. It is a good idea to enable this
      when rendering animations because a varying noise pattern is less noticeable.

.. _bpy.types.CyclesRenderSettings.sampling_pattern:

Pattern
   Random sampling pattern used by the integrator.

   :Progressive Multi-Jitter:
      Based on `Progressive Multi-Jittered Sample Sequences <https://graphics.pixar.com/library/ProgressiveMultiJitteredSampling/paper.pdf>`__.
      This is the default pattern and the only one that supports Scrambling Distance.

   :Sobol-Burley:
      Based on `Practical Hash-based Owen Scrambling <https://jcgt.org/published/0009/04/01/paper.pdf>`__.
      An alternative pattern with the same quality as Progressive Multi-Jitter.

.. _bpy.types.CyclesRenderSettings.sample_offset:

Sample Offset
   The number of samples to skip when starting render.
   This can be used to distribute a render across multiple computers
   then combine the images with `bpy.ops.cycles.merge_images`

Scrambling Distance
   Note, these options are not applicable when using the Sobol-Burley sample pattern.

   .. _bpy.types.CyclesRenderSettings.adaptive_scrambling_distance:

   Automatic
      Uses a formula to adapt the scrambling distance strength based on the sample count.

   .. _bpy.types.CyclesRenderSettings.preview_scrambling_distance:

   Viewport
      Uses the *Scrambling Distance* value for the viewport rendering.
      This will make the rendering faster but may cause flickering.

   .. _bpy.types.CyclesRenderSettings.scrambling_distance:

   Multiplier
      Lower values Reduce randomization between pixels to improve GPU rendering performance,
      at the cost of possible rendering artifacts if set too low.


.. _bpy.types.CyclesRenderSettings.min_light_bounces:

Min Light Bounces
   Minimum number of light bounces for each path,
   after which the integrator uses Russian Roulette to terminate paths that contribute less to the image.
   Setting this higher gives less noise, but may also increase render time considerably. For a low number of bounces,
   it is strongly recommended to set this equal to the maximum number of bounces.

.. _bpy.types.CyclesRenderSettings.min_transparent_bounces:

Min Transparent Bounces
   Minimum number of transparent bounces. Setting this higher reduces noise in the first bounces,
   but can also be less efficient for more complex geometry like hair and volumes.

.. _bpy.types.CyclesRenderSettings.use_layer_samples:

Layer Samples
   When render layers have per layer number of samples set, this option specifies how to use them.

   :Use: The render layer samples will override the set scene samples.
   :Bounded: Bound render layer samples by scene samples.
   :Ignore: Ignore render layer sample settings.

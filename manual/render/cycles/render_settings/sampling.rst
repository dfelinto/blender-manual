
********
Sampling
********

.. admonition:: Reference
   :class: refbox

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

Integrator
   There are two sample methods that can be used: *Path Tracing* and *Branched Path Tracing*.

   Path Tracing
      The *Path Tracing* integrator is a pure path tracer;
      at each hit it will bounce light in one direction and pick one light to receive lighting from.
      This makes each individual sample faster to compute,
      but will typically require more samples to clean up the noise.
   Branched Path Tracing
      The non-progressive Branched Path Tracing integrator offers finer control over sampling.
      It is similar to *Path Tracing*, but at the first hit it will split the path for
      different surface components and will take all lights into account for shading instead of just one.

      This makes each sample slower, but will reduce noise,
      especially in scenes dominated by direct or one-bounce lighting.
      To get the same number of diffuse samples as in the path tracing integrator,
      note that e.g. 250 path tracing samples = 10 AA Samples × 25 diffuse samples.
      The Sampling panel shows this total number of samples.

Render
   Number of paths to trace for each pixel in the final render. As more samples are taken,
   the solution becomes less noisy and more accurate.

   When using *Branched Path Tracing*, this changes the *AA Samples*
   which are multiplied by the `Subsamples`_ and improve :term:`Anti-Aliasing`.
Viewport
   Number of samples for viewport rendering. Setting this value to zero
   enables indefinite sampling of the viewport.


Subsamples
==========

The subpanel is only shown when using *Branched Path Tracing*.

Diffuse
   Number of diffuse bounce samples to take for each AA sample.
Glossy
   Number of glossy bounce samples to take for each AA sample.
Transmission
   Number of transmission bounce samples to take for each AA sample.
AO
   Number of ambient occlusion samples to take for each AA sample.
Mesh Light
   Number of mesh light samples to take for each AA sample.
Subsurface
   Number of subsurface scattering samples to take for each AA sample.
Volume
   Number of volume scattering samples to take for each AA sample.


Adaptive Sampling
=================

With adaptive sampling Cycles automatically reduces the number of samples in areas that have little noise,
for faster rendering and more even noise distribution.
For example hair on a character may need many samples, but the background may need very few.

By default, the threshold to stop sampling pixels is adapted to the number of AA samples.
This reduces overall render time, and particularly after denoising the result will be almost indistinguishable.

With adaptive sampling it is also possible to render images with a target amount of noise.
This is done by settings the *Noise Threshold*, typical values are in the range from 0.1 to 0.001.
Then render samples can then be set to a high value,
and the renderer will automatically choose the appropriate amount of samples.

Noise Threshold
   The error threshold to decide whether to continue sampling a pixel or not.
   Typical values are in the range from 0.1 to 0.001, with lower values meaning less noise.
   Setting it to exactly 0 lets Cycles guess an automatic value for it based on the total sample count.

Min Samples
   The minimum number of samples a pixel receives before adaptive sampling is applied.
   When set to 0 (default), it is automatically set to the square root of the total (max) sample count.


.. _render-cycles-settings-viewport-denoising:

Denoising
=========

Denoising removes noise while previewing scenes in *Rendered* mode in the 3D Viewport or for final renders.

Render
   Denoising for the final render can be enabled or disabled with the checkbox.
   For denoising the image after rendering with the :doc:`Denoising node </compositing/types/filter/denoise>`,
   the :ref:`Data Render Passes <render_layers_passes_data>` also adapt to the selected denoiser.

   NLM
      Uses `non-local means <https://en.wikipedia.org/wiki/Non-local_means>`__ to
      denoise the image. Addition properties for this denoising method can be set in
      the :ref:`View Layer Properties <render-layers-denoising-optix>`.
   Open Image Denoise
      Uses Intel's `Open Image Denoise <https://www.openimagedenoise.org/>`__,
      an AI denoiser which runs on the CPU.
   OptiX
      Uses an artificial intelligence algorithm to remove noise from renders.
      It is based on the :ref:`render-cycles-gpu-optix` acceleration engine
      and therefore has the same GPU requirements as rendering with Optix.

Viewport
   Denoising for the *Rendered* mode in the 3D Viewport can be enabled or disabled for with the checkbox.

   Automatic
      Uses the faster available denoiser for 3D Viewport rendering
      (*OptiX* if available, otherwise *OpenImageDenoise*).
   OpenImageDenoise
      Uses Intel's `Open Image Denoise <https://www.openimagedenoise.org/>`__,
      an AI denoiser which runs on the CPU.
   OptiX
      Uses an artificial intelligence algorithm to remove noise from renders.
      It is based on the :ref:`render-cycles-gpu-optix` acceleration engine
      and therefore has the same GPU requirements as rendering with Optix.

Start Sample
   Sample to start :ref:`denoising <render-cycles-settings-viewport-denoising>` in the 3D Viewport.


Advanced
========

Seed
   Seed value for integrator to get different noise patterns.

   Animate Seed (clock icon)
      Changes the seed for each frame. It is a good idea to enable this
      when rendering animations because a varying noise pattern is less noticeable.

Pattern
   Random sampling pattern used by the integrator.

   Sobol
      Uses a Sobol pattern to decide the random sampling pattern used by the integrator.
      See `Sobol sequence <https://en.wikipedia.org/wiki/Sobol_sequence>`__ on Wikipedia for more information.
   Correlated Multi-Jitter
      Uses a correlated multi-jitter pattern to decide the random sampling pattern used by the integrator.
      See `this Pixar paper <https://graphics.pixar.com/library/MultiJitteredSampling/paper.pdf>`__
      for more information.
   Progressive Multi-Jitter
      Uses a progressive multi-jitter pattern to decide the random sampling pattern used by the integrator.
      Its advantage is to provide a well distribution of samples over iterating sample counts.
      Because of its good distribution over a range of different sample counts,
      this sample pattern is used for `Adaptive Sampling`_.
      See `this Pixar paper <https://graphics.pixar.com/library/ProgressiveMultiJitteredSampling/paper.pdf>`__
      for more information.

Square Samples
   Square the amount of samples.

Min Light Bounces
   Minimum number of light bounces for each path,
   after which the integrator uses Russian Roulette to terminate paths that contribute less to the image.
   Setting this higher gives less noise, but may also increase render time considerably. For a low number of bounces,
   it is strongly recommended to set this equal to the maximum number of bounces.

Min Transparent Bounces
   Minimum number of transparent bounces. Setting this higher reduces noise in the first bounces,
   but can also be less efficient for more complex geometry like hair and volumes.

Light Threshold
   Probabilistically terminates light samples when the light contribution
   is below this threshold (more noise but faster rendering).
   Zero disables the test and never ignores lights.
   This is useful because in large scenes with many light sources,
   some might only contribute a small amount to the final image, and increase render times.
   Using this setting can decrease the render times needed to calculate
   the rays which in the end have very little affect on the image.

Sample All Direct Lights
   When enabled, Cycles will sample all lights in the scene for direct bounces, instead of randomly picking one.
   Disabling this can improve the performance, but will need a lot of *Samples*, to clear up the render.

   Visible only when using *Branched Path Tracing*.

Sample All Indirect Lights
   Similar to direct light, but for indirect lights. This can reduce noise in scenes with many lights.

   Visible only when using *Branched Path Tracing*.

.. _render-cycles-integrator-layer-samples:

Layer Samples
   When render layers have per layer number of samples set, this option specifies how to use them.

   Use
      The render layer samples will override the set scene samples.
   Bounded
      Bound render layer samples by scene samples.
   Ignore
      Ignore render layer sample settings.

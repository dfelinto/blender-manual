
Integrator
**********

The integrator is the rendering algorithm used to compute the lighting.
Cycles currently supports a path tracing integrator with direct light sampling.
It works well for various lighting setups,
but is not as suitable for caustics and some other complex lighting situations.

Rays are traced from the camera into the scene,
bouncing around until they find a light source such as a lamp, an object emitting light,
or the world background. To find lamps and surfaces emitting light,
both indirect light sampling (letting the ray follow the surface BSDF)
and direct light sampling (picking a light source and tracing a ray towards it) are used.


Scene Settings
==============

Sampling
^^^^^^^^

There are two integrator modes that can be used: path tracing and branched path tracing.
The **path tracing integrator** is a pure path tracer;
at each hit it will bounce light in one direction and pick one light to receive lighting from.
This makes each individual sample faster to compute,
but will typically require more samples to clean up the noise.

Render Samples
   Number of paths to trace for each pixel in the final render. As more samples are taken,
   the solution becomes less noisy and more accurate.
Preview Samples
   Number of samples for viewport rendering.

The **branched path tracing integrator** (formerly called non-progressive integrator)
is similar, but at the first hit it will split the path for different surface components and
will take all lights into account for shading instead of just one.
This makes each sample slower, but will reduce noise,
especially in scenes dominated by direct or one-bounce lighting.
To get the same number of diffuse samples as in the path tracing integrator, note that e.g.
250 path tracing samples = 10 AA samples x 25 diffuse samples.
The Sampling panel shows this total number of samples.

AA Render Samples
   Number of samples to take for each pixel in the final render. More samples will improve antialiasing.
AA Preview Samples
   Number of samples for viewport rendering.

Diffuse Samples
   Number of diffuse bounce samples to take for each AA sample.
Glossy Samples
   Number of glossy bounce samples to take for each AA sample.
Transmission Samples
   Number of transmission bounce samples to take for each AA sample.
AO Samples
   Number of ambient occlusion samples to take for each AA sample.
Mesh Light Samples
   Number of mesh light samples to take for each AA sample.
Subsurface Samples
   Number of subsurface scattering samples to take for each AA sample.

For both integrators the noise pattern can be controlled.

Seed
   Random number generator seed; each different value gives a different noise pattern.


Bounces
^^^^^^^

Max Bounces
   Maximum number of light bounces. For best quality, this should be set to the maximum. However, in practice,
   it may be good to set it to lower values for faster rendering.
   Setting it to maximum 1 bounce results in direct lighting.
Min Bounces
   Minimum number of light bounces for each path,
   after which the integrator uses Russian Roulette to terminate paths that contribute less to the image.
   Setting this higher gives less noise, but may also increase render time considerably. For a low number of bounces,
   it's strongly recommended to set this equal to the maximum number of bounces.

Diffuse Bounces
   Maximum number of diffuse bounces.
Glossy Bounces
   Maximum number of glossy bounces.
Transmission Bounces
   Maximum number of transmission bounces.


Transparency
^^^^^^^^^^^^

Transparency Max
   Maximum number of transparency bounces.
Transparency Min
   Minimum number of transparency bounces, after which Russian Roulette termination is used.
Transparent Shadows
   For direct light sampling,
   use transparency of surfaces in between to produce shadows affected by transparency of those surfaces.


Tricks
^^^^^^

.. _render-cycles-integrator-no_caustics:

No Caustics
   While in principle path tracing supports rendering of caustics with a sufficient number of samples,
   in practice it may be inefficient to the point that there is just too much noise.
   This option makes it possible to disable them entirely.


.. _render-cycles-integrator-filter_glossy:

Filter Glossy
   When using a value higher than 0.0, this will blur glossy reflections after blurry bounces,
   to reduce noise at the cost of accuracy. 1.0 is a good starting value to tweak.

   Some light paths have a low probability of being found while contributing much light to the pixel.
   As a result these light paths will be found in some pixels and not in others, causing fireflies. An example of
   such a difficult path might be a small light that is causing a small specular highlight on a sharp glossy
   material, which we are seeing through a rough glossy material.
   In fact in such a case we practically have a caustic.


   With path tracing it is difficult to find the specular highlight,
   but if we increase the roughness on the material, the highlight gets bigger and softer, and so easier to find.
   Often this blurring will hardly be noticeable, because we are seeing it through a blurry material anyway,
   but there are also cases where this will lead to a loss of detail in lighting.

Clamp Samples
   This option will clamp all samples to a maximum intensity they can contribute to the pixel,
   again to reduce noise at the cost of accuracy. With value 0.0 this option is disabled;
   lower values clamp more light away.


   If the image has fireflies, there will be samples that contribute very high values to pixels,
   and this option provides a way to limit that. However note that as you clamp out such values,
   bright colors in other places where there is no noise will be lost as well.
   So this is a balance between reducing the noise and keeping the image from losing its intended bright colors.


Motion Blur
^^^^^^^^^^^

Camera and object motion blur rendering can be enabled per scene,
and affects all render layers. This will take the camera and object motion into account to
blur objects along 3 points through the previous, current and next frame.
Currently scale motion is not supported,
only object transformations like translation and rotation.
Viewport rendering currently will not show motion blur.

If there are particles or other physics system in a scene,
be sure to bake them before rendering,
otherwise you might not get correct or consistent motion.

Shutter
   Time between frames over which motion blur is computed. Shutter time 1.0 blurs over the length of 1 frame,
   2.0 over the length of two frames, from the previous to the next.


Material Settings
=================

Multiple Importance Sample
   By default objects with emitting materials use both direct and indirect light sampling methods,
   but in some cases it may lead to less noise overall to disable direct light sampling for some materials.
   This can be done by disabling the :guilabel:`Multiple Importance Sample` option.
   This is especially useful on large objects that emit little light compared to other light sources.


   This option will only have an influence if the material contains an emission node;
   it will be automatically disabled otherwise.


World Settings
==============

Multiple Importance Sample
   By default lighting from the world is computed solely with indirect light sampling.
   However for more complex environment maps this can be too noisy,
   as sampling the BSDF may not easily find the highlights in the environment map image. By enabling this option,
   the world background will be sampled as a lamp, with lighter parts automatically given more samples.

Map Resolution
   When Multiple Importance Sample is enabled, this specifies the size of the importance map
   (resolution x resolution).  Before rendering starts,
   an importance map is generated by "baking" a grayscale image from the world shader. This will then be used to
   determine which parts of the background are light and so should receive more samples than darker parts.
   Higher resolutions will result in more accurate sampling but take more setup time and memory.


Lamp Settings
=============

Multiple Importance Sample
   By default lamps use only direct light sampling. For area lights and sharp glossy reflections, however,
   this can be noisy,
   and enabling this option will enable indirect light sampling to be used in addition to reduce noise.

Samples
   For the branch path tracing integrator, this specifies the number of direct light samples per AA sample.
   Point lamps might need only one sample, while area lamps typically need more.


Volume Render Settings
======================

The scene has these settings:

Step Size
   Distance between volume shader samples when rendering the volume.
   Lower values give more accurate and detailed results but also increased render time.
Max Steps
   Maximum number of steps through the volume before giving up,
   to protect from extremely long render times with big objects or small step sizes.

The world and materials have the following setting:

Homogeneous Volume
   Assume volume has the same density everywhere (not using any textures), for faster rendering.
   For example absorption in a glass object would typically not have any textures,
   and by knowing this we can avoid taking small steps to sample the volume shader.
Sampling Method
   Options are "Multiple Importance", "Distance" or "Equiangular".
   If you've got a pretty dense volume that's lit from far away then distance sampling is usually more efficient.
   If you've got a light inside or near the volume then equiangular sampling is better.
   If you have a combination of both, then the multiple importance sampling will be better.

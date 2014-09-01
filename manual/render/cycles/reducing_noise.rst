
Reducing Noise
**************

When performing a final render, it is important to reduce noise as much as possible.
Here we'll discuss a number of tricks that, while breaking the laws of physics,
are particularly important when rendering animations within a reasonable time.
Click to enlarge the example images to see the noise differences well.


Path Tracing
------------

Cycles uses path tracing with next event estimation,
which is not good at rendering all types of light effects, like caustics, but has the
advantage of being able to render more detailed and larger scenes compared to some other
rendering algorithms. This is because we do not need to store, for example,
a photon map in memory,
and because we can keep rays relatively coherent to use an on-demand image cache,
compared to e.g. bidirectional path tracing.


.. figure:: /images/Manual_cycles_light_path_rays.jpg


We do the inverse of what reality does,
tracing light rays from the camera into the scene and onto lights,
rather than from the light sources into the scene and then into the camera.
This has the advantage that we do not waste light rays that will not end up in the camera,
but also means that it is difficult to find some light paths that may contribute a lot.
Light rays will be sent either according to the surface BRDF,
or in the direction of known light sources (lamps, emitting meshes with Sample as Lamp).

For more details, see the
:doc:`Light Paths </render/cycles/light_paths>` and :doc:`Integrator </render/cycles/integrator>` documentation.


Where Noise Comes From
----------------------

To understand where noise can come from, take for example this scene.
When we trace a light ray into the specified location, this is what the diffuse shader "sees".
To find the light that is reflected from this surface,
we need to find the average color from all these pixels.
Note the glossy highlight on the sphere,
and the bright spot the lamp casts on the nearby wall. These hotspots are 100x brighter than
other parts of the image and will contribute significantly to the lighting of this pixel.


+------------------------------------------------------+--------------------------------------------+----------------------------------------------------+
+.. figure:: /images/Cycles_noise_fisheye_reference.jpg|.. figure:: /images/Cycles_noise_fisheye.jpg|.. figure:: /images/Cycles_noise_fisheye_hotspot.jpg+
+   :width: 180px                                      |   :width: 180px                            |   :width: 180px                                    +
+   :figwidth: 180px                                   |   :figwidth: 180px                         |   :figwidth: 180px                                 +
+------------------------------------------------------+--------------------------------------------+----------------------------------------------------+


The lamp is a known light source, so it will not be too hard to find, but the glossy highlight
(s) that it causes are a different matter.
The best we can do with path tracing is to distribute light rays randomly over the hemisphere,
hoping to find all the important bright spots. If for some pixels we miss some bright spot,
but we do find it for another, that results in noise. The more samples we take,
the higher the probability that we cover all the important sources of light.

With some tricks we can reduce this noise. If we blur the bright spots,
they become bigger and less intense, making them easier to find and less noisy.
This will not give the same exact result,
but often it's close enough when viewed through a diffuse or soft glossy reflection.
Below is an example of using Filter Glossy and Smooth Light Falloff.


+-----------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------+
+.. figure:: /images/Cycles_noise_fisheye_blur_reference.jpg|.. figure:: /images/Cycles_noise_fisheye_blur.jpg|.. figure:: /images/Cycles_noise_fisheye_blur_hotspot.jpg+
+   :width: 180px                                           |   :width: 180px                                 |   :width: 180px                                         +
+   :figwidth: 180px                                        |   :figwidth: 180px                              |   :figwidth: 180px                                      +
+-----------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------+


Bounces
-------

In reality light will bounce a huge number of times due to the speed of light being very high.
In practice more bounces will introduce more noise, and it might be good to use something like
the Limited Global Illumination preset that uses **fewer bounces for different shader
types**. Diffuse surfaces typically can get away with fewer bounces,
while glossy surfaces need a few more,
and transmission shaders such as glass usually need the most.


+--------------------------------------------+--------------------------------------------+--------------------------------------------+
+.. figure:: /images/Cycles_noise_0bounce.jpg|.. figure:: /images/Cycles_noise_2bounce.jpg|.. figure:: /images/Cycles_noise_4bounce.jpg+
+   :width: 180px                            |   :width: 180px                            |   :width: 180px                            +
+   :figwidth: 180px                         |   :figwidth: 180px                         |   :figwidth: 180px                         +
+--------------------------------------------+--------------------------------------------+--------------------------------------------+


Also important is to **use shader colors that do not have components of value 1.0** or
values near that; try to keep the maximum value to 0.8 or less and make your lights brighter.
In reality, surfaces are rarely perfectly reflecting all light,
but there are of course exceptions; usually glass will let most light through,
which is why we need more bounces there. High values for the color components tend to
introduce noise because light intensity then does not decrease much as it bounces off each
surface.


Caustics and Filter Glossy
--------------------------

Caustics are a well-known source of noise, causing fireflies.
They happen because the renderer has difficulty finding specular highlights
viewed through a soft glossy or diffuse reflection.
There is a :ref:`No Caustics <render-cycles-integrator-no_caustics>`
option to disable glossy behind a diffuse reflection entirely.
Many render engines will typically disable caustics by default.


+----------------------------------------------+------------------------------------------------+--------------------------------------------------+
+.. figure:: /images/Cycles_noise_reference.jpg|.. figure:: /images/Cycles_noise_no_caustics.jpg|.. figure:: /images/Cycles_noise_filter_glossy.jpg+
+   :width: 180px                              |   :width: 180px                                |   :width: 180px                                  +
+   :figwidth: 180px                           |   :figwidth: 180px                             |   :figwidth: 180px                               +
+----------------------------------------------+------------------------------------------------+--------------------------------------------------+


However using No Caustics will result in missing light,
and it still does not cover the case where a sharp glossy reflection is viewed through a soft glossy reflection.
There is a :ref:`Filter Glossy <render-cycles-integrator-filter_glossy>`
option to reduce the noise from such cases at the cost of accuracy.
This will blur the sharp glossy reflection to make it easier to find, by increasing the shader Roughness.

The above images show default settings, no caustics, and filter glossy set to 1.0.


Light Falloff
-------------

In reality light in a vacuum will always fall off at a rate of 1/(distance^2).
However as distance goes to zero,
this value goes to infinity and we can get very bright spots in the image.
These are mostly a problem for indirect lighting, where the probability of hitting such a
small but extremely bright spot is low and so happens only rarely.
This is a typical recipe for fireflies.


+-------------------------------------------------+-------------------------------------------------+
+.. figure:: /images/Cycles_noise_falloff_hard.jpg|.. figure:: /images/Cycles_noise_falloff_soft.jpg+
+   :width: 180px                                 |   :width: 180px                                 +
+   :figwidth: 180px                              |   :figwidth: 180px                              +
+-------------------------------------------------+-------------------------------------------------+


To reduce this problem, the
FIXME(TODO: Internal Link;
[[../Nodes/More/#Light_Falloff|Light Falloff node]]
) has a **Smooth factor, that can be used to reduce the maximum intensity** a light can contribute to nearby surfaces. The images above show default falloff and smooth value 1.0.


Sample as Lamp
--------------

Materials with emission shaders can be configured to be
FIXME(TODO: Internal Link;
[[../Integrator#Material_Settings|Sampled as a Lamp]]
). This means that they will get rays sent directly towards them, rather than ending up there based on rays randomly bouncing around. For very bright mesh light sources, this can reduce noise significantly. However when the emission is not particularly bright, this will take  samples away from other brighter light sources for which it is important to find them this way.

The optimal setting here is difficult to guess; it may be a matter of trial and error,
but often it is clear that a somewhat glowing object may be only contributing light locally,
while a mesh light used as a lamp would need this option enabled.
Here is an example where the emissive spheres contribute little to the lighting,
and the image renders with slightly less noise by disabling Sample as Lamp on them.


+------------------------------------------------+---------------------------------------------------+
+.. figure:: /images/Cycles_noise_sample_lamp.jpg|.. figure:: /images/Cycles_noise_no_sample_lamp.jpg+
+   :width: 180px                                |   :width: 180px                                   +
+   :figwidth: 180px                             |   :figwidth: 180px                                +
+------------------------------------------------+---------------------------------------------------+


The world background also has a
FIXME(TODO: Internal Link;
[[../Integrator#World_Settings|Sample as Lamp]]
) option.
This is mostly useful for environment maps that have small bright spots in them, rather than being smooth.
This option will then, in a preprocess, determine the bright spots, and send light rays directly towards them. Again,
enabling this option may take samples away from more important light sources if it is not needed.


.. _render-cycles-reducing_noise-glass_and_transp_shadows:

Glass and Transparent Shadows
-----------------------------

With caustics disabled, glass will miss shadows,
and with filter glossy they might be too soft.
We can make a glass shader that will **use a Glass BSDF when viewed directly,
and a Transparent BSDF when viewed indirectly**. The Transparent BSDF can be used for
transparent shadows to find light sources straight through surfaces,
and will give properly-colored shadows, but without the caustics.
The Light Path node is used to determine when to use which of the two shaders.


.. figure:: /images/Cycles_noise_glass_setup.jpg
   :width: 516px
   :figwidth: 516px


+----------------------------------------------------------+------------------------------------------------+
+.. figure:: /images/Cycles_noise_glass_too_much_shadow.jpg|.. figure:: /images/Cycles_noise_glass_trick.jpg+
+   :width: 180px                                          |   :width: 180px                                +
+   :figwidth: 180px                                       |   :figwidth: 180px                             +
+----------------------------------------------------------+------------------------------------------------+


Above we can see the node setup used for the glass transparency trick;
on the left the render has too much shadow due to missing caustics,
and on the right the render with the trick.


Window Lights
-------------

When rendering a daylight indoor scene where most of the light is coming in through a window
or door opening, it is difficult for the integrator to find its way to them.
We can replace the opening with a plane with an emission shader,
so that the integrator knows in which direction to fire rays.
For camera rays we can make this mesh light invisible,
so that we can still look into the outside scene.
This is done either by disabling camera ray visibility on the object,
or by switching between glass and emission shaders in the material.

The two renders below have the same render time,
with the second render using a mesh light positioned in the window.


+----------------------------------------------------+-------------------------------------------------+
+.. figure:: /images/Cycles_noise_window_no_trick.jpg|.. figure:: /images/Cycles_noise_window_trick.jpg+
+   :width: 180px                                    |   :width: 180px                                 +
+   :figwidth: 180px                                 |   :figwidth: 180px                              +
+----------------------------------------------------+-------------------------------------------------+


Clamp Fireflies
---------------

Ideally with all the previous tricks, fireflies would be eliminated, but they could still happen. For that,
**the intensity that any individual light ray sample will contribute to a pixel can be clamped**
to a maximum value with the integrator
FIXME(TODO: Internal Link;
[[../Integrator#Tricks|Clamp setting]]).
If set too low this can cause missing highlights in the image,
which might be useful to preserve for camera effects such as bloom or glare.


+--------------------------------------------+----------------------------------------------+
+.. figure:: /images/Cycles_noise_noclamp.jpg|.. figure:: /images/Cycles_noise_clamp_4.0.jpg+
+   :width: 180px                            |   :width: 180px                              +
+   :figwidth: 180px                         |   :figwidth: 180px                           +
+--------------------------------------------+----------------------------------------------+


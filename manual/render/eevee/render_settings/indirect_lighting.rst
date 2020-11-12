.. _bpy.ops.scene.light_cache:
.. _bpy.types.SceneEEVEE.gi:

*****************
Indirect Lighting
*****************

While not strictly correct, all lighting that is not coming straight out
from a light object is considered as indirect lighting in Eevee.
That means distant :term:`HDRI` lighting (or World) is considered as indirect lighting.
Mesh objects using an Emission node are also considered as indirect lighting.

In Eevee, indirect lighting is separated into two component: Diffuse and Specular.
Both have different needs and representation. For efficiency,
the indirect lighting data is precomputed on demand into a static lighting cache.

As of now the light cache is static and needs to be computed before rendering.
It cannot be updated per frame (unless via scripting).
This limitation is being worked on and will be removed in future versions.

Only view independent lighting can be baked. This is why Reflection Planes are not stored inside the light cache.

The visibility and collections used during the baking process are the ones in the current Active View Layer.

To enable light bounces through large environments, the light baking process can be run multiple times
while injecting the previous bake result into the bake.

Light bounces only concerns diffuse lighting.


.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Indirect Lighting`

Auto Bake
   Enabling this option will trigger baking when a probe is changed; useful when positioning probes objects.

Diffuse Bounces
   Number of bounces to compute when baking the diffuse irradiance.
   Total baking time is more or less multiplied by the number of bounce.

Cubemap Size
   Size of the reflection cubemaps.

Diffuse Occlusion
   Each irradiance sample also stores a shadow map that is used to minimize indirect light leaking.
   This parameter defines the size of this shadow map.

Irradiance Smoothing
   Smooths irradiance interpolation but introduces light bleeding.
   The irradiance visibility term can make the lighting not interpolate smoothly on some surfaces.
   This setting relaxes the weight of that interpolation.

Clamp Glossy
   Clamp pixel intensity to reduce noise inside glossy reflections from reflection cubemaps (0 is disabled).

Filter Quality
   Takes more samples during cubemap filtering to remove artifacts. For now, this only has an effect on cubemaps.


Display
=======

Cubemap Size
   Display the Reflection Cubemaps present in the cache directly in the 3D Viewport.

Irradiance Size
   Display the Irradiance Samples present in the cache in the 3D Viewport.

.. note::

   Cache data display only works in the 3D Viewport and
   only if the viewport uses world lighting in Material Preview or Rendered mode.

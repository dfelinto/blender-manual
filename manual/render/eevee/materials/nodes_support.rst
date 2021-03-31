
***************
Supported Nodes
***************

Most nodes are taken from Cycles. However, some features are missing and
may (or may not) be implemented in Eevee in the future.

.. seealso::

   :doc:`Shader Nodes </render/shader_nodes/index>`.


Eevee only Nodes
================

These nodes are only available if Eevee is the active render engine. These nodes will not work in Cycles.


Shader to RGB
-------------

Eevee supports the conversion of BSDF outputs into color inputs to make any kind of custom shading.
This is supported using the :doc:`Shader to RGB </render/shader_nodes/converter/shader_to_rgb>` node.


Specular BSDF
-------------

This :doc:`node </render/shader_nodes/shader/specular_bsdf>` implements the specular workflow
found in other render engines.


Other Nodes Support
===================

If something is not listed here, it is supported.


Shader Nodes
------------

In the general case, shader nodes should behave more or less like in Cycles.
So be sure to check out the Cycles section of this manual for that.

.. seealso::

   :doc:`Materials </render/shader_nodes/shader/index>`.

Although most BSDFs are supported, many of them are approximations and are not feature complete.

Diffuse BSDF
   Roughness is not supported. Only Lambertian diffusion is supported.

Emission
   Treated as indirect lighting and will only show up in :abbr:`SSR (Screen Space Reflection)`\ s and Probes.

Glass / Refraction BSDF
   Does not refract lights. Does not support Beckmann distribution.
   See :ref:`Refraction limitations <eevee-limitations-refraction>`.

Glossy BSDF
   Does not support Beckmann and Ashikhmin-Shirley distributions.

Subsurface Scattering
   Random Walk sampling is not supported. Per color channel Radius is specified by the default socket value.
   Any link plugged into this socket gets ignored.
   Texture Blur is not accurate for any value other than 0.0 and 1.0.

Transparent BSDF
   Transparency will only have an effect if the Material blend mode is not Opaque.
   Colored and additive transparency are only compatible with "Alpha Blend" mode.

Translucent BSDF
   Does not diffuse the light inside the object. It only lights the object with reversed normals.

Principled BSDF
   Cumulative limitations from Diffuse BSDF, Glossy BSDF, Refraction BSDF and Subsurface Scattering.
   Anisotropy is not supported. Transmission Roughness is not supported. The Sheen layer is a crude approximation.

Volume Absorption
   See :ref:`Volume Limitation <eevee-limitations-volumetrics>`.

Volume Scatter
   The anisotropy parameter will be mixed and averaged for all overlapping volumetric objects,
   which is not physically correct and differs from Cycles.
   Also see :ref:`Volume Limitation <eevee-limitations-volumetrics>`.

Principled Volume
   Same as Volume Scatter. See :ref:`Volume Limitation <eevee-limitations-volumetrics>`.

Holdout
   Partially supported, using :ref:`Blend Modes <bpy.types.Material.blend_method>`
   other than *Alpha* may give incorrect results.

Anisotropic BSDF
   Not supported.

Toon BSDF
   Not supported.

Hair BSDF
   Not supported.

Velvet BSDF
   Not supported.

Principled Hair BSDF
   Not supported.


Input Nodes
-----------

Ambient Occlusion
   The sample count is not used.

Camera Data
   Everything is compatible.

Geometry
   Pointiness is not supported.

Random per Island
   Random per Island is not supported.

Attribute
   Defaults to active UV layer. Only "density", "color", "flame" and "temperature" built-in attributes are supported.
   UVs and Vertex Color layers are supported.

Bevel
   Not supported.

Fresnel
   Everything is compatible.

Hair Info
   The Random output uses a different :abbr:`RNG (Random Number Generator)` algorithm.
   Range and statistical distribution of the values should be the same but the values will be different.

Layer Weight
   Everything is compatible.

Light Path
   Eevee has no real concept of rays. But in order to ease the workflow between Cycles and Eevee
   some of the outputs are supported in particular cases.
   This node makes it possible to tweak indirect lighting in the shader.

   Only a subset of the outputs is supported and the ray depth has not exactly
   the same meaning:

   - *Is Camera*: Supported.
   - *Is Shadow*: Supported.
   - *Is Diffuse*: Supported.
   - *Is Glossy*: Supported.
   - *Is Singular*: Not supported. Same as Is Glossy.
   - *Is Reflection*: Not supported. Same as Is Glossy.
   - *Is Transmission*: Not supported. Same as Is Glossy.
   - *Ray Length*: Not supported. Defaults to 1.0.
   - *Ray Depth*: Indicates the current bounce when baking the light cache.
   - *Diffuse Depth*: Same as Ray Depth but only when baking diffuse light.
   - *Glossy Depth*: Same as Ray Depth but only when baking specular light.
   - *Transparent Depth*: Not supported. Defaults to 0.
   - *Transmission Depth*: Not supported. Same as Glossy Depth.

   .. note::

      Is Glossy does not work with Screen Space Reflections/Refractions
      but does work with reflection planes (whether used with SSR or not).

Object Info
   Everything is compatible.

Particle Info
   Not supported.

Tangent
   Everything is compatible.

Texture Coordinate
   *From Instancer* is not supported.

UV Map
   *From Instancer* is not supported.

Wireframe
   Pixel size option does not give exactly the same output as Cycles. The width can be a bit different.


Other Nodes
-----------

Light Falloff
   Not supported.

Bump
   Imprecision due to less precise derivatives.

Displacement/Vector Displacement
   Not supported.

:abbr:`IES (Illuminating Engineering Society)` Texture
   Not supported.

Image Texture
   Smart Interpolation always uses Cubic interpolation.
   Artifact present using Tube or Sphere projection with linear interpolation.
   This is due to hardware mip-mapping and Anisotropic filtering.
   This kind of artifact will be also visible if the texture coordinates provided are not continuous.
   Using Box projection with *Extend type* set to Clip or Extend is not supported.
   Instead, it will always use Repeat.

Material Output
   Displacement output behavior is broken compared to Cycles.

Wavelength
   Not supported.

Point Density
   Not supported.

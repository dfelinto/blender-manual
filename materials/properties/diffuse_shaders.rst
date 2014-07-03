


Diffuse Shaders
===============


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Diffuse


A diffuse shader determines, simply speaking,
the general color of a material when light shines on it. Most shaders that are designed to
mimic reality give a smooth falloff from bright to dark from the point of the strongest
illumination to the shadowed areas,
but Blender also has other shaders for various special effects.


Common Options
--------------


All diffuse shaders have the following options:
 **Color**
   Select the base *diffuse color* of the material.
 **Intensity**
   The shader's brightness, or more accurately, the amount of incident light energy that is actually diffusely reflected towards the camera.
**Ramp**
   Allows you to set a range of colors for the :guilabel:`Material`\ , and define how the range will vary over a surface. See :doc:`Color Ramps <materials/properties/ramps>` for details.


Technical Details
-----------------


Light striking a surface and then re-irradiated via a Diffusion phenomenon will be scattered, i.e., re-irradiated in all directions isotropically. This means that the camera will see the same amount of light from that surface point no matter what the *incident viewing angle* is. It is this quality that makes diffuse light *viewpoint independent*\ . Of course, the amount of light that strikes the surface depends on the incident light angle. If most of the light striking a surface is reflected diffusely, the surface will have a matte appearance (\ *Light re-irradiated in the diffusion phenomenon.*\ ).

.. figure:: /images/Manual-Part-III-MatGen02.jpg

   Light re-irradiated in the diffusion phenomenon.


 .. admonition:: Shader Names
   :class: nicetip

   Some shaders' names may sound odd - they are traditionally named after the people who first introduced the models on which they are based.


Lambert
-------


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Lambert.jpg
   :width: 320px
   :figwidth: 320px

   Lambert Shader


This is Blender's default diffuse shader, and is a good general all-around workhorse for
materials showing low levels of specular reflection.

`Johann Heinrich Lambert <http://en.wikipedia.org/wiki/Johann_Heinrich_Lambert>`__ (1728-1777)
   was a Swiss mathematician, physicist and astronomer who published works on the reflection of light, most notably the `Beer-Lambert Law <http://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law>`__ which formulates the law of light absorption.

This shader has only the default option, determining how much of available light is reflected.
Default is 0.8, to allow other objects to be brighter.


.. figure:: /images/Manual-2.5-Material-Shader-Lambert-Settings.jpg
   :width: 220px
   :figwidth: 220px

   The Lambert diffuse shader settings.


Oren-Nayar
----------


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Oren-Nayar.jpg
   :width: 320px
   :figwidth: 320px

   Oren-Nayar Shader


Oren-Nayar takes a somewhat more 'physical' approach to the diffusion phenomena as it takes
into account the amount of microscopic roughness of the surface.
`Michael Oren <http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/o/Oren:Michael.html>`__ and `Shree K. Nayar <http://en.wikipedia.org/wiki/Shree_K._Nayar>`__
   Their `reflectance model <http://en.wikipedia.org/wiki/Oren%E2%80%93Nayar_reflectance_model>`__\ , developed in the early 1990s, is a generalization of Lambert's law now widely used in computer graphics.


Options
~~~~~~~

**Roughness**
    The roughness of the surface, and hence, the amount of diffuse scattering.


.. figure:: /images/Manual-2.5-Material-Shader-Oren-Nayar-Settings.jpg
   :width: 200px
   :figwidth: 200px

   The Oren-Nayar diffuse shader settings.


Toon

----


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Toon.jpg
   :width: 320px
   :figwidth: 320px

   Toon Shader, Different Spec


.. figure:: /images/Manual-2.5-Material-Shader-Toon-vary.jpg
   :width: 320px
   :figwidth: 320px

   Toon Shader Variations


The Toon shader is a very 'un-physical' shader in that it is not meant to fake reality but to
produce cartoon cel styled rendering,
with clear boundaries between light and shadow and uniformly lit/shadowed regions.


Options
~~~~~~~

**Size**
   The size of the lit area
**Smooth**
   The softness of the boundary between lit and shadowed areas


.. figure:: /images/Manual-2.5-Material-Shader-Toon-Settings.jpg
   :width: 200px
   :figwidth: 200px

   The Toon diffuse shader settings.


Minnaert
--------


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Minnaert.jpg
   :width: 320px
   :figwidth: 320px

   Minnaert Shader


Minnaert works by darkening parts of the standard Lambertian shader,
so if *Dark* is 1 you get exactly the Lambertian result.
Higher darkness values will darken the center of an object
(where it points towards the viewer).
Lower darkness values will lighten the edges of the object, making it look somewhat velvet.
`Marcel Minnaert <http://en.wikipedia.org/wiki/Marcel_Minnaert>`__ (1893-1970)
   was a Belgian astronomer interested in the effects of the atmosphere on light and images who in 1954 published a book entitled *The Nature of Light and Color in the Open Air*\ .


Options
~~~~~~~

**Dark**
    The darkness of the 'lit' areas (higher) or the darkness of the edges pointing away from the light source (lower).


.. figure:: /images/Manual-2.5-Material-Shader-Minnaert-Settings.jpg
   :width: 200px
   :figwidth: 200px

   The Minnaert diffuse shader settings.


Fresnel
-------


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Fresnel-vary.jpg
   :width: 320px
   :figwidth: 320px

   Various settings for the Fresnel shader, Cook-Torr Specular shader kept at Intensity 0.5, Hardness: 50


.. figure:: /images/Manual-2.5-Material-Shader-Fresnel.jpg
   :width: 320px
   :figwidth: 320px

   Fresnel Shader, Different Spec


With a Fresnel shader the amount of diffuse reflected light depends on the incidence angle, i.
e. from the direction of the light source.
Areas pointing directly towards the light source appear darker;
areas perpendicular to the incoming light become brighter.
`Augustin-Jean Fresnel <http://en.wikipedia.org/wiki/Augustin-Jean_Fresnel>`__ (1788-1827)
   was a French physicist who contributed significantly to the establishment of the theory of wave optics.


Options
~~~~~~~

**Fresnel**
    Power of the Fresnel effect, 5.0 is max.
**Factor**
    Blending factor of the Fresnel factor to blend in, 5.0 is max.


.. figure:: /images/Manual-2.5-Material-Shader-Fresnel-Settings.jpg
   :width: 200px
   :figwidth: 200px

   The Fresnel diffuse shader settings.


..    Comment: <!--
   = Other Options =
   [[File:Manual-2.5-Material-ShadingMenu.png|thumb|Shading menu, default settings]]
   In the separate {{literal|Shading}} tab six more options are available:
   Emit
   :Amount of light to emit
   Ambient
   :Amount of global ambient color the material receives
   Translucency
   :Amount of diffuse shading on the back side
   Shadeless
   :Make this material insensitive to light or shadow
   Tangent Shading
   :Use the material's tangent vector instead of the normal for shading&nbsp;&mdash; for anisotropic shading effects (e.g. soft hair and brushed metal).  This shading was [http://www.blender.org/development/release-logs/blender-242/material-features/ introduced in 2.42]; see also settings for strand rendering in the menu further down and in the Particle System menu.
   Cubic Interpolation
   :Use cubic interpolation for diffuse values, for smoother transitions between light areas and dark areas
   --> .

..    Comment: <!--
   {{Table|
   |-
   | valign="top" | [[Image:Manual - Light - Lamps - Sphere Non-Cubic Shadow.png|thumb|right|200px|Without Cubic enabled.]]
   | valign="top" | [[Image:Manual - Light - Lamps - Sphere Cubic Shadow.png|thumb|right|200px|With Cubic enabled.]]
   | valign="top" | [[Image:Manual - Light - Lamps - Sphere Cubic Shadow Animated.png|thumb|right|200px|Animation switching between Non-Cubic and Cubic shadowing.  You will need a modern, standards compliant, browser to see the animation. Click to View Animation.]]
   }}
   --> .



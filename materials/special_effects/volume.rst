
Volume Rendering
****************

.. figure:: /images/Doc-26-Materials-VolumeRender-Activate.jpg
   :width: 300px
   :figwidth: 300px

   Activation volume rendering


Volume rendering is a method for rendering light as it passes through participating media,
within a 3d region.
The implementation in Blender's sim-physics branch is a physically based model,
which represents the various interactions of light in a volume relatively realistically.


.. figure:: /images/Volumerendering-solid_eq.jpg

   Solid rendering

 The process of rendering a solid surface involves the camera finding a piece of geometry, then calculating the light that bounces from light sources (lamp objects, or other geometry), off the surface, and towards the camera. The light that arrives at the camera is the final colour that's rendered.

.. figure:: /images/Volumerendering-volume_eq.jpg

   Volume rendering

 Rendering a volume works differently. Light enters a 3D region of space (defined as the volume) that may be filled with small particles, such as smoke, mist or clouds.

The light bounces around off the various molecules, being scattered or absorbed,
until some light passes through the volume and reaches the camera.
In order for that volume to be visible, the renderer must figure out how much material the
light has passed through and how it has acted and reacted within that volume,
the volume object needs to contain a 3D region of space, for example a watertight closed mesh,
such as a cube, not just a flat surface like a plane. To get an image,
the renderer has to step through that region, and see how much 'stuff' is there (density)
in order to see how light is absorbed or scattered or whatever. This can be a time consuming
process since it has to check a lot of points in space and evaluate the density at each.


Options
*******

Density
=======

.. figure:: /images/Volumerendering-density.jpg

   Constant density vs textured density


Many things can happen to the light as it passes through the volume,
which will influence the final colour that arrives at the camera.
These represent physical interactions that happen in the real world,
and most of these are dependent on the density of the volume,
which can either be a constant density throughout, or varied, controlled by a texture. It is
by controlling the density that one can get the typical 'volumetric' effects such as clouds or
thick smoke.


.. figure:: /images/Doc-26-Materials-VolumeRender-Options-Density.jpg

   Density options


**Density**
   The base density of the material - other density from textures is added on top
**Density Scale**
   A global multiplier to increase or decrease the apparent density. This can be useful for getting consistent results across different scene scales.


Shading
=======

.. figure:: /images/Volumerendering-scattering1.jpg

   Spot lamp scattering in a constant volume


When light enters a volume from an external source, it doesn't just pass straight through.
Light gets scattered off tiny particles in the volume,
and some proportion of that light reaches the camera. This property makes it possible to see
light beams as they travel though a volume and are scattered towards the eye.


.. figure:: /images/Doc-26-Materials-VolumeRender-Options-Shading.jpg

   Shading options


**Scattering**
   The amount of light that is scattered out of the volume. The more light that is scattered out of the volume, the less it will penetrate through the rest of the volume. Raising this parameter can have the effect of making the volume seem denser, as the light is scattered out quickly at the 'surface' of the volume, leaving the areas internal to the volume darker, as the light doesn't reach it.


Note in the examples below, the less light that is scattered out of the volume,
the more easily it penetrates throughout the volume and to the shadow.

+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
+.. figure:: /images/Manual-volumerendering-scatter-Sc0.5.jpg|.. figure:: /images/Manual-volumerendering-scatter-Sc1.0.jpg|.. figure:: /images/Manual-volumerendering-scatter-Sc2.0.jpg|.. figure:: /images/Manual-volumerendering-scatter-Sc5.0.jpg+
+   :width: 150px                                            |   :width: 150px                                            |   :width: 150px                                            |   :width: 150px                                            +
+   :figwidth: 150px                                         |   :figwidth: 150px                                         |   :figwidth: 150px                                         |   :figwidth: 150px                                         +
+                                                            |                                                            |                                                            |                                                            +
+   Scattering: 0.5                                          |   Scattering: 1.0                                          |   Scattering: 2.0                                          |   Scattering: 5.0                                          +
+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+


Asymmetry
---------

.. figure:: /images/Volumerendering-phase_diagram.jpg
   :width: 300px
   :figwidth: 300px

   Isotropic and Anisotropic scattering


The default method for scattering light in a volume is for the light to be deflected evenly in
all directions - known as Isotropic scattering.
In real life different types of media can scatter light in different angular directions,
known as Anisotropic scattering.
Back-scattering means that light is scattered more towards the incoming light direction, and
forward-scattering means it's scattered along the same direction as the light is travelling.

**Asymmetry**
   Asymmetry controls the range between back-scattering (-1.0) and forward-scattering (1.0). The default value of 0.0 gives Isotropic scattering (even in all directions).


Transmission
------------

Transmission is a general term for light that is transmitted throughout a volume.

This transmitted light can be the result of various different interactions, for example:

- the left over result of incoming light after it has reflected/scattered out of the volume
- the left over result of light after being absorbed by the volume (and converted to heat)

Here, the transmission colour is used to set the end result colour that light becomes after it
is transmitted through the volume.


**Transmission Color**
   The resultant colour of light that is transmitted through the volume.

Note in the examples below, as more light is scattered out of the volume,
there is less available to be transmitted through.

+---------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+
+.. figure:: /images/Manual-volumerendering-tr_y-sc0.5.jpg|.. figure:: /images/Manual-volumerendering-tr_y-sc1.0.jpg|.. figure:: /images/Manual-volumerendering-tr_y-sc2.0.jpg|.. figure:: /images/Manual-volumerendering-tr_y-sc5.0.jpg+
+   :width: 150px                                         |   :width: 150px                                         |   :width: 150px                                         |   :width: 150px                                         +
+   :figwidth: 150px                                      |   :figwidth: 150px                                      |   :figwidth: 150px                                      |   :figwidth: 150px                                      +
+                                                         |                                                         |                                                         |                                                         +
+   Transmission color: Yellow, Scattering: 0.5           |   Transmission color: Yellow, Scattering: 1.0           |   Transmission color: Yellow, Scattering: 2.0           |   Transmission color: Yellow, Scattering: 5.0           +
+---------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+


Emission
--------

Some volumes can emit light where there was none before, via chemical or thermal processes,
such as fire. This light is generated from the volume itself and is independent of light
coming from external sources.

Currently, this emitted light does not affect other volumes or surfaces
(similar to surface material type, 'Emit' option).

**Emission Color**
   The colour of light that is emitted by the volume.
**Emission**
   An intensity multiplier for the emitted colour, for scaling up and down.


+------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Manual-volumerendering-emission-0.25-sc0.5.jpg|.. figure:: /images/Manual-volumerendering-emission-0.25-sc1.0.jpg|.. figure:: /images/Manual-volumerendering-emission-0.25-sc2.0.jpg|.. figure:: /images/Manual-volumerendering-emission-0.25-sc5.0.jpg+
+   :width: 150px                                                  |   :width: 150px                                                  |   :width: 150px                                                  |   :width: 150px                                                  +
+   :figwidth: 150px                                               |   :figwidth: 150px                                               |   :figwidth: 150px                                               |   :figwidth: 150px                                               +
+                                                                  |                                                                  |                                                                  |                                                                  +
+   Emission 0.25, Scattering: 0.5                                 |   Emission 0.25, Scattering: 1.0                                 |   Emission 0.25, Scattering: 2.0                                 |   Emission 0.25, Scattering: 5.0                                 +
+------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+


Reflection
----------

The 'reflection' parameters can be used to tint or scale the light that's scattered out of the
volume. This only affects light that has come from lamps and been scattered out,
it doesn't affect the colour of transmitted or emitted light and is .

These settings are not physically correct because they don't conserve energy - the light
scattering out doesn't affect the remaining light that is transmitted throughout the rest of
the volume. For example, physically speaking,
if the orange components of the light are scattered out of the volume towards the camera,
only the inverse of that (blue) will remain to continue penetrating through the volume,
causing the volume to take on a multi-coloured appearance, which can be difficult to use.
To make it a bit easier to plainly set the colour of the volume,
you can use the reflection parameters to quickly set an overall tint.


**Reflection Color**
   The colour of light that is scattered out of the volume.
**Reflection**
   An intensity multiplier for the reflection, for scaling up and down.


Hints
^^^^^

Ideally try to accomplish as much as you can with the other volume settings and lighting
before using the reflection controls. If you stick to what's physically plausible,
the material will act correctly,
and be more predictable and usable in a wider range of lighting scenarios.
Of course you can always break the rules too!


+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/Manual-volumerendering-reflection-sc0.5.jpg|.. figure:: /images/Manual-volumerendering-reflection-sc1.0.jpg|.. figure:: /images/Manual-volumerendering-reflection-sc2.0.jpg|.. figure:: /images/Manual-volumerendering-reflection-sc5.0.jpg+
+   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                               +
+   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                            +
+                                                               |                                                               |                                                               |                                                               +
+   Reflection: Green, Scattering: 0.5                          |   Reflection: Green, Scattering: 1.0                          |   Reflection: Green, Scattering: 2.0                          |   Reflection: Green, Scattering: 5.0                          +
+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+


+----------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
+.. figure:: /images/Manual-volumerendering-refl_g-tr_y-sc0.5.jpg|.. figure:: /images/Manual-volumerendering-refl_g-tr_y-sc1.0.jpg|.. figure:: /images/Manual-volumerendering-refl_g-tr_y-sc2.0.jpg|.. figure:: /images/Manual-volumerendering-refl_g-tr_y-sc5.0.jpg+
+   :width: 150px                                                |   :width: 150px                                                |   :width: 150px                                                |   :width: 150px                                                +
+   :figwidth: 150px                                             |   :figwidth: 150px                                             |   :figwidth: 150px                                             |   :figwidth: 150px                                             +
+                                                                |                                                                |                                                                |                                                                +
+   Reflection: Green, Transmission: Yellow, Scattering: 0.5     |   Reflection: Green, Transmission: Yellow, Scattering: 1.0     |   Reflection: Green, Transmission: Yellow, Scattering: 2.0     |   Reflection: Green, Transmission: Yellow, Scattering: 5.0     +
+----------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+


Lighting
========

.. figure:: /images/Doc-26-Materials-VolumeRender-Options-Lighting.jpg

   Lighting options


Several shading modes are available,
providing a range of options between fast to render and physically accurate.

**Lighting Mode**
   **Shadeless**
      Shadeless is the simplest, useful for thin, wispy mist or steam.
   **Shadowed**
      Shadowed is similar, but with shadows of external objects.
   **Shaded**
      Shaded uses a volumetric single-scattering method, for self-shading the volume as light penetrates through.
   **Multiple Scattering**
      Allows multiple scatter calculations.
   **Shaded+Multiple Scattering**
      Combines Shaded and Multiple Scattering functionality.


**Shaded Options:**
   **External Shadows**
      Receive shadows from sources outside the volume (temporary).
   **Light Cache**
      Pre-calculate the shading information into a voxel grid, speeds up shading at slightly less accuracy.
   **Resolution**
      Resolution of the voxel grid, low resolutions are faster, high resolutions use more memory.


**Multiple Scattering Options:**
   **Diffusion**
      Diffusion factor, the strength of the blurring effect.
   **Spread**
      Proportional distance over which the light is diffused.
   **Intensity**
      Multiplier for multiple scattered light energy.


Transparency
============

.. figure:: /images/Doc-26-Materials-VolumeRender-Options-Transparency.jpg

   Transparency options


**Mask**
   Mask the Background.
**Z Transparency**
   Use Alpha buffer for transparent faces.
**Raytrace**
   Use Raytracing for Transparent Refraction rendering.


Integration
===========

.. figure:: /images/Doc-26-Materials-VolumeRender-Options-Integration.jpg

   Integration options


**Step Calculation Method**
   Method of calculating the step through the volume.

   **Randomized**
      Randomized method of calculating the step.
   **Constant**
      Constant method of calculating the step.

**Step Size**
   Distance between subsequent volume depth samples. Step Sizes determine how noisy the volume is. Higher values result in lower render times and higher noise.
**Depth Cutoff**
   Stop ray marching early if transmission drops below this luminance - higher values give speedups in dense volumes at the expense of accuracy.


Options
=======

.. figure:: /images/Doc-26-Materials-VolumeRender-Options.jpg

   Material volume options


**Traceable**
   Allow this material to calculate raytracing.
**Full Oversample**
   Force this material to render full shading/textures for all anti-aliasing samples.
**Use Mist**
   Use mist with this material (in world settings).

**Light Group**
   Limit lighting of this material to lamps in this group.
**Exclusive**
   Material uses this group exclusively. Lamps are excluded from other scene lighting.


Examples
********

<these are sandbox edits to the whole shading intro section of the wiki, which groups materials and textures, and gives us an entree into Volumetric shading. Note qualification of Mesh object. Need to investigate shading of other object types...>

Shading is the process and the code which enables an object to be seen in the final render
output. Blender has four methods to shade a mesh object:


- Surface
- Volumetric
- Halo
- Wire

Surface shading indicates that the object is a tangible,
skinned object that has a solid (but possibly pliable) surface, such as a chair, a sword,
or a peach. The surface is described in terms of having a diffuse, specular, mirror,
and transparency.
It may also have a semi-transparent surface and something inside of it that scatters light,
called sub-surface scattering. It may be reflective, such as chrome, smooth plastic,
or metal, and may be partially transparent, such as glass, or liquid.

Volumetric shading treats the object as a volume of space that is filled with microscopic
particles, such as a cloud, smoke, mist, fog, mystical spells, and steam.
As light enters the volume, it is scattered by these particles,
and some of that scattering reaches the eye/camera for us to see.
The volume is described in terms of density, xxx.
The particles may be uniformly colored but have a varying density within the volume,
and so the shape may have darker areas.
The density may be uniformly dispersed throughout the volume, or it may be clumpled,
giving a recognizable shape. Those microscopic particles may give off light themselves,
as if they contained glowing embers or sparks,
or were transmitting some energy field inside the cloud.
That density may be driven by a particle system to create a well-defined jet or emission.

Halo shading turns each vertex of the object into a glob of light, an effect seen with sparks,
pixie dust, glint, and sparkles from, for example, a diamond in bright sunlight.
Halos can also be used to give a rough approximation of a lens flare, which is observed when a
real camera lens looks directly at a bright light source such as the sun.

Wire shading renders each edge of the object as a thin line, like a wire cage, or net.
Wire rendering is very fast and can be used as a proxy material for a more complicated surface
to save time during intermediate renders.

There are two major components to shading: the Material and its Textures.
The color that you see is a function of the light and the shading,
so you need to also check out the lighting section as well.
There are five types of objects in Blender that can be shaded: Mesh, Curve, Surface, Meta,
and Text.
The table below indicates which types of shading are available for each kind of object.
Keep in mind that all types of non-mesh objects can be converted from their type to a Mesh,
so, ultimately, all kinds of shading are available for all kinds of objects


+---------------------------------+---------------------+----+----------+---+
+Shading available per Object type                                          +
+---------------------------------+---------------------+----+----------+---+
+Surface                          |Halo                 |Wire|Volumetric    +
+---------------------------------+---------------------+----+----------+---+
+Mesh                             |yes                  |full|yes       |yes+
+---------------------------------+---------------------+----+----------+---+
+Curve                            |if cyclic or extruded|no  |no            +
+---------------------------------+---------------------+----+----------+---+
+Surface                          |yes                  |no  |yes           +
+---------------------------------+---------------------+----+----------+---+
+Meta                             |yes                  |no  |no            +
+---------------------------------+---------------------+----+----------+---+
+Text                             |yes                  |no  |no            +
+---------------------------------+---------------------+----+----------+---+


..    Comment: <!--
   [[File:1.png|300px|Step Size 1.0]]
   [[File:8.png|300px|Step Size 0.5]]
   [[File:3.png|300px|Step Size 0.3]]
   [[File:4.png|300px|Step Size 0.1]]
   [[File:5.png|300px|Step Size 0.05]]
   [[File:6.png|300px|Step Size 0.02]]
   --> .



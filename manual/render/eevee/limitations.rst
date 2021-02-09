
***********
Limitations
***********

Eevee's goal is to be an interactive render engine. Some features may not be there yet or
may be impossible to implement into Eevee's architecture without compromising performance.

Here is a rather exhaustive list of all the limitations you can expect while working with Eevee.


Cameras
=======

- Only perspective and orthographic projections are currently supported.


Lights
======

- Only 128 active lights can be supported by Eevee in a scene.
- Only 8 Shadowed sun lights can be supported at the same time.
- As of now, lights can only have one color and do not support light node trees.


Light Probes
============

- Eevee only supports up to 128 active Reflection Cubemaps.
- Eevee only supports up to 64 active Irradiance Volumes.
- Eevee only supports up to 16 active Reflection Planes inside the view frustum.


Indirect Lighting
=================

- Volumetrics don't receive light from Irradiance Volumes but do receive world's diffuse lighting.
- Eevee does not support "specular to diffuse" light bounces nor "specular to specular" light bounces.
- All specular lighting is turned off during baking.


.. _eevee-limitations-shadows:

Shadows
=======

- Only 128 active lights can be supported by Eevee in a scene.
- Only 8 Shadowed sun lights can be supported at the same time.


.. _eevee-limitations-volumetrics:

Volumetrics
===========

- Only single scattering is supported.
- Volumetrics are rendered only for the camera "rays". They don't appear in reflections/refractions and probes.
- Volumetrics don't receive light from Irradiance Volumes but do receive diffuse lighting from the world.
- Volumetric shadowing only work in volumetrics. They won't cast shadows onto solid objects in the scene.
- Volumetric shadowing only work for volumes inside the view frustum.
- Volumetric lighting do not respect the lights shapes. They are treated as point lights.


.. _eevee-limitations-dof:

Depth of Field
==============

- Rendered at half resolution which can create blocky pixel artifacts on tiny features that are nearly in focus.
- The near and far defocus buffers are in fact one single continuous texture. This can make some bleeding
  appear on the left and right sides of the image. This can be fixed by using the *overscan* feature.


Screen Space Effects
====================

Eevee is not a ray tracing engine and cannot do ray-triangle intersection.
Instead of this, Eevee uses the depth buffer as an approximated scene representation.
This reduces the complexity of scene scale effects and enables a higher performance.
However, only what is in inside the view can be considered when computing these effects.
Also, since it only uses one layer of depth, only the front-most pixel distance is known.

These limitations creates a few problems:

- The screen space effects disappear when reaching the screen border.
  This can be partially fixed by using the *overscan* feature.
- Screen space effects lack deep information (or the thickness of objects).
  This is why most effects have a thickness parameter to control how to consider potential intersected pixels.
- Blended surfaces are not considered by these effects.
  They are not part of the depth prepass and do not appear in the depth buffer.
- Objects that a part of :ref:`Holdout Collections <bpy.ops.outliner.collection_holdout_set>`
  will not be rendered with screen space effects.


.. _eevee-limitations-ao:

Ambient Occlusion
-----------------

- Objects are treated as infinitely thick, producing overshadowing if the *Distance* is really large.


.. _eevee-limitations-reflections:

Screen Space Reflections
------------------------

- Only one glossy BSDF can emit screen space reflections.
- The evaluated BSDF is currently arbitrarily chosen.
- Screen Space Reflections will reflect transparent objects and objects using Screen Space Refraction
  but without accurate positioning due to the one layer depth buffer.


.. _eevee-limitations-refraction:

Screen Space Refraction
-----------------------

- Only one refraction event is correctly modeled.
- Only opaque and alpha hashed materials can be refracted.


.. _eevee-limitations-sss:

Subsurface Scattering
---------------------

- Only one BSSRDF can produce screen space subsurface scattering.
- The evaluated BSSRDF is currently arbitrarily chosen.
- A maximum of 254 different surfaces can use subsurface scattering.
- Only scaling is adjustable per pixel. Individual RGB radii are adjustable in the socket default value.
- Input radiance from each surfaces are not isolated during the blurring,
  leading to light leaking from surface to surface.


Motion Blur
===========

:doc:`Motion Blur </render/eevee/render_settings/motion_blur>`
is only available in final renders and is not shown in the 3D Viewport
and thus :ref:`Viewport Renders <bpy.ops.render.opengl>`.


.. _eevee-limitations-materials:

Materials
=========

Refractions
   Refraction is faked by sampling the same reflection probe used by the Glossy BSDFs,
   but using the refracted view direction instead of the reflected view direction.
   Only the first refraction event is modeled correctly.
   An approximation of the second refraction event can be used for relatively thin objects using Refraction Depth.
   Using Screen Space refraction will refract what is visible inside the view,
   and use the nearest probe if there is no hit.

   Screen Space Reflections and Ambient Occlusion are not compatible with Screen Space Refraction;
   they will be disabled on the surfaces that use it.
   Surfaces that use Screen Space Refraction will not appear in Screen Space Reflections at the right place.
   Surfaces that use Screen Space Refraction will not cast Ambient Occlusion onto other surfaces.

Volume Objects
   Object volume shaders will affect the whole bounding box of the object.
   The shape of the volume must be adjusted using procedural texturing inside the shader.


Shader Nodes
============

- All BSDF's are using approximations to achieve realtime performance
  so there will always be small differences between Cycles and Eevee.
- Some utility nodes are not yet compatible with Eevee (e.g. Sky Texture node).

.. seealso::

   For a full list of unsupported nodes see :doc:`Nodes Support </render/eevee/materials/nodes_support>`.


Memory Management
=================

In Eevee, :abbr:`GPU (Graphic Processing Unit, also known as Graphics Card)`
Memory management is done by the GPU driver.
In theory, only the needed textures and meshes (now referred as "the resources") for a single draw call
(i.e. one object) needs to fit into the GPU memory.

So if the scene is really heavy,
the driver will swap things in and out to make sure all objects are rendered correctly.

In practice, using too much GPU memory can make the GPU driver crash, freeze, or kill the application.
So be careful of what you ask.

There is no standard way of estimating if the resources will fit into the GPU memory and/or
if the GPU will render them successfully.


CPU Rendering
=============

Being a rasterization engine, Eevee only uses the power of
the :abbr:`GPU (Graphic Processing Unit, also known as Graphics Card)` to render.
There is no plan to support :abbr:`CPU (Central Processing Unit)` (software) rendering
as it would be very inefficient. CPU power is still needed to handle high scene complexity
as the geometry must be prepared by the CPU before rendering each frame.


Multiple GPU Support
====================

There is currently no support for
multiple :abbr:`GPU (Graphic Processing Unit, also known as Graphics Card)` systems.


Headless Rendering
==================

There is currently no support for using Eevee on headless systems (i.e. without a Display Manager).

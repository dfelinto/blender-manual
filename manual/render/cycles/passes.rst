
Render Passes
*************

Layers
======

Render layers are used to render different objects in the scene into different images.
This way they can, for example, be color corrected or otherwise manipulated separately and
then recomposed in compositing later.

Which objects contribute to which render layers are defined by these layer settings:


:guilabel:`Scene Layers`
   Only objects on these layers will contribute to the image.
:guilabel:`Camera Layers`
   Objects on these layers are directly visible to the camera. 
   When an object is in the scene layers but not camera layers,
   it will still cast shadows or be visible in reflections, so it's still indirectly visible.
   This is equivalent to disabling the Camera in the Ray Visibility panel for the object.
   The way this works may be somewhat confusing at first,
   but it's designed such that render layers can be recomposed
   to give the full render, without any missing shadows or reflections.
:guilabel:`Mask Layers`
   Objects on these will mask out other objects appearing behind them.
   This is equivalent to assigning a Holdout shader for camera rays to the objects on such layers.
:guilabel:`Exclude Layers`
   Scene layers are shared between all render layers;
   however sometimes it's useful to leave out some object influence for a particular render layer.
   That's what this option allows you to do.


Lighting Passes
===============

:guilabel:`Diffuse Direct`
   Direct lighting from diffuse BSDFs. We define direct lighting as coming from lamps, emitting surfaces,
   the background, or ambient occlusion after a single reflection or transmission off a surface.
   BSDF color is not included in this pass.
:guilabel:`Diffuse Indirect`
   Indirect lighting from diffuse BSDFs. We define indirect lighting as coming from lamps,
   emitting surfaces or the background after more than one reflection or transmission off a surface.
   BSDF color is not included in this pass.
:guilabel:`Diffuse Color`
   Color weights of diffuse BSDFs. These weights are the color input socket for BSDF nodes,
   modified by any Mix and Add Shader nodes.

:guilabel:`Glossy Direct, Indirect, Color`
   Same as above, but for glossy BSDFs.
:guilabel:`Transmission Direct, Indirect, Color`
   Same as above, but for transmission BSDFs.
:guilabel:`Subsurface Direct, Indirect, Color`
   Same as above, but for subsurface BSDFs.

:guilabel:`Emission`
   Emission from directly visible surfaces.
:guilabel:`Environment`
   Emission from the directly visible background. When the film is set to transparent,
   this can be used to get the environment color and composite it back in.

:guilabel:`Shadow`
   Shadows from lamp objects.
:guilabel:`Ambient Occlusion`
   Ambient occlusion from directly visible surfaces. BSDF color or AO factor is not included; i.e.
   it gives a 'normalized' value between 0 and 1.

Note that :ref:`transparent BSDFs are given special treatment </render/cycles/light_paths>`
a fully transparent surface is treated as if there is no surface there at all;
a partially transparent surface is treated as if only part of the light rays can pass through.
This means it is not included in the Transmission passes;
for that a glass BSDF with index of refraction 1.0 can be used.


Combining
^^^^^^^^^

All these lighting passes can be combined to produce the final image as follows:


.. figure:: /images/Cycles_passes_combine.jpg


Data Passes
===========

:guilabel:`Z`
   Z depth.
:guilabel:`Mist`
   Mist value between 0.0 and 1.0, using settings from the Mist Pass panel in world properties.
:guilabel:`Normal`
   Surface normal used for shading.
:guilabel:`UV`
   Default render UV coordinates.
:guilabel:`Object Index`
   Pass index of object.
:guilabel:`Material Index`
   Pass index of material.
:guilabel:`Vector`
   Motion vectors for the vector blur node. The four components consist of 2D vectors giving the motion towards the
   next and previous frame position in pixel space.

The Z, Object Index and Material Index passes are not antialiased.
This is done because such values can't really be blended correctly.

:guilabel:`Alpha Threshold`
   Z, Index, normal,
   UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold.
   With value 0.0 the first surface hit will always write to these passes, regardless of transparency.
   With higher values surfaces that are mostly transparent can be skipped until an opaque surface is encountered.

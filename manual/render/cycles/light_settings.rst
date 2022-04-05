
**************
Light Settings
**************

.. reference::

   :Panel:     :menuselection:`Properties --> Light` and :menuselection:`Shader Editor --> Sidebar --> Settings`

Next to lighting from the background and any object with an emission shader,
lights are another way to add light into the scene.
The difference is that they are not directly visible in the rendered image,
and can be more easily managed as objects of their own type.


Common
======

:doc:`Light settings </render/lights/light_object>` for all renderers.


Cycles
======

.. _bpy.types.CyclesLightSettings.max_bounces:

Max Bounces
   Maximum number of times light from the light is allowed to :term:`Bounce <Light Bounces>`.
   Limited by :ref:`scene-wide bounce settings <bpy.types.CyclesRenderSettings.max_bounces>`.

.. _bpy.types.CyclesLightSettings.cast_shadow:

Cast Shadow
   By disabling this option, light from lights will not be blocked by objects in between.
   This can speed up rendering by not having to trace rays to the light source.

.. _bpy.types.CyclesLightSettings.use_multiple_importance_sampling:

Multiple Importance Sample
   By default lights use only direct light sampling. For area lights and sharp glossy reflections, however,
   this can be noisy,
   and enabling this option will enable indirect light sampling to be used in addition to reduce noise.

.. _bpy.types.CyclesLightSettings.is_caustics_light:

Shadow Caustics
   Mark a light as a refractive caustic caster. This setting can be used in conjunction with the
   :ref:`Cast and Receive caustics object settings <bpy.types.CyclesObjectSettings.is_caustics_caster>`
   to selectively speed up refractive caustic rendering of select objects.


Area Lights
===========

.. _render-cycles-lights-area-portals:

Portals
   Area lights can also function as light portals to help sample the environment light,
   and significantly reduce noise in interior scenes.
   Note that rendering with portals is usually slower, but as it converges more quickly, less samples are required.

   Light portals work by enabling the *Portal* option, and placing areas lights in
   windows, door openings, and any place where light will enter the interior.

   In outdoor scenes most rays do not bounce much and just fly off into the sky and therefore,
   light portals are not helpful for outdoor scenes.

   .. figure:: /images/render_cycles_light-settings_portals2.jpg
   .. figure:: /images/render_cycles_light-settings_portals.jpg

      White Room model by Jay Hardy.


Beam Shape
----------

Todo.

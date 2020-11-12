
**************
Light Settings
**************

.. admonition:: Reference
   :class: refbox

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

Samples
   For the branch path tracing integrator, this specifies the number of direct light samples per AA sample.
   Point lights might need only one sample, while area lights typically need more.
Max Bounces
   Maximum number of times light from the light is allowed to :term:`Bounce <Light Bounces>`.
   Limited by :ref:`scene-wide bounce settings <cycles-bounces>`.
Cast Shadow
   By disabling this option, light from lights will not be blocked by objects in between.
   This can speed up rendering by not having to trace rays to the light source.
Multiple Importance Sample
   By default lights use only direct light sampling. For area lights and sharp glossy reflections, however,
   this can be noisy,
   and enabling this option will enable indirect light sampling to be used in addition to reduce noise.


.. _render-cycles-lights-area-portals:

Light Portals
=============

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

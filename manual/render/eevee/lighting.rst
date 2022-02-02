
**************
Light Settings
**************

.. reference::

   :Panel:     :menuselection:`Properties --> Light` and :menuselection:`Shader Editor --> Sidebar --> Options`

Next to lighting from the background and any object with an emission shader,
lights are another way to add light into the scene.
The difference is that they are not directly visible in the rendered image,
and can be more easily managed as objects of their own type.


Common
======

:doc:`Light settings </render/lights/light_object>` for all renderers.


.. _bpy.types.Light.use_custom_distance:
.. _bpy.types.Light.cutoff_distance:

Eevee
=====

Specular
   Specular Light intensity multiplier. Use it for artistic control.
   Defines the intensity with which the light object will be visible in reflections on the surface of specular objects,
   like metals or mirrors.
   Setting this to 0 will make the light object disappear from specular reflections. Keep it exactly at 1.0 for
   photo-realistic results.
Custom Distance
   If enabled, uses *Distance* as the custom attenuation distance instead of global Light Threshold.
   In order to avoid long setup times, this distance is first computed
   automatically based on a light threshold. The distance is computed
   at the light origin and using the inverse square falloff.

   Distance
      Specifies where light influence will be set to 0.

   .. seealso::

      Global :doc:`Light Threshold </render/eevee/render_settings/shadows>`.

.. note::

   The light's *Power*/*Strength* affect both specular and diffuse light.


.. _bpy.types.*Light.shadow:

Shadows
=======

Common Parameters
-----------------

Clip Start
   Distance from the light object at which the shadow map starts.
   Any object which is closer to the light than Clip Start will not cast shadows.
   *Clip Start* is only available for point, spot and area lights.

Bias
   Bias applied to the depth test to reduce self-shadowing artifacts.
   This determines, what size of surface details (for example, bumps) will cast shadows on the object itself.
   If this value is low, small bumps will cast shadows on the object's surface.
   This might cause jagged shadow edge between the sunny and shadowy side of the object,
   but it can be smoothed out by turning on :doc:`Soft Shadows </render/eevee/render_settings/shadows>`


Contact Shadows
---------------

This type of shadow exists to fix light leaking caused by bias or shadow map undersampling.
It uses the depth buffer to find occluders (just like Screen Space Reflections).
However, just like Screen Space Reflections it has the same limitations,
namely, unknown object thickness and effect disappearing at screen edges.

.. tip::

   The distance of action of Contact Shadows should remain quite small.
   They are not accurate enough to shadow the entire scene.

Distance
   World space distance in which to search for screen space occluder.

Bias
   Bias applied to the ray tracing to reduce self-shadowing artifacts.

Thickness
   Pixel thickness used to detect occlusion, treating any potential occluder as this thick.


.. _eevee-cascaded-shadow-map:

Cascaded Shadow Map
-------------------

Sun lights usually illuminate a large scene with many objects, some close, some far away.
To optimize shadow calculation in this situation, a technique called Cascaded Shadow Maps is used.
The distance between the camera's near clip and far clip point is divided into as many equal intervals
(called cascades) as you set the Count parameter below.
For each cascade a different resolution shadow will be displayed: higher resolution for closer cascades and lower
resolution for distant ones.
Do note that cascade shadow maps are always updated because they depend on the camera position or your view origin in
the 3D-Viewport. This means they have a high performance impact.

.. note::

   In orthographic view the cascades cover the whole depth range of the camera
   with an evenly distributed shadow precision.

Count
   Number of cascades to use. More cascades means better shadow precision but a lower update rate.

Fade
   When the Fade is greater than 0, the size of each cascade (distance interval) is increased so that neighboring
   cascades overlap. Then a fade is applied in the overlapping region to provide a smooth transition between cascades.
   Higher values mean the cascade's size is increased more, which decreases the available shadow resolution
   inside the cascade since some of it is used in the overlapping region.

Max Distance
   Distance away from the view origin (or camera origin if in camera view) to cover by the cascades.
   If the view far clip distance is lower than Max Distance, the view far clip distance will be used.
   Only works in perspective view.

Distribution
   Puts more resolution towards the near clip plane. Only works in perspective view.

.. seealso:: :ref:`Limitations <eevee-limitations-shadows>`.


Limitations
===========

- Unlike in Cycles, the *Size* of spot lights does not change the softness of the cone.

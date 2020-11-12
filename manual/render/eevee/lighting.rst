
**************
Light Settings
**************

.. admonition:: Reference
   :class: refbox

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
   Specular Light intensity multiplier. Use it for more artistic control.
   Setting this to anything but 1.0 will yield non-photorealistic result.
Custom Distance
   If enabled uses *Distance* as the custom attenuation distance instead of global light threshold.
   In order to avoid long setup times, this distance is first computed
   automatically based on a light threshold. The distance is computed
   at the light origin and using the inverse square falloff.

   Distance
      Specifies where light influence will be set to 0.

   .. seealso::

      :doc:`Light Threshold </render/eevee/render_settings/shadows>`.

.. note::

   The light's *Power*/*Strength* affect both specular and diffuse light.


.. _bpy.types.*Light.shadow:

Shadows
=======

Common Parameters
-----------------

Clip Start
   Distance from the light object at which the shadow map starts.
   Any object before this distance will not appear to cast shadows.
   *Clip Start* will only appear for point, spot and area lights.

Bias
   Bias applied to the depth test to reduce self shadowing artifacts.


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

These special kind of shadow maps are used by Sun lights.
This is because they can shadow large scenes by distributing multiple shadow maps over the frustum range.
Each cascade covers a different portion of the view frustum.
Do note that cascade shadow maps are always updated because they are view dependent.
This means they have a high performance impact.

.. note::

   In orthographic view the cascades cover the whole depth range of the camera
   with an evenly distributed shadow precision.

Count
   Number of cascades to use. More cascades means better precision but a lower update rate.

Fade
   Fade transition area between two cascades.
   Higher values means less overall resolution because cascades need to overlap.

Max Distance
   Distance away from the view origin (or camera origin if in camera view) to cover by the cascade.
   If the view far clip distance is lower than Max Distance, the view far clip distance will be used.
   Only works in perspective view.

Distribution
   Puts more resolution towards the near clip plane. Only works in perspective view.

.. seealso:: :ref:`Limitations <eevee-limitations-shadows>`.


Limitations
===========

- Unlike in Cycles, the *Size* of spot lights does not change the softness of the cone.

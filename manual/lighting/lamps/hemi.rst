
Hemi Lamp
*********

.. figure:: /images/Manual-Part-V-HemiScheme.jpg
   :width: 250px
   :figwidth: 250px

   Hemi light conceptual scheme


The :guilabel:`Hemi` lamp provides light from the direction of a 180- hemisphere,

designed to simulate the light coming from a heavily clouded or otherwise uniform sky.
In other words, it is a light which is shed, uniformly,
by a glowing dome surrounding the scene.

Similar to the :guilabel:`Sun` lamp, the :guilabel:`Hemi` 's location is unimportant,
while its orientation is key.

The :guilabel:`Hemi` lamp is represented with four arcs,
visualizing the orientation of the hemispherical dome,
and a dashed line representing the direction in which the maximum energy is radiated,
the inside of the hemisphere.


Options
=======

.. figure:: /images/25-Manual-Lighting-Lamps-Hemi.jpg
   :width: 307px
   :figwidth: 307px

   Hemi lamp's panel


:guilabel:`Energy` and :guilabel:`Color`
   These settings are common to most types of lamps, and are described in :doc:`Light Properties </lighting/lights/light_properties>`.

:guilabel:`Layer`, :guilabel:`Negative`,\ :guilabel:`Specular`, and :guilabel:`Diffuse`
   These settings control what the lamp affects, as described in :doc:`What Light Affects </lighting/lights/what_light_affects>`.

The :guilabel:`Hemi` lamp has no light falloff settings: it always uses a constant attenuation
(i.e. no attenuation).

Since this lamp is the only lamp which cannot cast any shadow,
the :guilabel:`Shadow` panel is absent.



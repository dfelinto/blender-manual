
..    TODO/Review: {{review|im= examples}} .


Sun Lamp
========

A :guilabel:`Sun` lamp provides light of constant intensity emitted in a single direction.
A :guilabel:`Sun` lamp can be very handy for a uniform clear daylight open-space illumination.
In the 3D view,
the :guilabel:`Sun` light is represented by an encircled black dot with rays emitting from it,
plus a dashed line indicating the direction of the light.

This direction can be changed by rotating the :guilabel:`Sun` lamp, like any other object, but because the light is emitted in a constant direction, the location of a :guilabel:`Sun` lamp does not affect the rendered result (unless you use the :doc:`"sky & atmosphere" option <lighting/lamps/sun/sky_and_atmosphere>`\ ).


.. figure:: /images/25-Manual-Lighting-Lamps-Sun-LampPanel.jpg
   :width: 304px
   :figwidth: 304px

   Sun lamp panel


Lamp options
------------

:guilabel:`Energy` and :guilabel:`Color`
   These settings are common to most types of lamps, and are described in :doc:`Light Properties <lighting/lights/light_properties>`\ .
:guilabel:`Negative`\ ,  :guilabel:`This Layer Only`\ , :guilabel:`Specular`\ , and :guilabel:`Diffuse`
   These settings control what the lamp affects, as described in :doc:`What Light Affects <lighting/lights/what_light_affects>`\ .

The :guilabel:`Sun` lamp has no light falloff settings: it always uses a constant attenuation
(i.e. no attenuation!).


Sky & Atmosphere
----------------

.. figure:: /images/25-Manual-Lighting-Lamps-Sun-SkyAtmoPanel.jpg
   :width: 304px
   :figwidth: 304px

   Sky & Atmosphere panel


Various settings for the appearance of the sun in the sky, and the atmosphere through which it shines, are available. For details, see :doc:`Sky and Atmosphere <lighting/lamps/sun/sky_and_atmosphere>`\ .


Shadow
------

.. figure:: /images/25-Manual-Lighting-Lamps-Sun-ShadPanel.jpg
   :width: 304px
   :figwidth: 304px

   Shadow panel


The :guilabel:`Sun` light source can only cast ray-traced shadows. It shares with other lamp types the same common shadowing options, described in :doc:`Shadows Properties <lighting/shadows/properties>`\ .

The ray-traced shadows settings of this lamp are shared with other lamps, and are described in :doc:`Raytraced Properties <lighting/shadows/raytraced_properties>`\ .



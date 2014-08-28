
..    TODO/Review: {{review|im=examples}} .


Point Lamp
**********

.. figure:: /images/25-Manual-Lighting-Lamps-Point.jpg
   :width: 200px
   :figwidth: 200px

   Point lamp


The :guilabel:`Point` lamp is an omni-directional point of light, that is,
a point radiating the same amount of light in all directions. It's visualized by a plain,
circled dot. Being a point light source, the direction of the light hitting an object's
surface is determined by the line joining the lamp and the point on the surface of the object
itself.

Light intensity/energy decays based on (among other variables)
distance from the :guilabel:`Point` lamp to the object. In other words,
surfaces that are further away are rendered darker.


Lamp Options
============

:guilabel:`Distance`, :guilabel:`Energy` and :guilabel:`Color`
   These settings are common to most types of lamps, and are described in :doc:`Light Properties </lighting/lights/light_properties>`.

:guilabel:`Negative`, :guilabel:`This Layer Only`, :guilabel:`Specular`, and  :guilabel:`Diffuse`
   These settings control what the lamp affects, as described in :doc:`What Light Affects </lighting/lights/what_light_affects>`.

:guilabel:`Falloff` and :guilabel:`Sphere`
   These settings control how the light of the :guilabel:`Lamp` decays with distance. See :doc:`Light Attenuation </lighting/lights/light_attenuation>` for details.


Shadows
=======

.. figure:: /images/25-Manual-Lighting-Lamps-PointPanel-Noshad.jpg
   :width: 307px
   :figwidth: 307px

   Without ray shadows


.. figure:: /images/25-Manual-Lighting-Lamps-PointPanel-Rayshad.jpg
   :width: 307px
   :figwidth: 307px

   Point lamp with ray shadows and Adaptive QMC sample generator enabled


The :guilabel:`Point` light source can only cast ray-traced shadows. It shares with other lamp types the common shadow options described in :doc:`Shadow Properties </lighting/shadows/properties>`.

The ray-traced shadows settings of this lamp are shared with other lamps, and are described :doc:`Raytraced Properties </lighting/shadows/raytraced_properties>`.



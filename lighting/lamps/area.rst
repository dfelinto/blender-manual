
..    TODO/Review: {{review|im=examples}} .


Area Lamp
=========

The :guilabel:`Area` lamp simulates light originating from a surface (or surface-like)
emitter. For example, a TV screen, your supermarket's neon lamps, a window,
or a cloudy sky are just a few types of area lamp. The area lamp produces shadows with soft
borders by sampling a lamp along a grid the size of which is defined by the user.
This is in direct contrast to point-like artificial lights which produce sharp borders.


.. figure:: /images/25-Manual-Lighting-Lamps-Area-ComOptions.jpg
   :width: 308px
   :figwidth: 308px

   Commons Options


Lamp options
------------

:guilabel:`Distance`\ , :guilabel:`Energy` and :guilabel:`Color`
   These settings are common to most types of lamps, and are described in :doc:`Light Properties <lighting/lights/light_properties>`\ .

   Note that the :guilabel:`Distance` setting is much more sensitive and important for :guilabel:`Area` lamps than for others; usually any objects within the range of :guilabel:`Distance` will be blown out and overexposed. For best results, set the :guilabel:`Distance` to just below the distance to the object that you want to illuminate.

:guilabel:`Gamma`
    Amount to gamma correct the brightness of illumination. Higher values give more contrast and shorter falloff.

    The :guilabel:`Area` lamp doesn't have light falloff settings. It uses an "inverse quadratic" attenuation law. The only way to control its falloff is to use the :guilabel:`Distance` and/or :guilabel:`Gamma` settings.

:guilabel:`This Layer Only`\ , :guilabel:`Negative`\ , :guilabel:`Specular` and :guilabel:`Diffuse`
   These settings control what the lamp affects, as described in :doc:`What Light Affects <lighting/lights/what_light_affects>`\ .


Shadows
-------

Area light ray-traced shadows are described here: :doc:`Raytraced Shadows <lighting/lamps/area/raytraced_shadows>`\ .

When an :guilabel:`Area` light source is selected,
the :guilabel:`Shadow` panel has the following default layout:


+---------------------------------------------------------------------------+--------------------------------------------------------------+
+.. figure:: /images/25-Manual-Lighting-Lamps-Area-AdapQMC.jpg              |.. figure:: /images/25-Manual-Lighting-Lamps-Area-ContJitt.jpg+
+   :width: 300px                                                           |   :width: 300px                                              +
+   :figwidth: 300px                                                        |   :figwidth: 300px                                           +
+                                                                           |                                                              +
+   Adaptive QMC settings                                                   |   Constant Jittered settings                                 +
+---------------------------------------------------------------------------+--------------------------------------------------------------+
+The :guilabel:`Shadow` panel when :guilabel:`Area` light source is selected                                                               +
+---------------------------------------------------------------------------+--------------------------------------------------------------+


Area Shape
----------

The shape of the area light can be set to :guilabel:`Square` or :guilabel:`Rectangle`\ .


.. figure:: /images/25-Manual-Lighting-Lamps-Area-Square.jpg
   :width: 308px
   :figwidth: 308px

   Square options


.. figure:: /images/25-Manual-Lighting-Lamps-Area-Rect.jpg
   :width: 308px
   :figwidth: 308px

   Rectangle options


:guilabel:`Square`\ /\ :guilabel:`Rectangular`
    Emit light from either a square or a rectangular area
:guilabel:`Size`\ /\ :guilabel:`Size X`\ /\ :guilabel:`Size Y`
    Dimensions for the :guilabel:`Square` or :guilabel:`Rectangle`


.. admonition:: Shape Tips
   :class: note

   Choosing the appropriate shape for your :guilabel:`Area` light will enhance the believability of your scene.
   For example, you may have an indoor scene and would like to simulate light entering through a window.
   You could place a :guilabel:`Rectangular` area lamp in a window (vertical) or from neons (horizontal)
   with proper ratios for :guilabel:`Size X` and :guilabel:`Size Y`. For the simulation of the light emitted by a
   TV screen a vertical :guilabel:`Square` area lamp would be better in most cases.




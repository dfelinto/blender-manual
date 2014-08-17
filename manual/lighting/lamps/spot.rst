
..    TODO/Review: {{review|text=like 2.4?}} .


Spot Lamp
*********

A :guilabel:`Spot` lamp emits a cone-shaped beam of light from the tip of the cone,
in a given direction.

The :guilabel:`Spot` light is the most complex of the light objects and indeed,
for a long time,
among the most used thanks to the fact that it was the only one able to cast shadows.
Nowadays, with a ray tracer integrated into Blender's internal render engine,
all lamps can cast shadows (except :guilabel:`Hemi`). Even so,
:guilabel:`Spot` lamps' shadow buffers are much faster to render than ray-traced shadows,
especially when blurred/softened,
and spot lamps also provide other functionality such as "volumetric" halos.


Lamp options
============

.. figure:: /images/25-Manual-Lighting-Lamps-Spot-LampOptions.jpg
   :width: 307px
   :figwidth: 307px

   Common Lamp options of a Spot


:guilabel:`Distance`, :guilabel:`Energy` and :guilabel:`Color`
   These settings are common to most types of lamps, and are described in :doc:`Light Properties <lighting/lights/light_properties>`.
:guilabel:`This Layer Only`, :guilabel:`Negative`, :guilabel:`Diffuse` and :guilabel:`Specular`
   These settings control what the lamp affects, as described in :doc:`What Light Affects <lighting/lights/what_light_affects>`.
:guilabel:`Light Falloff` and :guilabel:`Sphere`
   These settings control how the light of the :guilabel:`Spot` decays with distance. See :doc:`Light Attenuation <lighting/lights/light_attenuation>` for details.


.. figure:: /images/25-Manual-Lighting-Lamps-Spot-Terms.jpg
   :width: 610px
   :figwidth: 610px

   Changing the Spot options also changes the appearance of the spotlight as displayed in the 3D View


Shadows
=======

.. figure:: /images/25-Manual-Lighting-Lamps-Spot-RayPanel.jpg
   :width: 306px
   :figwidth: 306px

   Shadow panel set to Ray Shadow


Spotlights can use either ray-traced shadows or buffered shadows.
Either of the two can provide various extra options.
Ray-traced shadows are generally more accurate,
with extra capabilities such as transparent shadows, although they are quite slower to render.

:guilabel:`No Shadow`
   Choose this to turn shadows off for this spot lamp.  This can be useful to add some discreet directed light to a scene.
:guilabel:`Buffer Shadow`
   :guilabel:`Buffered Shadows` are also known as depth map shadows. Shadows are created by calculating differences in the distance from the light to scene objects. See :doc:`Buffered Shadows <lighting/lamps/spot/buffered_shadows>` for full details on using this feature.
   Buffered shadows are more complex to set up and involve more faking, but the speed of rendering is a definite advantage. Nevertheless, it shares with other lamp types common shadow options described in :doc:`Shadows Properties <lighting/shadows/properties>`.
:guilabel:`Ray Shadow`
   The ray-traced shadows settings of this lamp are shared with other lamps, and are described in :doc:`Raytraced Properties <lighting/shadows/raytraced_properties>`.


Spot Shape
==========

:guilabel:`Size`

   The size of the outer cone of a :guilabel:`Spot`,
   which largely controls the circular area a :guilabel:`Spot` light covers.
   This slider in fact controls the angle at the top of the lighting cone,
   and can be between ``1.0- `` and ``180.0``.


+------------------------------------------------------------+------------------------------------------------------------+
+.. figure:: /images/25-Manual-Lighting-Lamps-Spot-Size45.jpg|.. figure:: /images/25-Manual-Lighting-Lamps-Spot-Size60.jpg+
+   :width: 300px                                            |   :width: 300px                                            +
+   :figwidth: 300px                                         |   :figwidth: 300px                                         +
+------------------------------------------------------------+------------------------------------------------------------+
+Changing the spot :guilabel:`Size` option                                                                                +
+------------------------------------------------------------+------------------------------------------------------------+


:guilabel:`Blend`
   The :guilabel:`Blend` slider controls the inner cone of the :guilabel:`Spot`. The :guilabel:`Blend` value can be between **0.0** and **1.0**. The value is proportional and represents that amount of space that the inner cone should occupy inside the outer cone (:guilabel:`Size`).

   The inner cone boundary line indicates the point at which light from the :guilabel:`Spot` will start to blur/soften; before this point its light will mostly be full strength. The larger the value of :guilabel:`Blend` the more blurred/soft the edges of the spotlight will be, and the smaller the inner cone's circular area will be (as it starts to blur/soften earlier).

   To make the :guilabel:`Spot` have a sharper falloff rate and therefore less blurred/soft edges, decrease the value of :guilabel:`Blend`. Setting :guilabel:`Blend` to **0.0** results in very sharp spotlight edges, without any transition between light and shadow.

   The falloff rate of the :guilabel:`Spot` lamp light is a ratio between the :guilabel:`Blend` and :guilabel:`Size` values; the larger the circular gap between the two, the more gradual the light fades between :guilabel:`Blend` and :guilabel:`Size`.

   :guilabel:`Blend` and :guilabel:`Size` only control the :guilabel:`Spot` light cone's aperture and softness ("radial" falloff); they do not control the shadow's softness as shown below.


+----------------------------------------------------------------------------------+
+.. figure:: /images/Manual_-_Shadow_&_Spot_-_Spotlight_-_Render_-_Sharp_Shadow.jpg+
+   :width: 400px                                                                  +
+   :figwidth: 400px                                                               +
+                                                                                  +
+   Render showing the soft edge spotlighted area and the sharp/hard object shadow +
+----------------------------------------------------------------------------------+


   Notice in the picture above that the object's shadow is sharp as a result of the ray tracing, whereas the spotlight edges are soft. If you want other items to cast soft shadows within the :guilabel:`Spot` area, you will need to alter other shadow settings.

:guilabel:`Square`
   The :guilabel:`Square` button makes a :guilabel:`Spot` light cast a square light area, rather than the default circular one.
:guilabel:`Show Cone`
   Draw a transparent cone in 3D view to visualize which objects are contained in it.
:guilabel:`Halo`
   Adds a volumetric effects to the spot lamp.  See :doc:`Spot Halos <lighting/lamps/spot/halos>`.



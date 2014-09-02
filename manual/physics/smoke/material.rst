..    TODO/Review: {{review}} .

Smoke Material
**************

Create the Material
===================

Simulating the smoke is easy, however rendering it is not.


.. figure:: /images/render.jpg
   :width: 300px
   :figwidth: 300px

   The Render without the correct smoke material.


Rendering at this point will result in just the big cube (Image, :kbd:`F12`)
or in a crash (Animation, :kbd:`ctrl-F12`).

The material must be a volumetric material with a Density of 0, and a high Density Scale.


.. figure:: /images/material.jpg
   :width: 300px
   :figwidth: 300px

   The material settings.


The first issue can easily be fixed by working on the material and texture of the domain cube.
Smoke requires a complex material to render correctly. Select the big cube and go to the material tab.
There change the material to 'Volume' and set the density to 0.
If you set the density to values bigger than 0 the domain cube will be filled with the volume material.
The `other settings <http://wiki.blender.org/index.php/User:Broken/VolumeRenderingDev>`__ will affect the smoke,
though. We'll cover those later.


+------------------------------------+---------------------------------------+--------------------------------------------------------------+
+.. figure:: /images/Material_tab.jpg|.. figure:: /images/Material_volume.jpg|.. figure:: /images/Density_0.jpg                             +
+   :width: 200px                    |   :width: 200px                       |   :width: 200px                                              +
+   :figwidth: 200px                 |   :figwidth: 200px                    |   :figwidth: 200px                                           +
+                                    |                                       |                                                              +
+   Go to the material tab           |   Smoke needs a volume material       |   Density applies to the cube only, so we need to set it to 0+
+------------------------------------+---------------------------------------+--------------------------------------------------------------+


Add the Texture
===============

In addition, Smoke requires its own texture. Blender 2.5 has a new texture just for rendering smoke called :doc:`Voxel Data </textures/types/volume>`. You must remember to set the domain object and change the influence.


.. figure:: /images/d.jpg
   :width: 300px
   :figwidth: 300px

   The texture settings.


Go to the texture tab and change the type to 'Voxel Data'.
Under the Voxel Data-Settings set the domain object to our domain cube
(it should be listed just as 'Cube' since we are using Blender's default cube.
Under Influence check 'Density' and leave it at 1.000
(Emission should be automatically checked, too).
Now you should be able to render single frames. You can choose to color your smoke as well,
by turning "Emmision Color" back on.


.. tip:: To see the smoke more clearly

   Under the world tab, chose a very dark color for the horizon.


+----------------------------------------+------------------------------------+----------------------------------------+
+.. figure:: /images/Texture_tab.jpg     |.. figure:: /images/Texture_type.jpg|.. figure:: /images/Voxel_domain.jpg    +
+   :width: 200px                        |   :width: 200px                    |   :width: 200px                        +
+   :figwidth: 200px                     |   :figwidth: 200px                 |   :figwidth: 200px                     +
+                                        |                                    |                                        +
+   We need to add a texture of the smoke|   Type should be Voxel Data        |   The domain is once again our big cube+
+----------------------------------------+------------------------------------+----------------------------------------+


+-----------------------------------------+-------------------------------------+
+.. figure:: /images/Influence_density.jpg|.. figure:: /images/Smoke_render.jpg +
+   :width: 200px                         |   :width: 200px                     +
+   :figwidth: 200px                      |   :figwidth: 200px                  +
+                                         |                                     +
+   Use density as influence              |   Finally your first smoke render :)+
+-----------------------------------------+-------------------------------------+


.. figure:: /images/render2.jpg
   :width: 550px
   :figwidth: 550px

   The rendered smoke. It's hard to see, but it's there.


Extending the Smoke Simulator: Fire!
====================================

You can also turn your smoke into fire with another texture! To make fire,
turn up the Emmision Value in the Materials panel.


.. figure:: /images/e.jpg
   :width: 300px
   :figwidth: 300px

   The Fire material.


Then, add another texture (Keep the old texture or the smoke won't show).
Give it a fiery color ramp- which colors based on the alpha,
and change the influence to emmision and emmision color. Change the blend to Multiply.


.. figure:: /images/f.jpg
   :width: 300px
   :figwidth: 300px

   The fire texture settings.


.. figure:: /images/render3.jpg
   :width: 640px
   :figwidth: 640px

   The fire render.



..    TODO/Review: {{review|text=
   *missing smoke groups explanation
   *some options are not explained at the end of the page}} .


Smoke Domain
************

Like the Fluid Sim, most of the settings are found when the Domain Object is selected.


Creating the Domain
===================

Before you can add smoke to your scene you need to define the area where the smoke simulation
takes place. In Blender physics this is called a domain. A good idea is to choose a cube for
that because you can scale it to the view of your camera later on. In our case we just make
the default cube bigger by hitting :kbd:`S` and dragging the mouse.


.. note:: Don't edit the domain's vertices!

   If you want a bigger domain, scale the object. Changing it in edit mode will lead to your smoke appearing more than once during rendering, like a repeating texture.


Make sure you're in object mode and go to the physics tab.
Add smoke and chose the radio button labeled 'Domain'. For now that's all,
we will return to the new settings that popped up later on.


+-----------------------------------+---------------------------------+------------------------------------+
+.. figure:: /images/Physics_tab.jpg|.. figure:: /images/Add_smoke.jpg|.. figure:: /images/Radio_domain.jpg+
+   :width: 200px                   |   :width: 200px                 |   :width: 200px                    +
+   :figwidth: 200px                |   :figwidth: 200px              |   :figwidth: 200px                 +
+                                   |                                 |                                    +
+   The physics tab might be hidden |   Add smoke                     |   Chose domain for the cube        +
+-----------------------------------+---------------------------------+------------------------------------+


.. figure:: /images/2011-06-27_1605.jpg
   :width: 400px
   :figwidth: 400px

   The Smoke Domain Object


Generic options
===============

Resolution
   How detailed the smoke is. A resolution of 32 will bake in a few seconds, while a resolution of 100 can take up to a half hour on most PC's.
Time Scale
   Affects how fast the simulation plays.

Border Collisions
   Vertically Open
      Smoke disappears when it collides with the top and bottom of the domain.
   Open
      Smoke disappears when it crosses the boundaries of the domain object.
   Collide All
      Domain Boundaries are treated as collision objects, the smoke will collide and stay inside.

Temperature and Density
   How much Density and Temperature affect smoke motion. Higher Values make faster-rising smoke.
Vorticity
   Affects how turbulence/rotation, or swirly the smoke is.

Dissolve
   Allow the smoke to dissipate over time.
Time
   The speed of the smoke's dissipation.
Slow
   Use 1/Time instead of Time, making the smoke dissolve slower.


Smoke Groups options
====================

..    TODO/Review: {{WikiTask/Todo}} .


Smoke High Resolution options
=============================

The High Resolution option lets you simulate at low resolution and then uses noise techniques
to enhance the resolution without actually computing it. This allows animators to set up a low
resolution simulation quickly and later add details without changing the overall fluid motion.

Various methods for this are available, including the default: Wavelet, which is an
implementation of '[http://graphics.ethz.ch/research/physics/wavelet turb.php|Wavelet
Turbulence for Fluid Simulation]'

Resolution/Divisions
   Enhance the resolution of smoke by this factor using noise.
Smooth Emitter
   Smoothens emitted smoke to avoid blockiness.
Show High Resolution
   Show high resolution using amplification.

Noise Method
   :guilabel:`Wavelet`

   :guilabel:`FFT`

Strength
   Strength of noise.


Smoke Field Weights options
===========================

Determines how much various forces and force fields affect the smoke.

Gravity
   How much the smoke is affected by Gravity.
All
   Changes the overall influence of all force fields.

The other settings determine how much various Force Fields affect the smoke.


.. figure:: /images/2011-06-27_1623.jpg
   :width: 550px
   :figwidth: 550px

   Smoke with a wind force field.




Particle Physics
================


.. figure:: /images/Physic_types.jpg

   Image 1: Physics types.


The movement of particles may be controlled in a multitude of ways.
With particles physics: there are five different systems:


+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+None                                                  |It doesn't give the particles any motion, which makes them belong to no physics system.                                                                                     +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Newtonian <physics/particles/physics/newtonian>`|Movement according to physical laws.                                                                                                                                        +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Keyed <physics/particles/physics/keyed>`        |Dynamic or static particles where the (animated) targets are other particle systems.                                                                                        +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Boids <physics/particles/physics/boids>`        |Particles with limited artificial intelligence, including behavior and rules programming, ideal for flocks of birds or schools of fishes, or predators vs preys simulations.+
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Fluid <physics/particles/physics/fluid>`        |Movement according to fluid laws (based on Smoothed Particle Hydrodynamics technique).                                                                                      +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Additional ways of moving particles:

- By softbody animation (only for Hair particle systems).
- By forcefields and along curves.
- By lattices.

Here we will discuss only the particle physics in the narrower sense, i.e.
the settings in the Physics panel.


Velocity
========


.. figure:: /images/Initial_velocity.jpg

   Image 3: Initial velocity.


The initial velocity of particles can be set through different parameters,
based on the type of the particle system (see Particle System tab).
If the particle system type is Emitter or Hair,
then the following parameters give the particle an initial velocity in the direction of…


Emitter Geometry
----------------

:guilabel:`Normal`
   The emitter's surface normals (i.e. let the surface normal give the particle a starting speed).
:guilabel:`Tangent`
   Let the tangent speed give the particle a starting speed.
:guilabel:`Rot`
   Rotates the surface tangent.


Emitter Object
--------------

:guilabel:`Align X,Y,Z`
   Give an initial velocity in the X, Y, and Z axes.
:guilabel:`Object`
   The emitter objects movement (i.e. let the object give the particle a starting speed).
:guilabel:`Random`
   Gives the starting speed a random variation. You can use a texture to only change the value, see Controlling Emission, Interaction and Time).


Rotation
========


.. figure:: /images/Rotation.jpg

   Image 4: Particles rotation.


These parameters specify how the individual particles are rotated during their travel. To
visualize the rotation of a particle you should choose visualization type Axis in the
Visualization panel and increase the Draw Size.

:guilabel:`Initial Rotation Mode`
    Sets the initial rotation of the particle by aligning the x-axis in the direction of:

   :guilabel:`None`
      the global x-axis.
   :guilabel:`Normal`
      Orient to the emitter's surface normal, the objects Y axis points outwards.
   :guilabel:`Normal-Tangent`
      As with normal, orient the Y axis to the surface normal.
Also orient the X axis to the tangent for control over the objects rotation about the normal. requires UV coordinates, the UV rotation effects the objects orientation, currently uses the active UV layer.
This allow deformation without the objects rotating in relation to their surface.
   :guilabel:`Velocity`
       the particle's initial velocity.
   :guilabel:`Global X/Global Y/Global Z`
       one of the global axes
   :guilabel:`Object X/Object Y/Object Z`
       one of the emitter object axes.

   :guilabel:`Random`
       Randomizes rotation.

:guilabel:`Dynamic`
    If enabled, only initializes particles to the wanted rotation and angular velocity and let's physics handle the rest. Particles then change their angular velocity if they collide with other objects (like in the real world due to friction between the colliding surfaces). Otherwise the angular velocity is predetermined at all times (i.e. set rotation to dynamic/constant).

:guilabel:`Phase`
    Initial rotation phase
:guilabel:`Random`
   Rand allows a random variation of the Phase.

:guilabel:`Angular Velocity`
    The magnitude of angular velocity, the dropdown specifies the axis of angular velocity to be
   :guilabel:`None`
       a zero vector (no rotation).
   :guilabel:`Spin`
       the particles velocity vector.
   :guilabel:`Random`
    a random vector.

If you use a Curve Guide and want the particles to follow the curve,
you have to set Angular Velocity to Spin and leave the rotation on Constant (i.e.
don't turn on Dynamic). Curve Follow does not work for particles.


Common Physics Settings
=======================

:guilabel:`Size`
   Sets the size of the particles.
:guilabel:`Random Size`
   Give the particles a random size variation.

:guilabel:`Mass`
   Specify the mass of the particles.
:guilabel:`Multiply mass with particle size`
   Causes larger particles to have larger masses.


No Physics
----------

At first a Physics type that makes the particles do nothing could seem a bit strange,
but it can be very useful at times.
None physics make the particles stick to their emitter their whole life time. The initial
velocities here are for example used to give a velocity to particles that are effected
(or affected?)
by a harmonic effector with this physics type when the effect of the effector ends.

Moreover, it can be very convenient to have particles at disposal
(whose both Unborn and Died are visible on render)
to groom vegetation and/or ecosystems using Object, Group or Billboard types of visualization.


Field Weights
=============

The Field Weight Panel allows you to control how much influence each type of external force field, or effector, has on the particle system. Force fields are external forces that give dynamic systems motion. The force fields types are detailed on the :doc:`Force Field Page <physics/force_fields>`\ .

:guilabel:`Effector Group`
   Limit effectors to a specified group. Only effectors in this group will have an effect on the current system.
:guilabel:`Gravity`
   Control how much the Global Gravity has an effect on the system.
:guilabel:`All`
   Scale all of the effector weights.


Force Fields
============

The Force Field Settings Panel allows you to make each individual act as a force field,
allowing them to affect other dynamic systems, or even, each other.

:guilabel:`Self Effect`
   Causes the particle force fields to have an effect on other particles within the same system.
:guilabel:`Amount`
   Set how many of the particles act as force fields. 0 means all of them are effectors.

You can give particle systems up to 2 force fields. By default they do not have any. Choose an effector type from the dropdowns to enable them. Settings are described on the :doc:`Force Field Page <physics/force_fields>`\ .


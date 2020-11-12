.. TODO2.8, Add: Angular Velocity: Axis changed, added options.

********
Rotation
********

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Rotation`

.. TODO2.8:
   .. figure:: /images/physics_particles_emitter_rotation_panel.png

      Particles rotation settings.

These parameters specify how the individual particles are rotated during their travel.
To visualize the rotation of a particle, display particles as *Axis*
in the :doc:`/physics/particles/emitter/display` panel.

Orientation Axis
   Sets the initial rotation of the particle by aligning the X axis in the direction of:

   None
      The global X axis.
   Normal
      Orient to the emitter's surface normal, the objects Y axis points outwards.
   Normal-Tangent
      As with normal, orient the Y axis to the surface normal.
      Also orient the X axis to the tangent for control over the objects rotation about the normal.
      requires UV coordinates, the UV rotation effects the objects orientation, currently uses the active UV map.
      This allow deformation without the objects rotating in relation to their surface.
   Velocity
      The particle's initial velocity.
   Global X, Y, Z
      One of the global axes.
   Object X, Y, Z
      One of the emitter object axes.

   Random
      Randomizes rotation.

Phase
   Initial rotation phase.
Randomize Phase
   Adds a random variation to the *Phase*.
Dynamic
   If Dynamic is enabled, only initializes particles to the chosen rotation and angular velocity and
   let the physics simulation handle the rest.
   Particles then change their angular velocity if they collide with other objects
   (like in the real world due to friction between the colliding surfaces).
   Otherwise the angular velocity is predetermined at all times (i.e. set rotation to dynamic/constant).


Angular Velocity
================

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Rotation --> Angular Velocity`

Axis
   The selector specifies the axis of angular velocity to be.

   None
      A zero vector (no rotation).
   Spin
      The particles velocity vector.
   Random
      A random vector.

   .. hint:: Curve Guide

      If you use a Curve Guide and want the particles to follow the curve,
      you have to set Angular Velocity to Spin and leave the rotation on Constant
      (i.e. do not turn on Dynamic). Curve Follow does not work for particles.

Amount
   The magnitude of angular velocity.


Collisions
==========

:doc:`Particles <physics/particles>`, :doc:`Soft Bodies <physics/soft_body>` and :doc:`Cloth objects <physics/cloth>` may collide with mesh objects. :doc:`Boids <physics/particles/physics/boids>` try to avoid :guilabel:`Collision` objects.


- The objects need to share at least one common layer to have effect.
- You may limit the effect on particles to a group of objects (in the :doc:`Field Weights panel <physics/particles/physics>`).
- *Deflection* for softbody objects is difficult, they often penetrate the colliding objects.
- :guilabel:`Hair` particles ignore deflecting objects (but you can animate them as softbodies which take deflection into account).

If you change the deflection settings for an object you have to recalculate the particle,
softbody or cloth system (:guilabel:`Free Cache`), this is not done automatically. You can
clear the cache for all selected objects with :kbd:`ctrl-B` → :guilabel:`Free cache
selected`.


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` Mode
   | Panel:    :guilabel:`Object` context → :guilabel:`Physics` sub-context → :guilabel:`Collision`


Options
=======

.. figure:: /images/Blender3D_2.58_CollisionPanel-2.49.jpg

   Image 1: Collision panel in the Physics sub-context.


:guilabel:`Permeability`
   Fraction of particles passing through the mesh. Can be animated with :guilabel:`Object` Ipos, :guilabel:`Perm` channel.

:guilabel:`Stickiness`
   How much particles stick to the object.

:guilabel:`Kill Particles`
   Deletes Particles upon impact.

:guilabel:`Damping Factor`
   Damping during a collision (independent of the velocity of the particles).
:guilabel:`Random` damping
   Random variation of damping.

:guilabel:`Friction Factor`
   Friction during movements along the surface.
:guilabel:`Random` friction
   Random variation of friction.


.. figure:: /images/Blender3D_VertexPlaneCollision.gif

   Image 1b: A softbody vertex colliding with a plane.


Soft Body and Cloth Interaction
-------------------------------

:guilabel:`Outer`
   Size of the outer collision zone.
:guilabel:`Inner`
   Size of the inner collision zone (padding distance).

Outside and inside is defined by the face normal, depicted as blue arrow in (*Image 1b*).

:guilabel:`Damping Factor`
   Damping during a collision.

*Softbody* collisions are difficult to get perfect. If one of the objects move too fast,
the soft body will penetrate the mesh. See also the section about :doc:`Soft Bodies <physics/soft_body>`.



Force Field Interaction
-----------------------

:guilabel:`Absorption`
   A deflector can also deflect effectors. You can specify some collision/deflector objects which deflect a specific
   portion of the effector force using the :guilabel:`Absorption` value. 100% absorption results in no force getting
   through the collision/deflector object at all. If you have 3 collision object behind each other with e.g.
   10%, 43% and 3%, the absorption ends up at around 50% (``100×(1-0.1)×(1-0.43)×(1-0.03)``).


Examples
--------

.. figure:: /images/UM_PART_XIII_KST_PI10.jpg

   Image 2: Deflected Particles.


Here is a :guilabel:`Meta` object, dupliverted to a particle system emitting downwards,
and deflected by a mesh cube:


Hints
-----

- Make sure that the normals of the mesh surface are facing towards the particles/points for correct deflection.
- :guilabel:`Hair` particles react directly to force fields, so if you use a force field with a short range you don't need necessarily collision.
- :guilabel:`Hair` particles avoid their emitting mesh if you edit them in :guilabel:`Particle` mode. So you can at least model the hair with collision.



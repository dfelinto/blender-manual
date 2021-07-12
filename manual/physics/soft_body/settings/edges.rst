.. _physics-softbody-settings-edges:

*****
Edges
*****

.. reference::

   :Panel:     :menuselection:`Physics --> Soft Body --> Edges`

Allow the edges in a mesh object to act like springs.
See :doc:`interior forces </physics/soft_body/forces/interior>`.

Springs
   Use a specified vertex group for spring strength values.

Pull
   The spring stiffness for edges (how much the edges are allowed to stretch).
   A low value means very weak springs (a very elastic material),
   a high value is a strong spring (a stiffer material) that resists being pulled apart.

   A value of 0.5 is latex, 0.9 is like a sweater, 0.999 is a highly-starched napkin or leather.
   The soft body simulation tends to get unstable if you use a value of 0.999,
   so you should lower this value a bit if that happens.

Push
   How much the soft body resists being scrunched together, like a compression spring.
   Low values for fabric, high values for inflated objects and stiff material.

Damp
   The friction for edge springs. High values (max of 50) dampen the *Push*/*Pull* effect and calm down the cloth.

Plasticity
   Permanent deformation of the object after a collision.
   The vertices take a new position without applying the modifier.

Bending
   This option creates virtual connections between a vertex and the vertices connected to its neighbors.
   This includes diagonal edges. Damping also applies to these connections.

Length
   The edges can shrink or be blown up. This value is given in percent,
   0 disables this function. 100% means no change, the body keeps 100% of its size.

Collision Edge
   Checks for edges of the soft body mesh colliding.

Face
   Checks for any portion of the face of the soft body mesh colliding (which is computationally intensive).
   While *Face* enabled can solve collision errors, there does not seem to be any dampening settings for it.
   So parts of the soft body object near a collision mesh tend to "jitter" as they bounce off and fall back,
   even when there is no motion of any meshes. Edge collision has dampening, so that can be controlled,
   but Deflection dampening value on a collision object does not seem to affect the face collision.


.. _physics-softbody-settings-aerodynamics:

Aerodynamics
============

Force from surrounding media.
See :ref:`exterior forces <physics-softbody-forces-exterior-aerodynamics>` for details.

Type
   Simple
      Edges receive a drag force from the surrounding media.
   Lift Force
      Edges receive a lift force when passing through the surrounding media.
Factor
   How much aerodynamic force to use. Try a value of 30 at first.


Stiffness
=========

For quad faces, the diagonal edges are used as springs.
This stops quad faces to collapse completely on collisions (what they would do otherwise).

Shear
   Stiffness of the virtual springs created for quad faces.

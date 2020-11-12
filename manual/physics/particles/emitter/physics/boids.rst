.. _bpy.types.Boid:
.. _bpy.ops.boid:

*****
Boids
*****

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Physics`
   :Type:      Boids

.. TODO2.8:
   .. figure:: /images/physics_particles_emitter_physics_boids_panel.png

      Boid Physics settings.

Boids particle systems are controlled by a limited artificial intelligence,
which can be programmed to follow basic rules and behaviors.
They are ideal for simulating flocks, swarms, herds and schools of various kind of animals,
insects and fishes or predators vs. preys simulations.
They can react on the presence of other objects and on the members of their own system.
Boids can handle only a certain amount of information,
therefore the sequence of the *Boid Brain* rules is very important.
In certain situations only the first three parameter are evaluated.


Movement
========

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Physics --> Movement`

Boids try to avoid objects with activated Collision.
They try to reach goal objects, and fly from "predators" according to the *Boid Brain* settings.

Boids can different physics depending on whether they are in the air,
or on land (on collision object).

Allow Flight
   Allow boids to move in the air.
Allow Land
   Allow boids to move on land.
Allow Climbing
   Allow boids to climb goal objects.

Max Air Speed
   Set the Maximum velocity in the air.
Min Air Speed
   Set the Minimum velocity in the air.
Max Air Acceleration
   Lateral acceleration in air, percentage of the max velocity (turn).
   Defines how fast a boid is able to change direction.
Max Air Angular Velocity
   Tangential acceleration in air, percent 180 degrees.
   Defines how much the boid can suddenly accelerate in order to fulfill a rule.
Air Personal Space
   Radius of boids personal space in air. Percentage of particle size.
Landing Smoothness
   How smoothly the boids land.

Max Land Speed
   Set the Maximum velocity on land.
Jump Speed
   Maximum speed for jumping.
Max Land Acceleration
   Lateral acceleration on land, percent of max velocity (turn). Defines how fast a boid is able to change direction.
Max Land Angular Velocity
   Tangential acceleration on land, percent 180 degrees.
   Defines how much the boid can suddenly accelerate in order to fulfill a rule.
Land Personal Space
   Radius of boids personal space on land. Percentage of particle size.
Land Stick Force
   How strong a force must be to start effecting a boid on land.

Collision Collection
   Only collide with objects in this collection.


Battle
======

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Physics --> Battle`

Health
   Initial boid health when born.
Strength
   Maximum caused damage per second on attack.
Aggression
   Boid will fight this time stronger than enemy.
Accuracy
   Accuracy of attack.
Range
   Maximum distance of which a boid can attack.


Misc
====

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Physics --> Misc`

Banking
   Amount of rotation around velocity vector on turns. Banking of 1.0 gives a natural banking effect.
Pitch
   Amount of rotation around side vector.
Height
   Boid height relative to particle size.


Relations
=========

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Physics --> Relations`

Target
   This :ref:`list view <ui-list-view>` allows you to set up other particle systems to react with the boids.
Target Object
   A :ref:`data ID <ui-data-id>` to select an object with a particle system set on.
System
   Index of the *Object*\ 's particle system as set in the list view in the particle panel.

Mode
   Enemy
      Setting the type to *Enemy* will cause the systems to fight with each other.
   Friend
      Will make the systems work together.
   Neutral
      Will not cause them to align or fight with each other.


Deflection
----------

Boids will try to avoid deflector objects according to the Collision rule's weight.
It works best for convex surfaces (some work needed for concave surfaces).


Force Fields
------------

As other physics types, Boids is also influenced by external force fields.

In addition, special *Boid* force fields can be used with the Boids physics.
These effectors could be predators (positive Strength) that boids try to avoid,
or targets (negative Strength) that boids try to reach
according to the (respectively) *Avoid* and *Goal* rules of the *Boid Brain*.


Boid Brain
==========

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Particle System --> Physics --> Boid Brain`

The Boid Brain panel controls how the boids particles will react with each other.
The boids' behavior is controlled by a list of rules.
Only a certain amount of information in the list can be evaluated.
If the memory capacity is exceeded, the remaining rules are ignored.

The rules are by default parsed from top-list to bottom-list
(thus giving explicit priorities),
and the order can be modified using the little arrows buttons on the right side.

Rule Evaluation
   There are three ways to control how rules are evaluated:

   Average
      All rules are averaged.
   Random
      A random rule is selected for each boid.
   Fuzzy
      Uses fuzzy logic to evaluate rules. Rules are gone through top to bottom.
      Only the first rule that affect above the *Rule Fuzziness* threshold is evaluated.
      The value should be considered how hard the boid will try to respect a given rule
      (a value of 1 means the Boid will always stick to it, a value of 0 means it will never).
      If the boid meets more than one conflicting condition at the same time,
      it will try to fulfill all the rules according to the respective weight of each.

   .. note::

      A given boid will try as much as it can to comply to each of the rules it is given,
      but it is more than likely that some rule will take precedence on other in some cases.
      For example, in order to avoid a predator, a boid could probably "forget" about Collision,
      Separate and Flock rules, meaning that "while panicked" it could well run into obstacles,
      e.g. even if instructed not to, most of the time.

In Air
   The current rule affects boids while they are flying.
On Land
   The current rule affects boids while they are not flying.


Goal Rule
---------

Seek goal.

Object
   Specifies the goal object. If not specified, Boid force fields with negative Strength are used as goals.
Predict
   Predict target's movements.


Avoid Rule
----------

Avoid "predators".

Object
   Specifies the object to avoid.
   If not specified, Boid force fields with positive Strength are used as predators.
Predict
   Predict target's movements.
Fear Factor
   Avoid object if danger from it is above this threshold.


Avoid Collision Rule
--------------------

Avoid objects with activated Deflection.

Boids
   Avoid collision with other boids.
Deflectors
   Avoid collision with deflector objects.
Look Ahead
   Time to look ahead in seconds.


Separate Rule
-------------

Boids move away from each other.


Flock Rule
----------

Copy movements of neighboring boids, but avoid each other.


Follow Leader Rule
------------------

Follows a leader object instead of a boid.

Distance
   Distance behind leader to follow.
Line
   Follow the leader in a line.

   Queue Size
      How many boids that are allowed to follow in a line.


Average Speed Rule
------------------

Maintain average velocity.

Speed
   Percentage of maximum speed.
Wander
   How fast velocity's direction is randomized.
Level
   How much velocity's Z component is kept constant.


Fight Rule
----------

Move toward nearby boids.

Fight Distance
   Attack boids at a maximum of this distance.
Flee Distance
   Flee to this distance.

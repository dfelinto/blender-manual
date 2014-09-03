
Boids
*****

.. figure:: /images/Boids.jpg

   Image 7: Boid Physics.


Boids particle systems can be set to follow basic rules and behaviors.
They are useful for simulating flocks, swarms, herds and schools of various kind of animals,
insects and fishes.
They can react on the presence of other objects and on the members of their own system.
Boids can handle only a certain amount of information,
therefore the sequence of the Behaviour settings is very important.
In certain situations only the first three parameter are evaluated.

To view the subpanel to the right, add a :guilabel:`Particle System` of type
:guilabel:`Emitter` and look in the middle area of the :guilabel:`Particle System` tab.


Physics
*******

Boids try to avoid objects with activated Deflection.
They try to reach objects with positive Spherical fields,
and fly from objects with negative Spherical fields.
The objects have to share one common layer to have effect.
It is not necessary to render this common layer, so you may use invisible influences.

Boids can different physics depending on whether they are in the air,
or on land (on collision object)

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
   Lateral acceleration in air, percent of max velocity (turn). Defines how fast a boid is able to change direction.
Max Air Angular Velocity
   Tangential acceleration in air, percent 180 degrees. Defines how much the boid can suddenly accelerate in order to fulfill a rule.
Air Personal Space
   Radius of boids personal space in air. Percentage of particle size.
Landing Smoothness
   How smoothly the boids land.

Max Land Speed
   Set the Maximum velocity on land.
Jump Speed
   Maximum speed for jumping
Max Land Acceleration
   Lateral acceleration on land, percent of max velocity (turn). Defines how fast a boid is able to change direction.
Max Land Angular Velocity
   Tangential acceleration on land, percent 180 degrees. Defines how much the boid can suddenly accelerate in order to fulfill a rule.
Land Personal Space
   Radius of boids personal space on land. Percentage of particle size.
Land Stick Force
   How strong a force must be to start effecting a boid on land.

Banking
   Amount of rotation around velocity vector on turns. Banking of (1.0 == natural banking).
Pitch
   Amount of rotation around side vector.
Height
   Boid height relative to particle size.


Battle
======

Health
   Initial boid health when born.
Strength
   Maximum caused damage per second on attack.
Aggression
   Boid will fight this times stronger than enemy.
Accuracy
   Accuracy of attack.
Range
   Maximum distance of which a boid can attack.


Alliance
========

The relations box allows you to set up other particle systems to react with the boids.
Setting the type to :guilabel:`Enemy` will cause the systems to fight with each other.
:guilabel:`Friend` will make the systems work together.
:guilabel:`Neutral` will not cause them to align or fight with each other.


Deflectors and Effectors
========================

As mentioned before, very much like Newtonian particles,
Boids will react to the surrounding deflectors and fields,
according to the needs of the animator:

Deflection:
Boids will try to avoid deflector objects according to the Collision rule's weight.
It works best for convex surfaces (some work needed for concave surfaces).
For boid physics,
Spherical fields define the way the objects having the field are seen by others.
So a negative Spherical field (on an object or a particle system)
will be a predator to all other boids particle systems,
and a positive field will be a goal to all other boids particle systems.

When you select an object with a particle system set on, you have in the Fields tab a little
menu stating if the field should apply to the emitter object or to the particle system. You
have to select the particle system name if you want prey particles to flew away from predator
particles.

Spherical fields: These effectors could be predators (negative Strength)
that boids try to avoid or targets (positive Strength)
that boids try to reach according to the (respectively) Avoid and Goal rules' weights.
Spherical's effective Strength is multiplied by the actual relevant weight (e.g.
if either Strength or Goal is null,
then a flock of boids won't track a positive Spherical field).
You can also activate Die on hit (Extras panel) so that a prey particle simply disappears when
"attacked" by a predator particle which reaches it. To make this work,
the predator particles have to have a spherical field with negative force,
it is not sufficient just to set a positive goal for the prey particles
(but you may set the predators force strength to -0.01).
The size of the predators and the prey can be set with the Size button in the Extras panel.


Boid Brain
==========

The Boid Brain panel controls how the boids particles will react with each other.
The boids' behavior is controlled by a list of rules.
Only a certain amount of information in the list can be evaluated.
If the memory capacity is exceeded, the remaining rules are ignored.

The rules are by default parsed from top-list to bottom-list
(thus giving explicit priorities),
and the \order can be modified using the little arrows buttons on the right side.

The list of rules available are:

Goal
   Seek goal (objects with Spherical fields and positive Strength)

   Predict
      Predict target's movements

Avoid
   Avoid "predators" (objects with Spherical fields and negative Strength)

   Predict
      Predict target's movements
   Fear Factor
      Avoid object if danger from it is above this threshold

Avoid Collision
   Avoid objects with activated Deflection

   Boids
      Avoid collision with other boids
   Deflectors
      Avoid collision with deflector objects
   Look Ahead
      Time to look ahead in seconds

Separate
   Boids move away from each other

Flock
   Copy movements of neighboring boids, but avoid each other

Follow Leader
   Follows a leader object instead of a boid

   Distance
      Distance behind leader to follow
   Line
      Follow the leader in a line

Average Speed
   Maintain average velocity.

   Speed
      Percentage of maximum speed
   Wander
      How fast velocity's direction is randomized
   Level
      How much velocity's Z component is kept constant

Fight
   Move toward nearby boids

   Fight Distance
      Attack boids at a maximum of this distance
   Flee Distance
      Flee to this distance


Rule Evaluation
---------------

There are three ways control how rules are evaluated.

Average
   All rules are averaged.
Random
   A random rule is selected for each boid.
Fuzzy
   Uses fuzzy logic to evaluate rules. Rules are gone through top to bottom.
   Only the first rule that effect above fuzziness threshold is evaluated.
   The value should be considered how hard the boid will try to respect a given rule
   (a value of 1.000 means the Boid will always stick to it, a value of 0.000 means it will never).
   If the boid meets more than one conflicting condition at the same time,
   it will try to fulfill all the rules according to the respective weight of each.

Please note that a given boid will try as much as it can to comply to each of the rules he is
given, but it is more than likely that some rule will take precedence on other in some cases.
For example, in order to avoid a predator, a boid could probably "forget" about Collision,
Crowd and Center rules, meaning that "while panicked" it could well run into obstacles,
for example, even if instructed not to, most of the time.

As a final note, the Collision algorithm is still not perfect and in research progress,
so you can expect wrong behaviors at some occasion. It is worked on.



Exterior Forces
===============

Exterior forces are applied to the vertices (and nearly exclusively to the vertices)
of Soft Body objects. This is done using Newtons Laws of Physics:

- If there is no force on a vertex, it stays either unmoved or moves with constant speed in a straight line.
- The acceleration of a vertex depends on its mass and the force. The heavier the mass of a vertex the slower the acceleration. The larger the force the greater the acceleration.
- For every action there is an equal and opposite reaction.

Well, this is done only in the range of computing accurateness,
there is always a little damping to avoid overshoot of the calculation.


Example
-------

We will begin with a very simple example - the default cube.

- To judge the effect of the external forces you should at first turn off the :guilabel:`Goal`, so that the vertices are not retracted to their original position.
- Press :kbd:`alt-A`.

What happens? The cube moves in negative Z-direction.
Each of it's eight vertices is affected by a global, constant force - the gravitation.
Gravitation without friction is independent from the weight of an object,
so each object you would use as a Soft Body here would fall with the same acceleration.
The object does not deform,
because every vertex moves with the same speed in the same direction.


Settings
========

Soft Body Panel
---------------

:guilabel:`Friction`
   The friction of the surrounding medium. The larger the friction, the more viscous is the medium. Friction always appears when a vertex moves relative to it's surround medium.

:guilabel:`Mass`
   Mass value for vertices. Larger mass slows down acceleration, except for gravity where the motion is constant regardless of mass. Larger mass means larger inertia, so also braking a Soft Body is more difficult.

:guilabel:`Mass Vertex Group`
   You can paint weight values for an mesh's mass, and select that vertex group here.

:guilabel:`Speed`
   You can control the internal timing of the Softbody system with this value. It sets the correlation between frame rate and tempo of the simulation. A free falling body should cover a distance of about five meters after one second. You can adjust the scale of your scene and your simulation with this correlation. If you render with 25 frames per second and 1 meter shall be 1 BU, you have to set :guilabel:`Speed` to 1.3.


Force Fields
------------

To create other forces you have to use another object,
often :guilabel:`Empty` objects are used for that.
You can use some of the forces on Soft Body vertices as on :guilabel:`Particles`.
Soft Bodies react only to:

- :guilabel:`Spherical`
- :guilabel:`Wind`
- :guilabel:`Vortex`

Soft bodies do react on :guilabel:`Harmonic` fields, but not in a useful way.
So if you use a :guilabel:`Harmonic` field for particles move the Soft body to another layer.

See the section :doc:`Force Fields <physics/force_fields>` for details. The force fields are quite strong, a :guilabel:`Spherical` field with a strength of -1.0 has the same effect that gravity has - approximately - a force of 10 Newton.


Aerodynamics
------------

This special exterior force is not applied to the vertices but to the connecting edges.
Technically, a force perpendicular to the edge is applied.
The force scales with the projection of the relative speed on the edge (dot product). Note
that the force is the same if wind is blowing or if you drag the edge through the air with the
same speed. That means that an edge moving in its own direction feels no force,
and an edge moving perpendicular to its own direction feels maximum force.

:guilabel:`Simple`
   Edges receive a drag force from surrounding media
:guilabel:`Lift Force`
   Edges receive a lift force when passing through surrounding media.
:guilabel:`Factor`
   How much aerodynamic force to use. Try a value of 30 at first.


Using a Goal
------------

A goal is a shape that a soft body object tries to conform to.

You have to confine the movement of vertices in certain parts of the mesh, e.g.
to attach a Soft Body object at other objects. This is done with the :guilabel:`Vertex Group`
(target). The target position is the original position of the vertex, like it would result
from the "normal" animation of an object including :guilabel:`Shape Keys`,
:guilabel:`Hooks` and :guilabel:`Armatures`.
The vertex tries to reach it's target position with a certain, adjustable intensity.


.. figure:: /images/Shockabs.gif
   :width: 300px
   :figwidth: 300px

   Image 2b: Shock absorber description.


Imagine the vertex is connected with it's target through a spring (*Image 2b*).

:guilabel:`Default`
   This parameter defines how strong the influence of this spring is. A strength of 1 means,
   that the vertex will not move as Soft Body at all, instead keep its original position. 0 :guilabel:`Goal`
   (or no :guilabel:`Goal`) means, that the vertex moves only according to Soft Body simulation.
   If no vertex group is used/assigned, this numeric field is the default goal weight for all vertices.
   If a vertex group is present and assigned,
   this button instead shows an popup selector button that allows you to choose the name of the goal vertex group.
   If you use a vertex group the weight of a vertex defines its goal.

   Often :doc:`weight painting <modeling/meshes/weight_paint>` is used to adjust the weight comfortably.
   For non-mesh objects the :guilabel:`Weight` parameter of their vertices/controlpoints is used instead
   (:kbd:`W` in :guilabel:`Edit mode`, or use the :guilabel:`Transform Properties` panel).
   The weight of :guilabel:`Hair` particles can also be painted in :doc:`Particle Mode <physics/particles/mode>`.


:guilabel:`Minimum` / :guilabel:`Maximum`
   When you paint the values in vertex-groups (using :guilabel:`WeightPaint` mode), you can use the :guilabel:`G Min` and :guilabel:`G Max` to fine-tune (clamp) the weight values. The lowest vertex-weight (blue) will become :guilabel:`G Min`, the highest value (red) becomes :guilabel:`G Max` (please note that the blue-red color scale may be altered by User Preferences).


.. admonition:: For now all is applied to single vertices
   :class: nicetip

   For now we have discussed vertex movement independent of each other, similar to particles. Every object without :guilabel:`Goal` would collapse completely if a non uniform force is applied. Now we will move to the next step, the forces that keep the structure of the object and make the Soft Body to a real Body.


:guilabel:`Stiffness`
   The spring stiffness for Goal. A low value creates very weak springs (more flexible "attachment" to the goal), a high value creates a strong spring (a stiffer "attachment" to the goal).

:guilabel:`Dampimg`
   The friction of the spring. With a high value the movement will soon come to an end (little jiggle).



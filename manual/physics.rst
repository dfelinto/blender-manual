
Introduction to Physics Simulation
**********************************

This chapter covers various advanced Blender effects,
often used to simulate real physical phenomena, such as:


- Smoke
- Rain
- Dust
- Cloth
- Water
- Jello

:doc:`Particle Systems </physics/particles>` can be used to simulate many things: hair, grass, smoke, flocks.

:doc:`Hair </physics/particles/hair>` is a subset of the particle system, and can be used for strand-like objects, such as hair, fur, grass, quills, etc.

:doc:`Soft Bodies </physics/soft_body>` are useful for everything that tends to bend, deform, in reaction to forces like gravity or wind, or when colliding with other objects... It can be used for skin, rubber, and even clothes, even though there is separate :doc:`Cloth Simulation </physics/cloth>` specific for cloth-like objects.

:doc:`Rigid Bodies </physics/rigid_body>` can simulate dynamic objects that are fairly rigid.

:doc:`Fluids </physics/fluid>`, which include liquids and gasses, can be simulated, including :doc:`Smoke </physics/smoke>`.

:doc:`Force Fields </physics/force_fields>` can modify the behavior of simulations.


Gravity
=======

Gravity is a global setting that is applied the same to all physics systems in a scene,
which can be found in the scene tab. This value is generally fine left at its default value,
at -9.810 in the Z axis, which is the force of gravity in the real world.
Lowering this value would simulate a lower or higher force of gravity. Gravity denoted g,
measurement [m×s\ :sup:`-2` ]).

Gravity is practically same around whole **Earth**.
South and North poles have g = 9.832 m×s\ :sup:`-2`, on the equator g = 9.
780 m×s\ :sup:`-2`.
For detail computing of falling in :guilabel:`Prague` or :guilabel:`Boston` use 9.81373.
For rendering scenes from **Moon** use value 6 times smaller, e.g. 1.622 m×s\ :sup:`-2`.
The most popular and probably not colonized **Mars** has g = 3.69.


Note that you can scale down the gravity value per physics system in the :guilabel:`Field
Weights tab.`


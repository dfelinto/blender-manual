
Fluid Physics
*************

.. figure:: /images/Fluid.jpg

   Image 8: Fluid Physics.


Fluid simulations are widely used in CG, and a very desired feature of any particle system,
fluid particles are similar to newtonian ones but this time particles are influenced by
internal forces like pressure, surface tension, viscosity, springs, etc.
Blender particle fluids use the SPH techniques to solve the particles fluid equations.

Smoothed-particle hydrodynamics (SPH)
is a computational method used for simulating fluid flows.
It has been used in many fields of research, including astrophysics, ballistics, vulcanology,
and oceanography. It is a mesh-free Lagrangian method
(where the co-ordinates move with the fluid), and the resolution of the method can easily be
adjusted with respect to variables such as the density.

From liquids to slime, goo to sand and wispy smoke the possibilities are endless.


Settings
********

Fluid physics share options with :doc:`Newtonian Physics </physics/particles/physics/newtonian>`. These are covered on that page.


Fluid Properties
================

Stiffness
   How incompressible the fluid is.
Viscosity
   Linear viscosity. Use lower viscosity for thicker fluids.
Buoyancy
   Artificial buoyancy force in negative gravity direction based on pressure differences inside the fluid.


Advanced
========

Repulsion Factor
   How strongly the fluid tries to keep from clustering (factor of stiffness). Check box sets repulsion as a factor of stiffness.
Stiff Viscosity
   Creates viscosity for expanding fluid. Check box sets this to be a factor of normal viscosity.
Interaction Radius
   Fluid's interaction radius. Check box sets this to be a factor of 4*particle size.
Rest Density
   Density of fluid when at rest. Check box sets this to be a factor of default density.


Springs
=======

Force
   Spring force
Rest Length
   Rest length of springs. Factor of particle radius. Check box sets this to be a factor of 2*particle size.

Viscoelastic Springs
   Use viscoelastic springs instead of Hooke's springs.
Elastic Limit
   How much the spring has to be stretched/compressed in order to change its rest length
Plasticity
   How much the spring rest length can change after the elastic limit is crossed.
Initial Rest Length
   Use initial length as spring rest length instead of 2*particle size.
Frames
   Create springs for this number of frames since particle's birth (0 is always).


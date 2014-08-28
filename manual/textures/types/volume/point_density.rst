
..    TODO/Review: {{review|partial=X|im=examples}} .


Point Density Texture
*********************

Point density renders a given point cloud (object vertices or particle system) as a 3D volume,
using a user-defined radius for the points. Internally,
the system uses a BVH data structure for fast range lookups.

The rendered points are spherical by default, with various smooth falloff options,
as well as simple Turbulence options for displacing the result with noise, adding fine detail.
When using Point Density with a particle system,
additional particle info such as particle velocity, age, and speed,
can be visualized using a color/alpha ramp gradient.


Options
=======

:guilabel:`Particle System`
   Particle System, Generate point density from a particle system.

:guilabel:`Object Vertices`
   Object Vertices, Generate point density from an object's vertices.

:guilabel:`Object`
:guilabel:`Radius`
:guilabel:`System`
:guilabel:`Falloff`

   :guilabel:`Standard`
   :guilabel:`Smooth`
   :guilabel:`Soft`
   :guilabel:`Softness`

   :guilabel:`Constant`
      Density is constant within lookup radius.

   :guilabel:`Root`
   :guilabel:`Particle Age`
   :guilabel:`Particle Velocity`
   :guilabel:`Velocity Scale`


:guilabel:`Falloff Curve`
   Use a custom falloff

:guilabel:`Cache`
   Coordinate system to cache particles in
   :guilabel:`Global Space`
   :guilabel:`Emit Object Space`
   :guilabel:`Emit Object Location`

:guilabel:`Color Source`
   Data to derive the color results from

   :guilabel:`Constant`
      Constant color
   :guilabel:`Particle Age`
      Lifetime mapped as 0.0 - 1.0 intensity.
   :guilabel:`Particle Speed`
      Particle speed (absolute magnitude of velocity) mapped as 0.0-1.0 intensity.

      :guilabel:`Scale`
         Multiplier to bring particle speed within an acceptable range.
   :guilabel:`Particle Velocity`
      XYZ velocity mapped to RGB colors.

      :guilabel:`Scale`
         Multiplier to bring particle speed within an acceptable range.


Turbulence
----------

Adds directed noise to the density at render time

:guilabel:`Influence`
   Method for driving added turbulent noise

   :guilabel:`Static`
      Noise patterns will remain unchanged, faster and suitable for stills.
   :guilabel:`Particle Velocity`
      Turbulent noise driven by particle velocity.
   :guilabel:`Particle Age`
      Turbulent noise driven by the particle's age between birth and death.
   :guilabel:`Global Time`
      Turbulent noise driven by the global current frame.

:guilabel:`Noise Basis`
   See :doc:`Here </textures/types/procedural>`

:guilabel:`Size`
   Scale of the turbulent noise
:guilabel:`Depth`
   Level of detail in the added turbulent noise
:guilabel:`Turbulence Strength`
   Strength of the added turbulent noise



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

Particle System
   Particle System, Generate point density from a particle system.

Object Vertices
   Object Vertices, Generate point density from an object's vertices.

Object
Radius
System
Falloff

   Standard
   Smooth
   Soft
   Softness

   Constant
      Density is constant within lookup radius.

   Root
   Particle Age
   Particle Velocity
   Velocity Scale


Falloff Curve
   Use a custom falloff

Cache
   Coordinate system to cache particles in
   Global Space
   Emit Object Space
   Emit Object Location

Color Source
   Data to derive the color results from

   Constant
      Constant color
   Particle Age
      Lifetime mapped as 0.0 - 1.0 intensity.
   Particle Speed
      Particle speed (absolute magnitude of velocity) mapped as 0.0-1.0 intensity.

      Scale
         Multiplier to bring particle speed within an acceptable range.
   Particle Velocity
      XYZ velocity mapped to RGB colors.

      Scale
         Multiplier to bring particle speed within an acceptable range.


Turbulence
----------

Adds directed noise to the density at render time

Influence
   Method for driving added turbulent noise

   Static
      Noise patterns will remain unchanged, faster and suitable for stills.
   Particle Velocity
      Turbulent noise driven by particle velocity.
   Particle Age
      Turbulent noise driven by the particle's age between birth and death.
   Global Time
      Turbulent noise driven by the global current frame.

Noise Basis
   See :doc:`Here </textures/types/procedural>`

Size
   Scale of the turbulent noise
Depth
   Level of detail in the added turbulent noise
Turbulence Strength
   Strength of the added turbulent noise


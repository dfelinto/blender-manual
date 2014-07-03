
Particle Emission
=================

The :guilabel:`Emitter` system works just like its name says: it emits/produces particles for a certain amount of time. In such a system, particles are emitted from the selected object from the :guilabel:`Start` frame to the :guilabel:`End` frame and have a certain lifespan. These particles are rendered default as :doc:`Halos <materials/halos>`\ , but you may also render these kind of particles as objects (depending on the particle system's render settings, see :doc:`Visualization <physics/particles/visualization>`\ ).


Options
=======


.. figure:: /images/Blender3D_ParticleSystem_EmissionSettings-2.5.jpg

   Image 2a: Settings for particle Emission.


The buttons in the :guilabel:`Emission` panel control the way particles are emitted over time:
:guilabel:`Amount`
   The maximum amount of parent particles used in the simulation.
:guilabel:`Start`
   The start frame of particle emission. You may set negative values, which enables you to start the simulation before the actual rendering.
:guilabel:`End`
   The end frame of particle emission.
:guilabel:`Lifetime`
   The lifetime (in frames) of the particles.
:guilabel:`Random`
   A random variation of the lifetime of a given particle. The shortest possible lifetime is *Lifetime*\ ``×(1-``\ *Rand*\ ``)``\ . Values above 1.0 are not allowed. For example with the default :guilabel:`Lifetime` value of 50 a :guilabel:`Random` setting of 0.5 will give you particles with lives ranging from 50 frames to ``50×(1.0-0.5)``\ =25 frames, and with a :guilabel:`Random` setting of 0.75 you'll get particles with lives ranging from 50 frames to ``50×(1.0-0.75)``\ =12.5 frames.


Emission Location
-----------------

:guilabel:`Emit From` parameters define how and where the particles are emitted, giving precise control over their distribution. You may use vertex groups to confine the emission, that is done in the :guilabel:`Vertexgroups` panel.

:guilabel:`Verts`
   Emit particles from the vertices of a mesh.
:guilabel:`Faces`
   Emit particles from the surface of a mesh's faces.
:guilabel:`Volume`
   Emit particles from the volume of an enclosed mesh.


Distribution Settings
---------------------

These settings control how the emissions of particles are distributed throughout the emission
locations

:guilabel:`Random`
   The emitter element indices are gone through in a random order instead of linearly (one after the other).

For Faces and Volume, additional options appear:

:guilabel:`Even Distribution`
    Particle distribution is made even based on surface area of the elements, i.e. small elements emit less particles than large elements, so that the particle density is even.

:guilabel:`Jittered`
    Particles are placed at jittered intervals on the emitter elements.

   :guilabel:`Particles/Face`
       Number of emissions per face (0 = automatic).
   :guilabel:`JitteringAmount`
       Amount of jitter applied to the sampling.

:guilabel:`Random`
    Particles are emitted from random locations in the emitter's elements.

:guilabel:`Grid`
    Particles are set in a 3d grid and particles near/in the elements are kept.

   :guilabel:`Invert Grid`
      Invert what is considered the object and what is not.
   :guilabel:`Hexagonal`
      Uses a hexagonal shaped grid instead of a rectangular one.
   :guilabel:`Resolution`
       Resolution of the grid.
   :guilabel:`Random`
      Add a random offset to grid locations.


.. admonition:: Your mesh must be watertight to emit particles from the volume.
   :class: nicetip

   Some modifiers like :guilabel:`Edge Split` break up the surface, in which case volume emission will not work correctly!



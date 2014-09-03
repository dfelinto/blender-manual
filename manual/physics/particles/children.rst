
Children
********

:guilabel:`Children` are :guilabel:`Hair` and :guilabel:`Keyed` particles assigned subparticles. They make it possible to work primarily with a relatively low amount of Parent particles, for whom the physics are calculated. The children are then aligned to their parents. Without recalculating the physics the number and visualization of the children can be changed.

- Children can be emitted from particles or from faces (with some different options). Emission from :guilabel:`Faces` has some advantages, especially the distribution is more even on each face (which makes it better suitable for fur and the like). However, children from particles follow their parents better, e.g. if you have a softbody animation and don't want the hair to penetrate the emitting mesh. But see also our manual page about :doc:`Hair </physics/particles/hair>`.
- If you turn on children the parents are no longer rendered (which makes sense because the shape of the children may be quite different from that of their parents). If you want to see the parents additionally turn on the :guilabel:`Parents` button in the :guilabel:`Visualization` panel.
- Children carry the same material as their parents and are colored according to the exact place from where they are emitted (so all children may have different color or other attributes).

The possible options depend from the type of particle system,
and if you work with *Children from faces* or *Children from particles*.
We don't show every possible combination,
only the settings for a :guilabel:`Hair` particle system.


Settings
********

Simple
   Children are emitted from the parent hairs.
Interpolated
   Children are emitted between the *Parent* particles on the faces of a mesh. They interpolate between adjacent parents. This is especially useful for fur, because you can achieve an even distribution. Some of the children can become virtual parents, which are influencing other particles nearby.

Display
   The number of children in the 3D window.
Render
   The number of children to be rendered (up to 10.000).

For Simple Mode
   Size
      Only for :guilabel:`Emitter`. A multiplier for children size.
   Random
      Random variation to the size of child particles.

Interpolated Mode
   Seed
      Offset the random number table for child particles, to get a different result.
   Virtual
      Relative amount of virtual parents.
   Long Hair
      Calculate children that suit long hair well.


Effects
=======

.. figure:: /images/Blender3D_ChildParticleRoundClump.jpg

   Image 2: From left to right: Round: 0.0 / Round: 1.0 / Clump: 1.0 / Clump: -1.0 / Shape: -0.99.


Clump
   Clumping. The children may meet at their tip (1.0) or start together at their root (-1.0).
Shape
   Form of :guilabel:`Clump`. Either inverse parabolic (0.99) or exponentially (-0.99).
Length
   Length of child paths
Threshold
   Amount of particles left untouched by child path length
Radius
   The radius in which the children are distributed around their parents. This is 3D, so children may be emitted higher or lower than their parents.
Roundness
   The roundness of the children around their parents. Either in a sphere (1.0) or in-plane (0.0).
Seed
   Offset in the random number table for child particles, to get a different randomized result


Roughness
=========

Uniform,\ Size
   It is based on children location so it varies the paths in a similar way when the children are near.
Endpoint,\ Shape
   "Rough End" randomizes path ends (a bit like random negative clumping). Shape may be varied from <1 (parabolic) to 10.0 (hyperbolic).
Random,\ Size,\ Threshold
   It is based on a random vector so it's not the same for nearby children. The threshold can be specified to apply this to only a part of children. This is useful for creating a few stray children that won't do what others do.


Kink
====


.. figure:: /images/Blender3D_ChildParticleKink.jpg

   Image 3: Child particles with Kink. From left to right: Curl / Radial / Wave / Braid / Roll.


With :guilabel:`Kink` you can rotate the children around the parent. See above picture
(*Image 3*) for the different types of :guilabel:`Kink`.

Curl
   Children grow in a spiral around the parent hairs.
Radial
   Children form around the parent a wave shape that passes through the parent hair.
Wave
   Children form a wave, all in the same direction.
Braid
   Children braid themselves around the parent hair.

Amplitude
   The amplitude of the offset.
Clump
   How much clump effects kink amplitude.
Flatness
   How flat the hairs are.

Frequency
   The frequency of the offset (1/total length). The higher the frequency the more rotations are done.
Shape
   Where the rotation starts (offset of rotation).


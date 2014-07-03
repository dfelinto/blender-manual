..    TODO/Review: {{review}} .

Particle
========

.. figure:: /images/Blender_fluids_particle.jpg
   :width: 300px
   :figwidth: 300px

   Fluid particle settings


This type can be used to display particles created during the simulation.
For now only tracers swimming along with the fluid are supported.
Note that the object can have any shape,
position or type - once the particle button is pressed, a particle system with the fluid
simulation particles will be created for it at the correct position.
When moving the original object, it might be necessary to delete the particle system,
disable the fluidsim particles, and enable them again.
The fluidsim particles are currently also unaffected by any other particle forces or settings.

:guilabel:`Influence`
    :guilabel:`Size Influence`
       The particles can have different sizes, if this value is 0 all are forced to be the same size.

    :guilabel:`Alpha Influence`
       If this value is >0, the alpha values of the particles are changed according to their size.

:guilabel:`Particle type`
   :guilabel:`Drops`
      Surface splashes of the fluid result in droplets being strewn about, like fresh water, with low Surface Tension.

   :guilabel:`Floats`
      The surface tension of the fluid is higher and the fluid heavier, like cold seawater and soup. Breakaways are clumpier and fall back to the surface faster than :guilabel:`Drops`\ , as with high Surface Tension.

   :guilabel:`Tracer`
      Droplets follow the surface of the water where it existed, like a fog suspended above previous fluid levels. Use this to see where the fluid level has been.

:guilabel:`Path` (bake directory)
   The simulation run from which to load the particles. This should usually have the same value as the fluid domain object (e.g. copy by :kbd:`ctrl-C`\ , :kbd:`ctrl-V`\ ).


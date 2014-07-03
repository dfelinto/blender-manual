..    TODO/Review: {{review}} .


Smoke Simulation
================


Development notes
-----------------


Blender's new smoke simulation is based on the paper '[http://www.cs.cornell.edu/~tedkim/wturb
Wavelet Turbulence for Fluid Simulation]' and associated sample code.

It has been implemented in Blender by Daniel Genrich and Miika Hamalainen.


Inner working
-------------


The simulator uses a volumetric fluid-based model, with the end results output as voxel grids. This voxel data is visualized interactively in Blender's 3D view using custom OpenGL shading, and can be rendered using the Voxel Data texture. Blender's **smoke simulation** wraps Voxels around existing :doc:`Particles <physics/particles>`\ . It requires a particle-emitting object and a 'domain' object within which smoke is rendered.


.. admonition:: Note
   :class: note

   This Part of the Documentation uses the 2.58 Release


User workflow
-------------


The smoke simulation is similar to the Fluid simulation:
a Domain and Flow object is required to do a smoke simulation:


- set as the simulation :doc:`Domain <physics/smoke/domain>` an object that defines the bounds of the simulation volume,
- set as the :doc:`Flow object <physics/smoke/flow_object>` an object which determines where the smoke will be produced from,
- set :doc:`Collision objects <physics/smoke/collisions>`\ , to make the smoke interact with objects in the scene.
- assign a :doc:`Material <physics/smoke/material>` to the smoke
- save the project
- :doc:`bake <physics/smoke/baking>` the simulation

In case you are having troubles, please consult the :doc:`Appendix <physics/smoke/appendix>`


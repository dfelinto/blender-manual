
Fluid Simulation
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode / :guilabel:`Edit mode` (Mesh)
   | Panel:    :guilabel:`Physics` sub-context → :guilabel:`Fluid`


Description
===========

While modeling a scene with blender,
certain objects can be marked to participate in the fluid simulation, e.g.
as fluid or as an obstacle. The bounding box of another object will be used to define a
box-shaped region to simulate the fluid in (the so called "simulation domain").
The global simulation parameters (such as viscosity and gravity)
can be set for this domain object.

Using the :guilabel:`BAKE` button,
the geometry and settings are exported to the simulator and the fluid simulation is performed,
generating a surface mesh together with a preview for each animation frame,
and saving them to hard disk. Then the appropriate fluid surface for the current frame is
loaded from disk and displayed or rendered.


.. figure:: /images/Manual-Part-X-fluidsim-example1.jpg
   :width: 640px
   :figwidth: 640px

   A breaking dam.


Workflow
========

In general, you follow these steps:


- set the :doc:`simulation domain <physics/fluid/domain>` (the portion of the scene where the fluid will flow),
- set the :doc:`fluid source(s) <physics/fluid/fluid_object>`, and specify its material, viscosity, and initial velocity,
- eventually, set other :doc:`objects to control the volume <physics/fluid/volume>` of the fluid (inlets and outlets),
- eventually, set other objects related to the fluid, like:
  - :doc:`obstacles <physics/fluid/obstacle>`,
  - :doc:`particles <physics/fluid/particle>` floating on the fluid,
  - :doc:`fluid control <physics/fluid/control>`, to shape part of the fluid in the desired form,
- eventually, :doc:`animate the fluid properties <physics/fluid/animation>`,
- :doc:`Bake the simulation <physics/fluid/domain>` (eventually, revise as necessary and bake repeatedly).


.. admonition:: Baking is done on the Domain object!
   :class: nicetip

   When you calculate the fluid simulation, **you bake the simulation on the domain object**.

   For this reason:

   - all the baking options are visible only when selecting the Domain Object,
   - baking options are explained in the  :doc:`the baking section <physics/fluid/domain#baking>` of the Domain manual page.


More about the simulation
=========================

To know more about simulating fluids in Blender you can read:


- some :doc:`useful hint <physics/fluid/hints>` about the simulation,
- some :doc:`technical details <physics/fluid/technical_details>`, to learn how to do a more realistic fluid simulation,
- the :doc:`fluids appendix <physics/fluid/appendix>` to learn limitations and workarounds, and some additional links.


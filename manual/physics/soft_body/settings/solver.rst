.. _physics-softbody-settings-solver:

******
Solver
******

.. reference::

   :Panel:     :menuselection:`Physics --> Soft Body --> Solver`

The settings in the *Soft Body Solver* panel determine the accuracy of the simulation.

Step Size Min
   Minimum simulation steps per frame. Increase this value, if the soft body misses fast-moving collision objects.
Max
   Maximum simulation steps per frame.
   Normally the number of simulation steps is set dynamically
   (with the *Error Limit*) but you have probably a good reason to change it.

Auto-Step
   Use velocities for automatic step sizes.
   Helps the Solver figure out how much work it needs to do based on how fast things are moving.

Error Limit
   Rules the overall quality of the solution delivered.
   The most critical setting that defines how precise the solver should check for collisions.
   Start with a value that is half the average edge length.
   If there are visible errors, jitter, or over-exaggerated responses, decrease the value.
   The solver keeps track of how "bad" it is doing and the *Error Limit* causes the solver to
   do some "adaptive step sizing".


Diagnostics
===========

Print Performance to Console
   Prints on the console how the solver is doing.

Estimate Matrix
   Estimate matrix, split to ``COM``, ``ROT``, ``SCALE``.

.. (TODO) explain what it is, when it can be useful

   Center of mass -- Location of the center of mass.
   Rot Matrix -- Estimated the rotation matrix.
   Scale Matrix -- Estimated the scale matrix.


Helpers
=======

These settings control how the soft body will react (deform)
once it either gets close to or actually intersects (cuts into) another collision object on the same layer.

Choke
   Calms down (reduces the exit velocity of) a vertex or edge once it penetrates a collision mesh.

Fuzzy
   Fuzziness while on collision, high values make collision handling faster but less stable.
   Simulation is faster, but less accurate.

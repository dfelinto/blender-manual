.. index:: Object Constraints; Camera Solver Constraint
.. _bpy.types.CameraSolverConstraint:

************************
Camera Solver Constraint
************************

The *Camera Solver* constraint gives the owner of this constraint,
the location and rotation of the "solved camera motion".

The "solved camera motion" is where Blender reconstructs the position of the physical, real-world camera,
when it filmed the video footage, relative to the thing being tracked.

.. note::

   This constraint only works after you have set up a minimum of eight markers and pressed
   :ref:`Solve Camera Motion <editors-movie-clip-tracking-clip-solve-motion>`
   (:menuselection:`Movie Clip Editor --> Toolbar --> Solve --> Solve Camera Motion`).


Options
=======

.. figure:: /images/animation_constraints_motion-tracking_camera-solver_panel.png

   Camera Solver Constraint panel.

Active Clip
   Receive tracking data from the movie clip active in the Movie Clip editor.
   If unchecked, an option appears to choose from the other clips.

Constraint to F-Curve
   Applies the constraint, creating Keyframes for the transforms.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.

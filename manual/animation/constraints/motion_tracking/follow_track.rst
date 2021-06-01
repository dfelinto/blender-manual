.. index:: Object Constraints; Follow Track Constraint
.. _bpy.types.FollowTrackConstraint:

***********************
Follow Track Constraint
***********************

By default the Follow Track constraint is making objects have the same position at a frame as the track has.
The motion of this object happens on a single plane defined by the camera and the original position of the object.


Options
=======

.. figure:: /images/animation_constraints_motion-tracking_follow-track_panel.png

   Follow Track Constraint panel.

Active Clip
   Receive tracking data from the active movie clip in the Movie Clip editor.
   If unchecked, an option appears to choose from the other available clips.

3D Position
   Use the 3D position of the track to parent to.

Undistorted
   Parent to the undistorted position of the 2D track.

Frame Method
   Defines how the footage is fitted in the camera frame.

Camera
   Select the camera to which the motion is parented to (if empty, the active scene camera is used).

Depth Object
   If this object is set, constrained objects will be projected onto the surface
   of this depth object which can be used to create facial makeup visual effects.

Constraint to F-Curve
   Creates F-curves for the object that copies the movement caused by the constraint.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. youtube:: KZalGrjGKSA

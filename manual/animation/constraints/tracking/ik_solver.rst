.. index:: Object Constraints; Inverse Kinematics Constraint
.. _bpy.types.KinematicConstraint:

*****************************
Inverse Kinematics Constraint
*****************************

The *Inverse Kinematics* constraint implements the *inverse kinematics* armature
posing technique. Hence, it is only available for bones.
To quickly create an IK constraint with a target, select a bone in Pose Mode,
and press :kbd:`Shift-I`.

This constraint is fully documented in
the :ref:`Inverse Kinematics <bone-constraints-inverse-kinematics>` page, part of the rigging chapter.

.. note::

   The IK constraints are special in that they modify multiple bones.
   For this reason, they ignore their position in the stack and
   always run after all other constraints on the affected bones. To apply constraints after IK,
   it is necessary to first copy the final transformation to a new bone chain,
   e.g. using :doc:`Copy Transforms </animation/constraints/transform/copy_transforms>`.


Options
=======

.. figure:: /images/animation_constraints_tracking_ik-solver_panel.png

   Inverse Kinematics panel.

Target
   :ref:`ui-data-id` used to select the an armature.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Pole Target
   Object for pole rotation.

Iterations
   Maximum number of solving iterations.

Chain Length
   How many bones are included in the IK effect. Set to 0 to include all bones.

Use Tail
   Include bone's tail as last element in chain.

Stretch
   Enable IK stretching.

Weight Position
   For Tree-IK: Weight of position control for this target.

Rotation
   Chain follows rotation of target.

Target
   Disable for targetless IK.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


iTaSC Solver
------------

If the :ref:`iTaSC IK Solver <rigging-armatures_posing_bone-constraints_ik_model_itasc>`
is used, the IK Solver Constraint changes to add these addition parameters.

IK Type
   Copy Pose
      Equivalent to the traditional end effector position and orientation constraint:
      the end effector is constrained to take the position, and optionally the orientation,
      of a given target, which is set in the target field.

      Position/Rotation Locking
         Allows to obtain various effect by not constraining the coordinates along certain axis.

         Axis Reference
            Specifies how to compute the axis coordinates.

            Bone
               The coordinates are the position and orientation of the target relative to the bone.
            Target
               The opposite of *Bone*, the coordinates are the position and
               orientation of the tip of the bone relative to the target.
   Distance
      Specify that the end effector will stay inside, at, or outside a sphere centered on the target object.

      Limit Mode
         Inside
            The end effector will stay inside of the distance from the target object.
         Outside
            The end effector will stay outside of the distance from the target object.
         On Surface
            The end effector will stay exactly at the distance from the target object.

      Distance
         The radius from the target object.

.. note::

   The *Influence* parameter is not implemented if *Pole Target* is used.


Example
=======

.. peertube:: 20f9cc94-1c52-4485-bca3-272df8a899a2

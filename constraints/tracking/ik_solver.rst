
..    TODO/Review: {{review|}} .

IK Solver Constraint
====================

The :guilabel:`Inverse Kinematics` constraint implements the *inverse kinematics* armature
posing technique. Hence, it is only available for bones.
To quickly create an IK constraint with a target, select a bone in pose mode,
and press :kbd:`Shift` :kbd:`I`.

This constraint is fully documented in the :doc:`inverse kinematics page <rigging/posing/inverse_kinematics>` of the rigging chapter.


Options
-------

.. figure:: /images/25-Manual-Constraints-Tracking-IK.jpg
   :width: 305px
   :figwidth: 305px

   Inverse Kinematics panel


:guilabel:`Target`
   Must be an armature
:guilabel:`Bone`
   A bone in the armature
:guilabel:`Pole Target`
   Object for pole rotation
:guilabel:`Iterations`
   Maximum number of solving iterations
:guilabel:`Chain Length`
   How many bones are included in the IK effect. Set to 0 to include all bones

   :guilabel:`Use Tail`
      Include bone's tail as last element in chain
   :guilabel:`Stretch`
      Enable IK stretching
:guilabel:`Weight`:
   :guilabel:`Position`
      For Tree-IK: Weight of position control for this target
   :guilabel:`Rotation`
      Chain follow rotation of target
:guilabel:`Target`
   Disable for targetless IK
:guilabel:`Rotation`
   Chain follows rotation of target



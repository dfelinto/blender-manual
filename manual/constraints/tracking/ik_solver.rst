
..    TODO/Review: {{review|}} .

IK Solver Constraint
********************

The :guilabel:`Inverse Kinematics` constraint implements the *inverse kinematics* armature
posing technique. Hence, it is only available for bones.
To quickly create an IK constraint with a target, select a bone in pose mode,
and press :kbd:`Shift` :kbd:`I`.

This constraint is fully documented in the :doc:`inverse kinematics page </rigging/posing/inverse_kinematics>` of the rigging chapter.


Options
=======

.. figure:: /images/25-Manual-Constraints-Tracking-IK.jpg
   :width: 305px
   :figwidth: 305px

   Inverse Kinematics panel


Target
   Must be an armature
Bone
   A bone in the armature
Pole Target
   Object for pole rotation
Iterations
   Maximum number of solving iterations
Chain Length
   How many bones are included in the IK effect. Set to 0 to include all bones

   Use Tail
      Include bone's tail as last element in chain
   Stretch
      Enable IK stretching
Weight:
   Position
      For Tree-IK: Weight of position control for this target
   Rotation
      Chain follow rotation of target
Target
   Disable for targetless IK
Rotation
   Chain follows rotation of target



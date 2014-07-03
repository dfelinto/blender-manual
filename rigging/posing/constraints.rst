
..    TODO/Review: {{review|}} .


Applying Constraints to Bones
=============================


.. figure:: /images/Doc26-rigging-constraints.jpg

   The Constraints panel in Pose mode, with one Floor constraint applied to the active bone (Bone.001).


As bones behave like objects in :guilabel:`Pose` mode, they can also be constrained. This is
why the :guilabel:`Constraints` panel is shown in both :guilabel:`Object` and
:guilabel:`Editing` contexts in this mode… This panel contains the constraints *of the active
bone* (its name is displayed at the top of the panel,
in the :guilabel:`To Bone:…` static text field).

Constraining bones can be used to control their degree of freedom in their pose transformations, using e.g. the :guilabel:`Limit` constraints. You can also use constraints to make a bone track another object/bone (inside the same object, or in another armature), etc. And the :doc:`inverse kinematics feature <rigging/posing/inverse_kinematics>` is also mainly available through the :guilabel:`IK Solver` constraint - which is specific to bones.

For example, a human elbow can't rotate backward (unless the character has broken his hand),
nor to the sides, and its forward and roll rotations are limited in a given range
(for example, depending on the rest position of your elbow,

it may be from **0- ** to **160- **\ , OR from **-45- ** to **135- **\ ).

So you should apply a :guilabel:`Limit Rotation` constraint to the forearm bone
(as the elbow movement is the result of rotating the forearm bone around its root).

Using bones in constraints, either as owners or as targets, is discussed in detail in the :doc:`constraints pages <constraints>`\ .



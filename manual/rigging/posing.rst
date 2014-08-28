
..    TODO/Review: {{review|partial=X}} .

Posing
******

Once your armature is :doc:`skinned </rigging/skinning>` by the needed object(s), you can start to pose it. Basically, by transforming its bones, you deform or transform the skin object(s). But you don't do that in :guilabel:`Edit` mode - remember that in this mode, you edit *the default, base, "rest" position of your armature*. You can't use the :guilabel:`Object` mode either, as here you can only transform whole objects...

So, armatures in Blender have a third mode, :guilabel:`Pose`, dedicated to this process. It's a sort of "object mode for bones". In rest position (as edited in :guilabel:`Edit` mode), each bone has its own position/rotation/scale to neutral values (i.e. **0.0** for position and rotation, and **1.0** for scale). Hence, when you edit a bone in :guilabel:`Pose` mode, you create an offset in its transform properties, from its rest position - this is quite similar to :doc:`meshes' relative shape keys </animation/techs/shape/shape_keys>`, in fact.


Posing Section Overview
=======================

In this section, we will see:

- The :doc:`visualization features </rigging/posing/visualization>` specific to :guilabel:`Pose` mode.
- How to :doc:`select and edit bones </rigging/posing/editing>` in this mode.
- How to :doc:`use pose library </rigging/posing/pose_library>`.
- How to :doc:`use constraints </rigging/posing/constraints>` to control your bones' DoF (degrees of freedom).
- How to :doc:`use inverse kinematics features </rigging/posing/inverse_kinematics>`.
- How to :doc:`use the Spline inverse kinematics features </rigging/posing/inverse_kinematics/spline_ik>`.

Even though it might be used for completely static purposes, posing is heavily connected with :doc:`animation features and techniques </animation>`.

In this part, we will try to focus on animation-independent posing, but this isn't always possible. So if you know nothing about animation in Blender, it might be a good idea to read the :doc:`animation features and techniques </animation>` chapter first, and then come back here.


See Also
========

As usual, see the :doc:`tutorials </igging>` for more demonstrative examples, and especially :doc:`this BSoD one </nimation/bsod/character_animation#animation>`.



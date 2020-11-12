
*****
Limbs
*****

These rig types handle generation of different kind of limbs and their features, like fingers.


``limbs.simple_tentacle``
=========================

Will create a bendy and stretchy b-bones tentacle chain or automatic bendy and stretchy finger controls.

Requirement: A chain of at least two connected bones.

Automation Axis (X, Y, Z, None)
   Enables the automation on the selected axis. Multiple axis or none can be selected holding :kbd:`Shift-LMB`.
   When enabled the controls of the last bones will copy the rotations from the previous ones.
   The option is exposed on the controls of the final rig as a Copy Rotation constraint and
   can be disabled even after rig is generated, or at animation time.


``limbs.super_finger``
======================

Will create a bendy and stretchy chain or automatic bendy and stretchy finger depending on a master control bone.

Requirement: A chain of at least two connected bones.

Bend Rotation Axis (X, Y, Z, -X, -Y, -Z)
   Defines the automatic rotation axis to be linked to the scale of the master bone.


``limbs.super_limb``
====================

Will create a full featured bendy and stretchy limb depending on the user defined options.
Available limb types:

Arm
   Requirement: A chain of at least three connected bones (upper_arm, forearm, hand).

   Rotation Axis (Automatic, X, Z)
      Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
   Limb Segments (integer)
      Defines the number of additional tweak controls each limb bone will have on the final rig.
   B-Bone Segments (integer)
      Defines the number of b-bone segments each tweak control will be split into.
   FK Extra Layers
      Defines on which bone layer the FK chain will be created.
      The yellow dot shows where will be placed the IK chain
      (by default is the same layer of meta-rig's limb chain).
   Tweak Extra Layers
      Defines on which bone layer the Tweak controls will be created.
      The yellow dot shows where will be placed the IK chain
      (by default is the same layer of meta-rig's limb chain).

Leg
   Requirement: A chain of at least four connected bones and a last child used as
   heel pivot (thigh, shin, foot, toe, heel).

   Rotation Axis (Automatic, X, Z)
      Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
   Limb Segments (integer)
      Defines the number of additional tweak controls each limb bone will have on the final rig.
   B-Bone Segments (integer)
      Defines the number of b-bone segments each tweak control will be split into.
   FK Extra Layers
      Defines on which bone layer the FK chain will be created.
      The yellow dot shows where will be placed the IK chain
      (by default is the same layer of meta-rig's limb chain).
   Tweak Extra Layers
      Defines on which bone layer the Tweak controls will be created.
      The yellow dot shows where will be placed the IK chain
      (by default is the same layer of meta-rig's limb chain).

Paw
   Requirement: A chain of at least four connected bones (upper_arm, forearm, paw, toe) or (thigh, shin, paw, toe).

   Rotation Axis (Automatic, X, Z)
      Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
   Limb Segments (integer)
      Defines the number of additional tweak controls each limb bone will have on the final rig.
   B-Bone Segments (integer)
      Defines the number of b-bone segments each tweak control will be split into.
   FK Extra Layers
      Defines on which bone layer the FK chain will be created.
      The yellow dot shows where will be placed the IK chain
      (by default is the same layer of meta-rig's limb chain).
   Tweak Extra Layers
      Defines on which bone layer the Tweak controls will be created.
      The yellow dot shows where will be placed the IK chain
      (by default is the same layer of meta-rig's limb chain).


``limbs.super_palm``
====================

Will create a palm system based on the distance between palm bones.

Requirement: At least two bones child of the same parent.
The property has to be set on the inner palm bones (think it as index's metacarpus),
the rig control will appear on the last palm bone (think it as pinky's metacarpus).

Bend Rotation Axis (X, Z)
   Defines the automatic rotation axis to be used on the palm bones.

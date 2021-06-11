
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
   The option is accessible in the controls of the final rig as a Copy Rotation constraint and
   can be disabled even after rig is generated, or at animation time.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls on different layers from the main controls.


``limbs.super_finger``
======================

Will create a bendy and stretchy chain or automatic bendy and stretchy finger depending on a master control bone.

Requirement: A chain of at least two connected bones.

Bend Rotation Axis (Automatic, X, Y, Z, -X, -Y, -Z)
   Defines the automatic rotation axis to be linked to the scale of the master bone.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
IK Control
   Generates a very simple IK mechanism with only one control.

   IK starts its work with the shape of the finger defined by FK controls and adjusts it
   to make the fingertip touch the IK control. It is designed as a tool to temporarily keep
   the fingertip locked to a surface it touches, rather than a fully featured posing system.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls on different layers from the main controls.


``limbs.super_limb``
====================

A backwards compatibility wrapper around ``limbs.arm``, ``limbs.leg`` and ``limbs.paw``.


``limbs.arm``
=============

Will create a full featured bendy and stretchy arm depending on the user-defined options.

Requirement: A chain of three connected bones (upper_arm, forearm, hand).

.. figure:: /images/addons_rigging_rigify_rig-types_limbs_arm-required.png

   Arm required bones.

IK Wrist Pivot
   Generates an extra child of the hand IK control that rotates around the tail of the hand bone.

Rotation Axis (Automatic, X, Z)
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
Limb Segments (integer)
   Defines the number of additional tweak controls each limb bone will have on the final rig.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Custom IK Pivot
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
Assign FK Layers
   If enabled, allows placing the FK chain on different layers from the IK bones.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls on different layers from the IK bones.


``limbs.leg``
=============

Will create a full featured bendy and stretchy leg depending on the user-defined options.

Requirement: A chain of four connected bones (thigh, shin, foot, toe) with one unconnected
child of the foot to be used as the heel pivot.

.. figure:: /images/addons_rigging_rigify_rig-types_limbs_leg-required.png

   Leg required bones.

Rotation Axis (Automatic, X, Z)
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
Limb Segments (integer)
   Defines the number of additional tweak controls each limb bone will have on the final rig.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Custom IK Pivot
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
Assign FK Layers
   If enabled, allows placing the FK chain on different layers from the IK bones.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls on different layers from the IK bones.


``limbs.paw``
=============

Will create a full featured bendy and stretchy paw depending on the user-defined options.

Requirement: A chain of four or five connected bones (thigh, shin, paw, *optional* digit, toe).

.. figure:: /images/addons_rigging_rigify_rig-types_limbs_leg-required.png

   Leg required bones.

Rotation Axis (Automatic, X, Z)
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
Limb Segments (integer)
   Defines the number of additional tweak controls each limb bone will have on the final rig.
B-Bone Segments (integer)
   Defines the number of b-bone segments each tweak control will be split into.
Custom IK Pivot
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
Assign FK Layers
   If enabled, allows placing the FK chain on different layers from the IK bones.
Assign Tweak Layers
   If enabled, allows placing the Tweak controls on different layers from the IK bones.


``limbs.front_paw``
===================

Derivative of ``limbs.paw`` with extended IK suitable for use in front paws.
The additional IK limits the degree of change in the angle between shin and
paw bones (2nd and 3rd) as the main IK control moves and rotates.

For best results, the shin bone should not be parallel to either thigh or paw in rest pose,
i.e. there should be some degree of bend in all joints of the paw.

Heel IK Influence
   Influence of the extended IK. At fully rotating the main IK control or digit bone would
   not affect the rotation of the paw bone, while lower values provide some blending.


``limbs.rear_paw``
==================

Derivative of ``limbs.paw`` with extended IK suitable for use in rear paws.
The additional IK tries to maintain thigh and paw bones (1st and 3rd) in a nearly parallel orientation
as the main IK control moves and rotates.

For best results, thigh and paw bones should start nearly parallel in the rest pose.


``limbs.super_palm``
====================

Will create a palm system based on the distance between palm bones.

Requirement: At least two bones child of the same parent.
The property has to be set on the inner palm bones (think it as index's metacarpus),
the rig control will appear on the last palm bone (think it as pinky's metacarpus).

Both Sides
   Generates controls on both sides of the palm, with influence on inner bones blended between them.

Primary Rotation Axis (X, Z)
   Defines the automatic rotation axis to be used on the palm bones.


**********************
Generated Rig Features
**********************

After human rig generation a new armature named ``rig`` will be added to your scene.
This is the character rig you have generated from the human meta-rig and will contain all the features.

Limbs
=====

Each limb will have a gear widget at its base. This is the utility bone that
contains all the sub-rig properties. The rig features will be displayed anyway
when the affected bone is selected but if you are looking in the Graph editor for
those properties' animated values, this is most likely the bone to look at.

Depending on the user defined meta-rig options, multiple deform bone segments will be created.
Each bone can be controlled by tweak controls placed at the respective bone's head/tail.
Tweaks are subordinate to the general IK or FK limb position but can be moved apart,
twisted and scaled freely, even reaching virtually impossible limb shapes.

Rigify's limbs have the following controls in the Sidebar panel:

.. figure:: /images/addons_rigging_rigify_rig-features_limb-properties.png
   :align: right

FK Limb Follow :guilabel:`Slider`
   When set to 1 the FK limb will not rotate with the torso and will retain is rotation
   relative to the root bone instead.

IK-FK :guilabel:`Slider`
   Controls whether the limb follows IK or FK controls, blending between full IK at 0 and full FK at 1.

IK<->FK Snapping :guilabel:`Buttons`
   To snap one type of controls to another use the appropriate buttons.

   Each snap direction has buttons to update just the current pose, bake the whole animation in the
   current *Action*, or *Clear* keyframes instead of snapping. The buttons dealing with keyframes
   use options from an additional panel to control the range of frames to bake.

IK Stretch :guilabel:`Slider`
   Blends between the limb stretching freely at 1, or having its maximum length constrained at 0.

Toggle Pole :guilabel:`Switch`
   When set to 0 the IK limb will use the rotational pole vector (the arrow at the base of the limb).
   Rotating/translating/scaling the arrow will control the IK limb base.
   When set to 1 the classic pole vector will be displayed and used to orient the IK limb.
   The arrow will continue to handle the scale and the location of the IK limb base.

   Similar to IK-FK Snapping, the row includes buttons to convert the current pose between types,
   or bake the whole action.

IK Parent :guilabel:`Switch`
   Switches the effective parent of the main IK control, with different integer values corresponding
   to choices from a list.

   The row includes buttons that allow converting the current pose via choosing from a menu,
   or baking the whole action.

Pole Parent :guilabel:`Switch`
   Switches the effective parent of the classic IK Pole control.


Head
====

Neck Follow :guilabel:`Slider`
   This slider controls the rotations isolation for the neck bones.
   When set to 0 the neck will stay oriented as the Torso (the big box control).
   When set to 1 the neck will be oriented as the Chest (the big circle in the shoulder area).

Head Follow :guilabel:`Slider`
   This slider controls the rotations isolation for the head.
   When set to 0 the head will stay oriented as the Torso (the big box control).
   When set to 1 the head will be oriented as the neck.


Face
====

Mouth Lock :guilabel:`Slider`
   This slider controls the mouth opening.
   When set to 0 moving/rotating the jaw bone will result in mouth opening,
   when set to 1 the lips will stay sealed while the jaw is moving.

Eyes Following :guilabel:`Slider`
   This slider controls the eyelid automation.
   When set to 1 the eyelids and the lower eyebrow will follow
   the eye movement giving a realistic effect to the character,
   when set to 0 no automation will happen.

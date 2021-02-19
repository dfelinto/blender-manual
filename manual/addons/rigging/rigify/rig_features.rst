
**********************
Generated Rig Features
**********************

After human rig generation a new armature named "Rig" will be added to your scene.
This is the character rig you have generated from the human meta-rig and will contain all the features.


Limbs
=====

Each limb will have a gear widget at its base. This is the utility bone that
contains all the sub-rig properties. The rig features will be displayed anyway
when the affected bone is selected but if you are looking in the Graph editor for
those properties' animated values, this is most likely the bone to look at.
Rigify's super limb will list the following features:

IK/FK Snapping
   To snap one chain to another just select the control you want to snap and
   in the Sidebar panel the snap buttons will appear. Click on the snap you want and it's done!

FK Limb Isolation
   Slider (0, 1)

   When set to 1 the FK arm will not rotate with the torso and will retain is rotation in world space instead.

IK Following
   Boolean (0=False, 1=True)

   When the IK follow is set to 1 the IK limb will follow its parent depending on the Root/Parent slider.
   When set to 0 the IK limb will stay fixed in space whatever the rest of the rig will do.
   This is a useful option if you want to create your own Child Of constraint on the IK limb toward
   another part of the rig itself (like parenting the hand to the head).

   IK Limb Domain Space Select
      Slider Root/Parent (0=Root, 1=Parent)

      When set to Root the IK limb will move with the root,
      when set to Parent will move along with the torso.
      This value depends from the IK Follow option.

IK/FK Limb Interactive Blending
   Slider (0=IK, 1=FK)

   When set to IK the arm will follow the IK controls,
   when set to FK the arm will follow the FK controls.

Pole Vector Type Switch
   Boolean (0=Rotational Pole, 1=Standard pole vector)

   When set to 0 the IK arm will use the rotational pole vector (the arrow at the base of the limb).
   Rotating/translating/scaling the arrow will control the IK limb base.
   When set to 1 the classic pole vector will be displayed and used to orient the IK limb.
   The arrow will continue to handle the scale and the location of the IK limb base.

   Pole Vector Following
      Slider (0= Root, 1=Limb)

      If pole vector switch is set to 1 (standard pole), then this value defines the pole's parenting.
      If Pole Following is set to 1 then the pole vector will be parented to the limb,
      if set to 0 will instead follow the root. This properties also depends on the IK follow control.
      When the general IK follow is set to 0, then the pole vector following will have no effect.

IK Auto-Stretching
   Slider (0=No stretching, 1=Full Stretch)

   When set to 0 the IK limb it's constrained to its rest length.
   When set to 1 the IK limb will stretch until it reaches the IK effector.

Bendy Bones Flexible Tweaking
   For each limb -- depending on the user defined meta-rig options -- multiple bone segments will be created.
   Each bone can be controlled by controls placed at the respective bone's head/tail.
   Tweaks movement will depend from the general IK limb position but
   they can be moved apart, twisted and scaled freely, even reaching virtually impossible limb shapes.

   Just select the desired tweak control and do whatever you want with it.


Torso
=====

Neck Follow
   Slider (0=Neck Follows Torso, 1=Neck Follows Chest)

   This slider controls the rotations isolation for the neck bones.
   When set to 0 the neck will stay oriented as the Torso (the big box control).
   When set to 1 the neck will be oriented as the Chest (the big circle in the shoulder area).
Head Follow
   Slider (0=Head Follows Torso, 1=Head Follows Neck)

   This slider controls the rotations isolation for the head.
   When set to 0 the head will stay oriented as the Torso (the big box control).
   When set to 1 the head will be oriented as the neck.


Face
====

Mouth Lock
   Slider (0=Free Lips, 1=Lips Sealed)

   This slider controls the mouth opening.
   When set to 0 moving/rotating the jaw bone will result in mouth opening,
   when set to 1 the lips will stay sealed while the jaw is moving.

Eyes Following
   Slider (0=locked eyelids, 1=automatic eyelids)

   This slider controls the eyelid automation.
   When set to 1 the eyelids and the lower eyebrow will follow
   the eye movement giving a realistic effect to the character,
   when set to 0 no automation will happen.

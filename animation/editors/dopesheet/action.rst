
..    TODO/Review: {{review|partial=X}} .


Action Editor
=============


Blender 2.5 simplifies the system by making Actions the generic containers for F-Curves.
Actions can contain any number of F-Curves, and can be attached to any data block.As long as
the RNA data paths stored in the Action's F-Curves can be found on that data block,
the animation will work. For example, an action modifying 'X location' and 'Y location'
properties can be shared across multiple objects,
since both objects have 'X location' and 'Y location' properties beneath them.

The :guilabel:`Action Editor` window enables you to see and edit the FCurve datablocks you defined as actions in the :guilabel:`FCurve Editor` window. So it takes place somewhere in-between the low-level :doc:`FCurves <animation/editors/graph>`\ , and the high-level :doc:`NLA editor <animation/editors/nla>`\ . Hence, you do not have to use them for simple Ipo curves animations - and they have not much interest in themselves, so you will mostly use this window when you do :doc:`NLA animation <animation/editors/nla>` (they do have a few specific usages on their own, though, like e.g. with the :doc:`Action constraint <constraints/relationship/action>`\ , or the :doc:`pose libraries <rigging/posing/pose_library>`\ …).

This is not a mandatory window, as you do can edit the actions used by the NLA directly in the
:guilabel:`FCurve Editor` window (or even the :guilabel:`NLA Editor` one). However,
it gives you a slightly simplified view of your FCurve datablocks
(somewhat similar to the "key" mode of the FCurve window,
even though more powerful in some ways) - and, more interesting,
it can show you all "action" FCurve datablocks of a same object at once.

Additionally, it also allows you to affect timing of the different keys of the layers created with the :doc:`grease pencil tool <3d_interaction/sketching>`\ .

Each "action" FCurve datablock forms a top-level channel (see below).
Note that an object can have several :guilabel:`Constraint` (one per animated constraint)
and :guilabel:`Pose` (for armatures, one per animated bone) FCurve datablocks,
and hence an action can have several of these channels.


Action Datablocks
-----------------

As everything else in Blender, actions are datablocks. Unlike FCurve ones,
there is only one type of action, which can regroup all FCurve of a given object.
You'll find its usual datablock controls in the :guilabel:`Action Editor` header.

However, there is one specificity with action datablocks: they have by default a "fake user",
i.e. once created, they are always kept in Blender file, even if no object uses them.
This is due to the fact that actions are designed to be used in the NLA,
where you can affect several different actions to a same object! Yes,
this is the only way to use different actions (and hence,
different FCurve datablocks of the same kind) to animate a same object.
But as you have to assign an action to an object to be able to edit it
(and an object can only have one action datablock at a time), to have "fake users" guaranties
you that you won't lost your precious previously-edited actions when you start working on a
new one!

This window shows, by default, the action datablock linked to the current active object.
However, as with FCurvs, you can pin an :guilabel:`Action Editor` to a given action with the
small "pin" button to the left of the datablock controls, in the header.
This will force the window to always display this datablock,
whatever the current selected object is.


Channel Menu
------------

:guilabel:`Delete` (\ :kbd:`X`\ )
   Deletes the whole channel from the current action (i.e. unlink the underlying FCurve datablock from this action datablock).

 .. warning::

   FIXME - warning body below

The :kbd:`X` shortcut is area-dependent: if you use it in the left list part, it'll delete the selected channels, whereas if you use it in the main area, it'll delete the selected keyframes…

:menuselection:`Settings --> Toogle/Enable/Disable a Setting` (\ :kbd:`shift-W`\ /\ :kbd:`ctrl-shift-W`\ /\ :kbd:`alt-W`\ )
   Enable/disable a channel's setting (selected in the menu that pops-up) - currently, "lock" and/or "mute" only.

:guilabel:`Toggle Channel Editability` :kbd:`Tab`
   Locks or unlocks a channel for editing

:guilabel:`Extrapolation Mode`
   Change the extrapolation between selected keyframes. More options are available in the Graph Editor.

:guilabel:`Expand Channels`\ , :guilabel:`Collapse Channels` (\ :kbd:`pad-+`\ , :kbd:`pad--`\ )
   Expands or collapses selected channels.

:guilabel:`Move...`
   This allows you to move top-level channels up/down (\ :kbd:`shift-pgup`\ /\ :kbd:`shift-pgdown`\ ), or directly to the top/bottom (\ :kbd:`ctrl-shift-pgup`\ /\ :kbd:`ctrl-shift-pgdown`\ ).

:guilabel:`Revive Disabled F-Curves`
   Clears 'disabled' tag from all F-Curves to get broken F-Curves working again



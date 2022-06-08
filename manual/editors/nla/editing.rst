
*******
Editing
*******

Transform
=========

Todo.


.. _bpy.ops.nla.snap:

Snap
====

Todo.


.. _bpy.ops.nla.bake:

Bake Action
===========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Edit --> Bake Action`

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object and Pose Modes
   :Menu:      :menuselection:`Header --> Object Animation --> Bake Action...`

The final motion of objects or bones depends not only on the keyframed animation,
but also on any active F-Curve modifiers, drivers, and constraints.
On each frame of all the scene's frames, the *Bake Action* operator computes
the final animation of the selected objects or bones with all those
modifiers, drivers, and constraints applied, and keyframes the result.

This can be useful for adding deviation to a cyclic action like a :term:`Walk Cycle`,
or to create a keyframe animation created from drivers or constraints.


.. _bpy.ops.nla.duplicate:

Duplicate
=========

.. reference::

   :Menu:      :menuselection:`Edit --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Creates a new instance of the selected strips with a copy of the action.


Linked Duplicate
================

.. reference::

   :Menu:      :menuselection:`Edit --> Linked Duplicate`
   :Shortcut:  :kbd:`Alt-D`

The contents of one Action strip can be instanced multiple times. To instance another strip,
select a strip, go to :menuselection:`Edit --> Linked Duplicate`.
It will uses the same action as the selected strips.

Now, when any strip is tweaked, the others will change too.
If a strip other than the original is tweaked,
the original will turn to red.

.. figure:: /images/editors_nla_editing_linked-strip-edit.png

   Linked duplicated strip being edited.


.. _bpy.ops.nla.split:

Split Strips
============

Todo.


.. _bpy.ops.nla.delete:

Delete Strips
=============

Todo.


.. _bpy.ops.nla.tracks_delete:

Delete Tracks
=============

Todo.


.. _bpy.ops.nla.mute_toggle:

Toggle Muting
=============

Todo.


.. _bpy.ops.nla.apply_scale:

Apply Scale
===========

Todo.


.. _bpy.ops.nla.clear_scale:

Clear Scale
===========

Todo.


.. _bpy.ops.nla.action_sync_length:

Sync Action Length
==================

Todo.


.. _bpy.ops.nla.make_single_user:

Make Single User
================

.. reference::

   :Menu:      :menuselection:`Edit --> Make Single User`
   :Shortcut:  :kbd:`U`

This tool ensures that none of the selected strips use an action which is also used by any other strips.

.. note::

   This does not recursively go inside meta strips.


.. _bpy.ops.nla.swap:

Swap Strips
===========

Todo.


.. _bpy.ops.nla.move_up:

Move Strips Up
==============

Todo.


.. _bpy.ops.nla.move_down:

Move Strips Down
================

Todo.


Track Ordering
==============

Todo.


.. _bpy.ops.anim.channels_clean_empty:

Remove Empty Animation Data
===========================

.. reference::

   :Menu:      :menuselection:`Edit --> Remove Empty Animation Data`

This operator removes AnimData data-blocks (restricted to only those
which are visible in the animation editor where it is run from) which are "empty"
(i.e. that is, have no active action, drivers, and NLA tracks or strips).

It is sometimes possible to end up with a lot of data-blocks which have old and
unused Animation Data containers still attached.
This most commonly happens when doing motion graphics work
(i.e. when some linked-in objects may have previously been used to develop a set of reusable assets),
and is particularly distracting in the NLA Editor.


.. _bpy.ops.nla.tweakmode_enter:

Start Editing Stashed Action
============================

.. reference::

   :Menu:      :menuselection:`Edit --> Start Editing Stashed Action`
   :Shortcut:  :kbd:`Shift-Tab`

It will enter and exit Tweak Mode as usual, but will also make sure that the action can be edited in isolation
(by flagging the NLA track that the action strip comes from as being "solo").
This is useful for editing stashed actions, without the rest of the NLA Stack interfering.

When you finished editing the strip, simply go to :menuselection:`Edit --> Stop Editing Stashed Action`
or press :kbd:`Shift-Tab`.

.. list-table::

   * - .. figure:: /images/editors_nla_editing_nla-mode.png
          :width: 320px

          Strip in NLA mode.

     - .. figure:: /images/editors_nla_editing_edit-mode.png
          :width: 320px

          Strip in Tweak mode.


Start Tweaking Strips Actions (Full Stack)
==========================================

.. reference::

   :Menu:      :menuselection:`Edit --> Start Tweaking Strips Actions (Full Stack)`

Allows you to edit the contents of the strip without disabling all the tracks above the tweaked strip.
This allows keyframing to work as expected, and preserves the pose that you visually keyed.

When you finished editing the strip, simply go to :menuselection:`Edit --> Stop Tweaking Strips Actions`
or press :kbd:`Tab`.

.. note::

   For transitions above the tweaked strip, keyframe remapping will fail
   for channel values that are affected by the transition.
   A work around is to tweak the active strip without evaluating the upper NLA stack.


Start Tweaking Strips Actions (Lower Stack)
===========================================

.. reference::

   :Menu:      :menuselection:`Edit --> Start Tweaking Strips Actions (Lower Stack)`
   :Shortcut:  :kbd:`Tab`

The contents of Action strips can be edited, but you must be in *Tweak Mode* to do so.
The keyframes of the action can then be edited in the Dope Sheet.

When you finished editing the strip, simply go to :menuselection:`Edit --> Stop Tweaking Strips Actions`
or press :kbd:`Tab`.


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


.. _bpy.ops.nla.duplicate:

Duplicate
=========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Edit --> Duplicate`
   :Hotkey:    :kbd:`Shift-D`

Creates a new instance of the selected strips with a copy of the action.


Linked Duplicate
================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Edit --> Linked Duplicate`
   :Hotkey:    :kbd:`Alt-D`

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

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Edit --> Make Single User`
   :Hotkey:    :kbd:`U`

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


.. _bpy.ops.anim.channels_move:

Track Ordering
==============

Todo.


.. _bpy.ops.anim.channels_clean_empty:

Remove Empty Animation Data
===========================

.. admonition:: Reference
   :class: refbox

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

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Edit --> Start Editing Stashed Action`
   :Hotkey:    :kbd:`Shift-Tab`

It will enter and exit Tweak Mode as usual, but will also make sure that the action can be edited in isolation
(by flagging the NLA track that the action strip comes from as being "solo").
This is useful for editing stashed actions, without the rest of the NLA Stack interfering.


Start Tweaking Strips Action
============================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Edit --> Start Tweaking Strips Action`
   :Hotkey:    :kbd:`Tab`

The contents of Action strips can be edited, but you must be in *Tweak Mode* to do so.
The keyframes of the action can then be edited in the Dope Sheet.

.. list-table::

   * - .. figure:: /images/editors_nla_editing_nla-mode.png
          :width: 320px

          Strip in NLA mode.

     - .. figure:: /images/editors_nla_editing_edit-mode.png
          :width: 320px

          Strip in Tweak mode.

When you finished editing the strip, simply go to :menuselection:`Edit --> Tweaking Strips Action`
or press :kbd:`Tab`.

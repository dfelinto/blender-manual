.. _bpy.ops.pose.select_all:

*********
Selecting
*********

Selection in *Pose Mode* is very similar to the one in :doc:`Edit Mode </animation/armatures/bones/selecting>`,
with a few deviations:
You can only select *whole bones* in *Pose Mode*, not roots/tips...


.. _bpy.ops.pose.select_mirror:

Select Mirror
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Mirror`
   :Shortcut:  :kbd:`Shift-Ctrl-M`

Flip the selection from one side to another.


.. _bpy.ops.pose.select_constraint_target:

Constraint Target
=================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Constraint Target`

Todo.


.. _bpy.ops.pose.select_linked:

Linked
======

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Linked`
   :Shortcut:  :kbd:`L`

Selects all the bones in the chain which the active (last selected) bone belongs to.

All Forks
   Selects all bones connected to the active bone even if the branch off from the current bone.

.. list-table:: Linked bones selection.

   * - .. figure:: /images/animation_armatures_bones_selecting_single-bone.png
          :width: 320px

          A single selected bone.

     - .. figure:: /images/animation_armatures_bones_selecting_whole-chain.png
          :width: 320px

          Its whole chain selected with Linked.


.. _bpy.ops.pose.select_hierarchy:

Select More/Less
================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Select More/Less`

Parent :kbd:`[`, Child :kbd:`]`
   You can deselect the active bone and select its immediate parent or one of its children.
Extend Parent :kbd:`Shift-[`, Extend Child :kbd:`Shift-]`
   Similar to *Parent*/*Child* but it keeps the active bone in the selection.


.. _bpy.ops.pose.select_grouped:

Grouped
=======

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Select --> Grouped`
   :Shortcut:  :kbd:`Shift-G`

You can select bones based on their group and/or layer, through the *Select Grouped* pop-up menu :kbd:`Shift-G`:

Layer
   To select all bones belonging to the same layer(s) as the selected ones,
   use the *In Same Layer* entry.
Group
   To select all bones belonging to the same group(s) as the selected ones,
   use the *In Same Group* entry.
Keying Set
   ToDo.


Select Pattern
==============

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select Pattern...`

Selects all bones whose name matches a given pattern.
Supported wild-cards: \* matches everything, ? matches any single character,
[abc] matches characters in "abc", and [!abc] match any character not in "abc".
As an example \*house\* matches any name that contains "house",
while floor\* matches any name starting with "floor".

Case Sensitive
   The matching can be chosen to be case sensitive or not.
Extend
   When *Extend* checkbox is checked the selection is extended instead of generating a new one.


*********
Selecting
*********

.. _bpy.ops.clip.select_box:

Box Select
==========

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Box Select`
   :Hotkey:    :kbd:`B`

See :ref:`tool-select-box`.


.. _bpy.ops.clip.select_circle:

Circle Select
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Circle Select`
   :Hotkey:    :kbd:`C`

See :ref:`tool-select-circle`.


.. _bpy.ops.clip.select_all:

(De)select All
==============

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> (De)select All`
   :Hotkey:    :kbd:`A`

Selects all items.


Inverse
=======

.. admonition:: Reference
   :class: refaabox

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Inverse`
   :Hotkey:    :kbd:`Ctrl-I`

Selects non-selected items and deselects existing selection.


.. _bpy.ops.clip.select_grouped:

Select Grouped
==============

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Select Grouped`
   :Hotkey:    :kbd:`Shift-G`

Select all tracks from specified group.

Action
   The group of tracks to select.

   :Keyframed Tracks: Select all keyframed tracks.
   :Estimated Tracks: Select all estimated tracks.
   :Tracked Tracks: Select all tracked tracks.
   :Locked Tracks: Select all locked tracks.
   :Disabled Tracks: Select all disabled tracks.
   :Track with Same Color: Select all tracks with same color as active track.
   :Failed Tracks: Select all tracks which failed to be reconstructed.


.. _bpy.ops.clip.stabilize_2d_select:

Select Stabilization Tracks
===========================

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking mode
   :Menu:      :menuselection:`Select --> Select Stabilization Tracks`

Select tracks which are used for translation stabilization.


.. _bpy.ops.clip.stabilize_2d_rotation_select:

Select Stabilization Rotation Tracks
====================================

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking mode
   :Menu:      :menuselection:`Select --> Select Stabilization Rotation Tracks`

Select tracks which are used for rotation stabilization.

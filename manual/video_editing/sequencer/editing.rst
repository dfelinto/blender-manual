
*******
Editing
*******

Transform
=========

.. _bpy.ops.transform.seq_slide:

Move
----

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Move`
   :Hotkey:    :kbd:`G`

Pressing :kbd:`G` moves all the selected strip(s).
Move your mouse horizontally (left/right) to change the strip's position in time.
Move vertically (up/down) to change channels.

Holding down :kbd:`Ctrl` while dragging snaps to the start and endpoints of other strips.
The position of the mouse relative to the selection influences where the strips are snapped.
If it is closer to the start of the selection, then the start frame of the selection gets snapped,
else the end frame will get snapped.

To "ripple edit" (make room for strips you drag) hold :kbd:`Alt` when placing a strip.

You can also lock the direction to time with :kbd:`X` or to change the strip's channel with :kbd:`Y`.

It is possible to move strips using mouse by dragging them while holding :kbd:`LMB`.
Currently it is possible to move only one strip by dragging.


Start Frame Offset
^^^^^^^^^^^^^^^^^^

The *Start Frame Offset* for that strip can be selected by clicking :kbd:`LMB` on the left handle of the strip;
holding it down (or pressing :kbd:`G` and then moving the mouse left/right)
changes the start frame within the strip by the number of frames you move it.
The frame number label under the strip displays the start frame of the strip.

- If you have a 20-image sequence strip, and drag the left handle to the right by 10 frames,
  the strip will start at image 11 (images 1 to 10 will be skipped).
  Use this to clip off a roll-up or undesired lead-in.
- Dragging the left handle left will create a lead-in (copies) of the first frame for as many frames as you drag it.
  Use this when you want some frames for a transition at the start of the clip.


End Frame
^^^^^^^^^

The *End Frame* of the strip could be selected by clicking :kbd:`LMB` on the right handle of the strip;
holding it down (or pressing :kbd:`G`) and then moving the mouse changes the ending frame within the strip.
The frame number label over the strip displays the end frame of the strip.

- Dragging the right handle to the left shortens the clip;
  any original images at the tail are ignored. Use this to quickly clip off a roll-down.
- Dragging the right handle to the right extends the clip.
  For movies and images sequences, more of the animation is used until exhausted.
  Extending a clip beyond its length will render as a copy of the last image.
  Use this for transitions out of this clip.

.. note:: Multiple selection

   You can select several (handles of) strips by :kbd:`Shift-LMB` clicking: when you press :kbd:`G`,
   everything that is selected will move with your mouse -- this means that,
   for example, you can at the same time move a strip, shorten two others, and extend a forth one.


Move/Extend from Current Frame
------------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Move/Extend from Current Frame`
   :Hotkey:    :kbd:`E`

With a number of strips selected, pressing :kbd:`E` lets you interactively extend the strips.
This is similar to moving but is useful for extending (or shortening) time around the current frame.

All selected strip handles to the "mouse side" of the current frame indicator will transform together,
so you can change the duration of the current frame.


.. _bpy.ops.sequencer.slip:

Slip Strip Contents
-------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Slip Strip Contents`
   :Hotkey:    :kbd:`S`

The Slip tool allows you to change the position of the contents of a strip without moving the strip itself.


.. _bpy.ops.sequencer.snap:

Snap Strips to the Current Frame
--------------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Snap Strips to the Current Frame`
   :Hotkey:    :kbd:`Shift-S`

Moves the strip or control point to the current frame.


.. _bpy.ops.sequencer.offset_clear:

Clear Strips Offset
-------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Clear Strips Offset`
   :Hotkey:    :kbd:`Alt-O`

To reset the (soft) start/end frame handles.


.. _bpy.ops.sequencer.swap:

Swap Strips
-----------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Swap Strips`

Left :kbd:`Alt-Left`
   Swaps the active strip with the strip to the left.
Right :kbd:`Alt-Right`
   Swaps the active strip with the strip to the right.


.. _bpy.ops.sequencer.gap_remove:

Remove Gaps
-----------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Insert Gaps`
   :Hotkey:    :kbd:`Backspace`

Remove blank frames between the current frame and the first strip to the right,
independent of selection or locked state of strips.


.. _bpy.ops.sequencer.gap_insert:

Insert Gaps
-----------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Transform --> Insert Gaps`
   :Hotkey:    :kbd:`Equals`

Insert blank frames between the current frame and the first strips to the right,
independent of selection or locked state of strips.


.. _bpy.ops.sequencer.split:

Split
=====

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Split`
   :Hotkey:    :kbd:`K`

This splits the selected strip in two at the current frame.
This will result in two strips which use the same source, fitting the original strip's timing and length.

.. hint::

   This can be thought of as a quick way to duplicate the current strip,
   adjusting the start/end frames to form two non-overlapping strips showing the same content as before.


Hold Split
==========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Hold Split`
   :Hotkey:    :kbd:`Shift-K`

Like *Split*, it splits a strip in two distinct strips;
however you will not be able to drag the endpoints to show the frames past the split of each resulting strip.

Although you can adjust the :ref:`Hold Offset <sequencer-duration-hard>`
number fields in the *Strip Info* panel.

.. hint::

   This can be thought of as a way to simulate splitting the video file in two parts at the cut-point,
   replacing the current strip with each.


.. _bpy.ops.sequencer.duplicate_move:

Duplicate Strips
================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Duplicate Strips`
   :Hotkey:    :kbd:`Shift-D`

Duplicate a strip to make an unlinked copy;
drag it to a time and channel, and drop it by :kbd:`LMB` click.


.. _bpy.ops.sequencer.delete:

Delete
======

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Delete`
   :Hotkey:    :kbd:`Delete`, :kbd:`X`

Delete the selected strip(s).


Separate Images
===============

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Separate Images`
   :Hotkey:    :kbd:`Y`

For images sequence only -- Converts the strip into multiple strips, one strip for each frame.
Useful for slide shows and other cases where you want to bring in a set on non-continuous images.

Length
   You have to specify the duration you want the resulting strips will be.


Movie Strip
===========

.. _bpy.ops.sequencer.rendersize:

Set Render Size
---------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Set Render Size`

Sets the render resolution and aspect to match the strip's resolution.


.. _bpy.ops.sequencer.deinterlace_selected_movies:

Deinterlace Movies
------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Deinterlace Movies`

Converts interlaced video into progressive video.


.. _sequencer-edit-change:

Effect Strip
============

.. _bpy.ops.sequencer.change_effect_input:

Change Effect Input
-------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Effect Strip --> Change Effect Type`

Swaps which strips are the input for the effect strip.


.. _bpy.ops.sequencer.change_effect_type:

Change Effect Type
------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Effect Strip --> Change Effect Type`

Switch the effects on a selected Effect strip.


.. _bpy.ops.sequencer.reassign_inputs:

Reassign Inputs
---------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Effect Strip --> Reassign Inputs`
   :Hotkey:    :kbd:`R`

This tool can be used to assign (reconnect) effect strips in a different way.
Select three arbitrary strips and press :kbd:`R`.
If you don't create a cycle, those will be connected to a new effect chain.


.. _bpy.ops.sequencer.swap_inputs:

Swap Inputs
-----------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Strip --> Effect Strip --> Swap Inputs`
   :Hotkey:    :kbd:`Alt-S`

Swaps the first two inputs for the effect strip.


Lock/Mute
=========

.. _bpy.ops.sequencer.lock:
.. _bpy.ops.sequencer.unlock:

Lock Strips :kbd:`Shift-L`
   Disables the strip from being transformed.
Unlock Strips :kbd:`Shift-Alt-L`
   Enables disabled strips allowing them to be transformed.

.. _bpy.ops.sequencer.mute:
.. _bpy.ops.sequencer.unmute:

Mute/Unmute Strips :kbd:`H`, :kbd:`Alt-H`
   Mute or unmute the selected strips.
Mute/Unmute Deselected Strips :kbd:`Shift-H`, :kbd:`Ctrl-Alt-H`
   Mute or unmute all strips but the selected.


Inputs
======

.. _bpy.ops.sequencer.reload:

Reload Strips :kbd:`Alt-R`
   Reloads the strips from their external saved location.
Reload Strips and Adjust Length :kbd:`Shift-Alt-R`
   Reloads the strips from their external saved location and re-adjusts the strip duration.

.. _bpy.ops.sequencer.change_path:

Change Path/Files
   Changes the source file contained in a selected strip.

.. _bpy.ops.sequencer.swap_data:

Swap Data
   Swaps two sequence strips.


Context Menu
============

You can activate context menu by clicking :kbd:`RMB` in the Sequencer's timeline.
In this menu you can quickly access some commonly used tools.


Fades
=====

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Add --> Fades`

This submenu contains tools to add or remove fades to strips.
In case of visual strips the tools will animate the opacity or volume in case of audio strips.

Clear Fades
   Removes fade animation from selected sequences.
Fade In and Out
   Fade selected strips in and out.
Fade In
   Fade in selected strips.
Fade Out
   Fade out selected strips.
From Current Frame
   Fade from the current frame to the end of overlapping sequences.
To Current Frame
   Fade from the start of sequences under the Playhead to the current frame.

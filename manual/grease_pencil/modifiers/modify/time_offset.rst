.. index:: Grease Pencil Modifiers; Time Offset Modifier
.. _bpy.types.TimeGpencilModifier:

********************
Time Offset Modifier
********************

The *Time Offset* Modifier offsets the position of Grease Pencil keyframes.

For example can be used to start the same animation loop
at different times and avoid an unappealing synchronization of the loops.

Or if you have different character poses in several keyframes,
the Time Offset Modifier can be use to select which pose to show at a particular time in the animation.
This is especially useful for cut-out animation.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_time-offset_panel.png
   :align: right

   Time Offset Modifier.

Mode
   Regular
      Offsets keyframes in default animation playback direction (left to right).

   Reverse
      Offsets keyframes in inverse animation playback direction (right to left).

   Fixed Frame
      Keep the selected frame fixed and do not change over time.

      Frame
         Frame number to use.

Frame Offset
   Number of frames to offset the original keyframes.

Scale
   Evaluation time (in seconds).

Keep Loop
   Moves end frame to the animation start to keep animation in a loop.


Custom Range
------------

When enabled, uses a custom range of frames.

Frame Start/End
   Sets the range start and end frames.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.

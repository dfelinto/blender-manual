
*************
Interpolation
*************

Interpolate
============

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw and Edit Modes
   :Tool:      :menuselection:`Toolbar --> Interpolate`
   :Hotkey:    :kbd:`Ctrl-E`

When you are animating simple shapes you can use the interpolate tool
to automatically add new breakdown keyframes.

See :ref:`Interpolate tool <tool-grease-pencil-draw-interpolate>` for more details.


Interpolate Sequence
=====================

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw and Edit Modes
   :Menu:      :menuselection:`Header --> Interpolate`
   :Hotkey:    :kbd:`Shift-Ctrl-E`

Interpolate strokes between the previous and next keyframe by adding *multiple* keyframes.
When you are on a frame between two keyframes and click the sequence button
a breakdown keyframe will be added on every frame between the previous and next keyframe.

Step
   The number of frames between generated interpolated frames.
Layer
   Restrict the interpolation to Active or All layers.
Only selected (:guilabel:`Edit Mode Only`)
   When enabled, only selected strokes will be interpolated.
Flip Mode
   Invert strokes start and end. Automatic will try to found the right mode for every stroke.
Smooth
   Amount of smoothing to apply to interpolated strokes for reducing jitter/noise.
Iterations
   Number of time to smooth newly created strokes.
Type
   Interpolation method to use for the sequence.


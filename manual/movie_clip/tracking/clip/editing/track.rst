
*****
Track
*****

Clear Solution
==============

Todo.


.. _bpy.ops.clip.solve_camera:

Solve Solution
==============

The *Camera Motion* operator solves the motion of camera using all tracks placed
on the footage and two keyframes specified on this panel. There are some requirements:

- There should be at least eight common tracks on the both of the selected keyframes.
- There should be noticeable parallax effects between these two keyframes.

If everything goes smoothly during the solve, the average reprojection error is reported to
the information space and to the Clip editor header. Reprojection error means the average
distance between reconstructed 3D position of tracks projected back to footage and
original position of tracks. Basically, reprojection error below 0.3 means accurate reprojection,
(0.3 - 3.0) means quite nice solving which still can be used.
Values above 3 means some tracks should be tracked more accurately,
or that values for focal length or distortion coefficients were set incorrectly.

.. (todo 2.62) object solver


Clear After
===========

Todo.


Clear Before
============

Todo.


Clear Track Path
================

Todo.


.. _bpy.ops.clip.join_tracks:

Join Tracks
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking
   :Menu:      :menuselection:`Track --> Join Tracks`
   :Hotkey:    :kbd:`Ctrl-J`

This operator joins all selected tracks into one.
Selected tracks should not have common tracked or keyframed markers at the same frame.

.. (wip)
   Joining two tracks now works better for tracks which have got intersection by frames:
   coordinates of joined track would be interpolated linearly on segments with intersection.
   This is still not perfect from accurate solving point of view,
   but this allows to prevent camera jump which is much more annoying than sight camera slide.


.. _bpy.ops.clip.clean_tracks:

Clean Tracks
============

Identifies all tracks which matches settings from above and performs desired action on them.

Tracked Frames
   Tracks or tracked segments shorter than this number of frames will be removed.
Reprojection Error
   Tracks which has reprojection error higher than this value will be removed.
Action
   Several actions can be performed for bad tracks.

   Select
      They can simply be selected.
   Delete Track
      The whole track can be deleted.
   Delete Segments
      Bad segments of tracked sequence can be removed.


Copy Tracks
===========

Todo.


Paste Tracks
============

Todo.


Track Frame Backwards
=====================

Todo.


Track Backwards
===============

Todo.


Track Forwards
==============

Todo.


Track Frame Forwards
====================

Todo.


.. _bpy.ops.clip.delete_track:

Delete Track
============

Delete all selected tracks.


Delete Marker
=============

Todo.


.. _bpy.ops.clip.add_marker_move:

Add Marker and Move
===================

Places a new marker at the position of the mouse
(which is under the button in this case, not ideal but it is just how things work)
and then it can be moved to the needed location. When it is moved to the desired position,
:kbd:`LMB` can be used to finish placing the new marker.
Also, :kbd:`Return` and :kbd:`Spacebar` can be used to finish placing the marker.
But it is faster to use :kbd:`Ctrl-LMB` to place markers directly on the footage.
This shortcut will place the marker in the place you have clicked.
One more feature here: until you have released the mouse button,
you can adjust the marker position by moving the mouse and
using the track preview widget to control how accurately the marker is placed.


Show/Hide
=========

Todo.


Transform
=========

Todo.

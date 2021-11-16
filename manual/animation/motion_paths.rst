.. _bpy.types.AnimVizMotionPaths:
.. _bpy.types.MotionPath:

************
Motion Paths
************

.. reference::

   :Editor:    3D Viewport, Properties
   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Motion Paths`

.. reference::

   :Editor:    3D Viewport, Properties
   :Mode:      Pose Mode
   :Panel:     :menuselection:`Properties --> Armature --> Motion Paths`
   :Menu:      :menuselection:`Pose --> Motion Paths`

.. figure:: /images/animation_motion-paths_example-object.png
   :width: 400px

   An animated cube with its motion path displayed.

The Motion Paths tool allows you to visualize the motion of points as paths over a series of frames.
These points can be object origins and bone joints.

To create or remove motion paths, it is necessary to first select the bones. Then:

#. To show the paths (or update them, if needed), click on the *Calculate Path* button.
#. To hide the paths, click on the *Clear Paths* button.

.. note::

   Remember that only selected bones and their paths are affected by these actions!

The paths are shown in a light shade of gray for unselected points,
and a slightly bluish gray for selected ones.
Around the current frame a glow indicate the direction of movement:
blue towards future frames and green towards the past.
Each frame is displayed by a small white dot on the paths.

The paths are automatically updated when you edit your poses/keyframes,
and they are also active during animation playback. Playing the animation
affects the paths only when the *Around Current Frame* option is enabled.


Options
=======

.. figure:: /images/animation_motion-paths_panel.png

   The Motion Paths panel in the Armature tab.

.. _bpy.types.AnimVizMotionPaths.type:

Paths Type
   Type of range to show for Motion Paths.

   :Around Frame:
      Display paths of points within a fixed number of frames around the current frame.
      When you enable this button, you get paths for a given number of frames before and after the current one
      (again, as with ghosts).
   :In Range:
      Display paths of points within specified range.

      .. _bpy.ops.pose.paths_range_update:

      Update Range from Scene (Clock Icon)
         Updates the display frame range from the scene frame range.

.. _bpy.types.AnimVizMotionPaths.frame_start:
.. _bpy.types.AnimVizMotionPaths.frame_end:

Frame Range Start, End
   Starting and Ending frame of range of paths to display/calculate
   (not for *Around Current Frame* onion skinning method).

.. _bpy.types.AnimVizMotionPaths.frame_before:
.. _bpy.types.AnimVizMotionPaths.frame_after:

Frame Range Before, After
   Number of frames to show before and after the current frame
   (only for *Around Current Frame* onion skinning method).

.. _bpy.types.AnimVizMotionPaths.frame_step:

Step
   Allows displaying one point for every *n* frames on the path.
   Mostly useful when you enable the frame number display (see below), to avoid cluttering the 3D Viewport.

.. _bpy.types.MotionPath.frame_start:
.. _bpy.types.MotionPath.frame_end:

Cache/Bone Cache From, To
   These are the start/end frames of the range in which motion paths are shown.
   You cannot modify this range without deleting the motion path first.

.. _bpy.ops.pose.paths_calculate:
.. _bpy.ops.object.paths_calculate:

Calculate
   If no paths have been calculated, Calculate Paths will create a new motion path in cache based on
   the options specified in the pop-up menu or the :ref:`bpy.ops.screen.redo_last` panel.
   Note, if the current context is an Armature calculating the objects motion paths, and not the bones,
   this operator will calculate the motion paths for all the bones within the armature as well.

   Start, End
      These are the start/end frames of the range in which motion paths are shown.
      The start frame is *inclusive*, so if you set *Start* to 1,
      you will really see the frame 1 as starting point of the paths...

   Bake Location
      Which point on the bones is used when calculating paths.
      Only available for bones while in Pose Mode.

      :Heads: Calculates the path position of the bone's heads.
      :Tails: Calculates the path position of the bone's heads.

.. _bpy.ops.pose.paths_update:
.. _bpy.ops.object.paths_update:

Update Paths
   In the case a path has already been calculated, this operator will update the path shape to the current animation.
   To change the frame range of the calculated path, you need to delete the path and calculate it again.

   .. _bpy.ops.pose.paths_clear:
   .. _bpy.ops.object.paths_clear:

   Clear Paths ``X``
      Clears paths on all objects/bones or just the selected ones when holding :kbd:`Shift`.

.. _bpy.ops.object.paths_update_visible:

Update All Paths
   Recalculates the motion paths for all visible objects and poses.


Display
-------

.. _bpy.types.AnimVizMotionPaths.show_frame_numbers:

Frame Numbers
   When enabled, a small number appears next to each frame dot on the path,
   which is of course the number of the corresponding frame.

.. _bpy.types.AnimVizMotionPaths.show_keyframe_highlight:

Keyframes
   When enabled, big yellow square dots are displayed on motion paths, showing the keyframes of their bones
   (i.e. only the paths of keyed bones at a given frame get a yellow dot at this frame).

.. _bpy.types.AnimVizMotionPaths.show_keyframe_action_all:

\+ Non-Grouped Keyframes
   For bone motion paths, it searches the whole Action for keyframes instead of
   in groups with matching name only (this is slower).

.. _bpy.types.AnimVizMotionPaths.show_keyframe_numbers:

Keyframe Numbers
   When enabled, you will see the numbers of the displayed keyframes,
   so this option is obviously only valid when *Show Keys* is enabled.

.. _bpy.types.MotionPath.lines:

Lines
   Toggles whether the lines between the points are shown.

.. _bpy.types.MotionPath.line_thickness:

Thickness
   Line thickness for motion path.

.. _bpy.types.MotionPath.use_custom_color:
.. _bpy.types.MotionPath.color:

Custom Color
   Use custom color for this motion path.


Example
=======

.. figure:: /images/animation_motion-paths_example-armature.png

   An example of a motion path of an armature.


*********
Animation
*********

The *Animation* section lets you manage settings related to :doc:`Animation </animation/index>`.
This includes how editors look and also some different tools properties.

.. figure:: /images/editors_preferences_section_animation.png

   Blender Preferences Animation section.


Timeline
========

These settings control things in the :doc:`Timeline </editors/timeline>`.

Allow Negative Frame
   Playback and animations can occur during negative frame ranges.
Minimum Grid Spacing
   The minimum number of pixels between grid lines.
Timecode Style
   Format of timecodes displayed when not displaying timing in terms of frames.
   The format uses '+' as a separator for sub-second frame numbers,
   with left and right truncation of the timecode as necessary.
Zoom to Frame Type
   Defines what time range (around the cursor) will be displayed
   when the *View Frame* :kbd:`Numpad0` is performed.

   Keep Range
      The currently displayed time range is preserved.
   Seconds
      The number of seconds specified in the *Zoom Seconds* field will be shown around the cursor.
   Keyframes
      The number of animation keyframes defined in the *Zoom Keyframes* field will be shown around the cursor.


Keyframes
=========

These settings control :doc:`Keyframes </animation/keyframes/index>`
which are the building blocks for animations.

Visual Keying
   When an object is using constraints, the object property value does not actually change.
   *Visual Keying* will add keyframes to the object property,
   with a value based on the visual transformation from the constraint.

Only Insert Needed
   This will only insert keyframes if the value of the property is different.

Auto-Keyframing
   Show Warning
      Displays a warning at the top right of the *3D Viewport*, when moving objects, if *Auto Keyframe* is on.
   Only Insert Available
      This will only add keyframes to channels of F-Curves that already exist.
   Enable in New Scenes
      Enables *Auto Keyframe* by default for new scenes.

   .. seealso::

      Learn more about :ref:`Auto-Keyframing <bpy.types.ToolSettings.use_keyframe_insert_auto>`.


F-Curves
========

These settings control how :doc:`F-Curves </editors/graph_editor/fcurves/index>`
look and their default behavior.

Unselected Opacity
   Controls the opacity of unselected :doc:`F-Curves </editors/graph_editor/fcurves/index>` against
   the background of the Graph Editor.
Default Smoothing Mode
   Controls the behavior of :ref:`automatic curve handles <editors-graph-fcurves-settings-handles>`
   for newly created F-Curves.
Default Interpolation
   Controls the default :ref:`Interpolation <editors-graph-fcurves-settings-interpolation>`
   for newly created keyframes.
Default Handles
   Controls the default :ref:`Handle <editors-graph-fcurves-settings-handles>` for newly created F-Curves.
XYZ to RGB
   Color for X, Y, or Z animation curves (location, scale or rotation)
   is the same as the color for the X, Y, and Z axis.
Show Group Colors
   Display groups and channels with colors matching their corresponding groups.

.. |first| unicode:: U+02759 U+023F4
.. |last|  unicode:: U+023F5 U+02759
.. |rewind| unicode:: U+025C0
.. |play|   unicode:: U+025B6
.. |previous| unicode:: U+025C6 U+023F4
.. |next|     unicode:: U+023F5 U+025C6
.. |pause| unicode:: U+023F8
.. |record| unicode:: U+023FA

.. _bpy.types.SpaceTimeline:
.. _bpy.ops.time:

********
Timeline
********

The *Timeline* editor, identified by a clock icon, is used for manipulating keyframes and
scrubbing the playhead.

.. figure:: /images/editors_timeline_interface.png

   The Timeline.

The *Timeline* gives the user a broad overview of a scene's animation,
by showing the current frame, the keyframes of the active object,
the start and end frames of your animation sequence, as well as markers set by the user.

The *Timeline* includes *Transport Controls*, to play, pause, and skip through an animation sequence.

It also includes tools for manipulating *Keyframes*, *Keying Sets*, and *Markers*.


Main View
=========

The main *Timeline* region displays the animation frames over time.

.. figure:: /images/editors_timeline_main.png

Here you can see the *Keyframes* (diamond shapes), *Playhead* (blue handle), *Scrollbar* (along the bottom).


Adjusting the View
------------------

The *Timeline* can be panned by holding :kbd:`MMB`,
then dragging the area left or right.

You can zoom the *Timeline* by using :kbd:`Ctrl-MMB`, the mouse :kbd:`Wheel`,
or pressing :kbd:`NumpadMinus` and :kbd:`NumpadPlus`.

You can also use the scrollbars, located at the bottom or the right of the editor, to pan and zoom the view.


Playhead
--------

The *Playhead* is the blue vertical line with the current frame number at the top.

.. figure:: /images/editors_timeline_cursor.png
   :align: right

   Playhead.

The *Playhead* can be set or moved to a new position by pressing or
holding :kbd:`LMB` in scrubbing area at the top of the timeline.

The *Playhead* can be moved in single-frame increments by pressing :kbd:`Left` or :kbd:`Right`,
or you can jump to the beginning or end frame by pressing :kbd:`Shift-Left` or :kbd:`Shift-Right`.


Frame Range
-----------

By default, the *Frame Range* is set to start at frame 1 and end at frame 250.
You can change the frame range in the top right of the Timeline header, or in the Output Properties.


Keyframes
---------

For the active and selected objects, keyframes are displayed as diamond shapes.

You can click to select one at a time, or select several by holding :kbd:`Shift`,
or by dragging a box around the keyframes.
You can then move single keys by dragging them,
and you can move multiple keys by pressing :kbd:`G` and scale them with :kbd:`S`.

*Only Selected Channels* can be enabled. :menuselection:`Timeline --> View --> Only Selected Channels`.
For *Armatures*, this will display the object keyframes,
and the keyframes for the active and selected pose bones.


Markers
-------

See the :doc:`Markers page </animation/markers>` for more information.


Header
======

Popovers
--------

.. _timeline-playback:

Playback Popover
^^^^^^^^^^^^^^^^

.. figure:: /images/editors_timeline_playback.png

The *Playback* popover contains options controlling the animation playback.

Sync
   .. figure:: /images/editors_timeline_red-fps.png
      :figwidth: 109px
      :align: right

      3D Viewport red FPS.

   When you play an animation, the frame rate is displayed at the top left of the 3D Viewport.
   If the scene is detailed and playback is slower than the set :ref:`Frame Rate <bpy.types.RenderSettings.fps>`,
   these options are used to synchronize the playback.

   Play Every Frame
      Plays every frame even if playback is slow.
   Frame Dropping
      Drop frames if playback becomes slower than the scene's frame rate.
   Sync to Audio
      Drop frames if playback becomes too slow to remain synced with audio.

Audio
   Scrubbing
      If your animation has sound, this option plays bits of the sound wave
      while you move the playhead with :kbd:`LMB` or keyboard arrows (like a moving playhead).
   Mute
      Mute the sound from any audio source.

Playback
   Limit Playback to Frame Range
      Don't allow selecting frames outside of the playback range using the mouse.

   .. _bpy.types.Screen.use_follow:

   Follow Current Frame
      Animation editors can be setup to always follow the time indicator as animation is being played back.
      Following will be done when animating and changing frame:
      When the cursor reaches the end of the screen, the next range of frames of the same width will be displayed.

.. _bpy.types.Screen.use_play:

Play In
   Active Editor
      While playing, updates the Timeline, if *Animation Editors* and *All 3D Viewports* disabled.
   3D Viewport
      While playing, updates the 3D Viewport and the Timeline.
   Animation Editors
      While playing, updates the Timeline, Dope Sheet, Graph Editor, Video Sequencer.
   Image Editor
      The Image editor in Mask mode.
   Properties Editor
      When the animation is playing, this will update the property values in the UI.
   Movie Clip Editor
      While playing, updates the Movie Clip Editor.
   Node Editors
      While playing, updates the Node properties for the node editors.
   Video Sequencer
      While playing, updates the Video Sequencer.

.. _bpy.types.Scene.show_subframe:

Show
   Subframes
      Display and allow changing the current scene subframe.


.. _timeline-keying:

Keying Popover
^^^^^^^^^^^^^^

.. figure:: /images/editors_timeline_keying.png

The *Keying* popover contains options that affect keyframe insertion.

.. _bpy.types.KeyingSetsAll.active:

Active Keying Set
   .. figure:: /images/editors_timeline_keying-sets.png
      :align: right

      Timeline Keying Sets.

   *Keying Sets* are a set of keyframe channels in one.
   They are made so the user can record multiple properties at the same time.
   With a keying set selected, when you insert a keyframe,
   Blender will add keyframes for the properties in the active *Keying Set*.
   There are some built-in keying sets, *LocRotScale*, and also custom keying sets.
   Custom keying sets can be defined in the panels
   :menuselection:`Properties --> Scene --> Keying Sets + Active Keying Set`.

   Insert Keyframes (plus icon)
      Insert keyframes on the current frame for the properties in the active *Keying Set*.
   Delete Keyframes (minus icon)
      Delete keyframes on the current frame for the properties in the active *Keying Set*.

.. _bpy.types.ToolSettings.keyframe_type:

New Keyframe Type
   :ref:`keyframe-type` on insertion.

.. _bpy.types.ToolSettings.use_keyframe_cycle_aware:

Cycle-Aware Keying
   When inserting keyframes into :ref:`trivially cyclic curves <bpy.types.FModifierCycles>`,
   special handling is applied to preserve the cycle integrity (most useful while tweaking an established cycle):

   - If a key insertion is attempted outside of the main time range of the cycle,
     it is remapped back inside the range.
   - When overwriting one of the end keys, the other one is updated appropriately.


.. Move to some content to animation?
.. _bpy.types.ToolSettings.use_keyframe_insert_auto:

Auto Keying Popover
^^^^^^^^^^^^^^^^^^^

.. figure:: /images/editors_timeline_keyframes-auto.png
   :align: right

   Timeline Auto Keyframe.

The record button (|record|) enables *Auto Keyframe*:
It will add and/or replace existing keyframes for the active object when you transform it in the 3D Viewport.
For example, when enabled, first set the Playhead to the desired frame,
then move an object in the 3D Viewport, or set a new value for a property in the UI.

When you set a new value for the properties,
Blender will add keyframes on the current frame for the transform properties.
Other use cases are :ref:`Fly/Walk Navigation <3dview-fly-walk>` to record the walk/flight path
and :ref:`Lock Camera to View <3dview-lock-camera-to-view>` to record the navigation in camera view.

.. note::

   Note that *Auto Keyframe* only works for transform properties (objects and bones),
   in the 3D Viewport (i.e. you can't use it e.g. to animate the colors of a material in the Properties...).

Add & Replace / Replace
   This controls how the auto keyframe mode works.
   Only one mode can be used at a time.

   Add & Replace
      Add or replace existing keyframes.
   Replace
      Only replace existing keyframes.

Only Active Keying Set
   When enabled, new keyframes for properties will be inserted into the active *Keying Set*.

Layered Recording
   Adds a new NLA Track and strip for every loop/pass made over the animation to allow non-destructive tweaking.


Menus
-----

.. _timeline-view-menu:

View Menu
^^^^^^^^^

The *View Menu* controls what you see, and what it looks like.

Show Seconds :kbd:`Ctrl-T`
   Whether to show the time in the X axis and the *Playhead* as
   frames (based on the FPS) or as seconds.
Sync Visible Range
   It synchronizes the horizontal panning and scale of the current editor
   with the other editors (Graph, Dope Sheet, NLA and Sequencer) when this option is set.
   That way you always have these editors showing the same section of frames.
Show Markers
   Shows the markers region. When disabled, the `Markers Menu`_ is also hidden
   and markers operators are not available in this editor.
Only Keyframes from Selected Channels
   For *Armatures*, this will display the object keyframes,
   and the keyframes for the active and selected pose bones.
Cache
   Show Cache
      Show all enabled types.

      Soft Body, Particles, Cloth, Smoke, Dynamic Paint, Rigid Body.

   .. figure:: /images/editors_timeline_cache.png

      Timeline Cache.

Frame All :kbd:`Home`
   Maximize the area based on the Animation Range.
Go to Current Frame :kbd:`Numpad0`
   Centers the Timeline to the Playhead.


Markers Menu
^^^^^^^^^^^^

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, markers are shown at the bottom of the editor.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

For descriptions of the different marker tools see :ref:`Editing Markers <animation-markers-editing>`.


.. _animation-editors-timeline-headercontrols:

Header Controls
---------------

The Timeline header controls.

.. figure:: /images/editors_timeline_header.png

   Timeline header controls.

   \1. Popovers for Playback and Keying, 2. Transport Controls, 3. Frame Controls


Transport Controls
^^^^^^^^^^^^^^^^^^

These buttons are used to set, play, rewind, the *Playhead*.

.. figure:: /images/editors_timeline_player-controls.png
   :align: right

   Transport controls.

Jump to Start (|first|) :kbd:`Shift-Left`
   This sets the cursor to the start of frame range.
Jump to Previous Keyframe (|previous|) :kbd:`Down`
   This sets the cursor to the previous keyframe.
Rewind (|rewind|) :kbd:`Shift-Ctrl-Spacebar`
   This plays the animation sequence in reverse.
   When playing the play buttons switch to a pause button.
Play (|play|) :kbd:`Spacebar`
   This plays the animation sequence.
   When playing the play buttons switch to a pause button.
Jump to Next Keyframe (|next|) :kbd:`Up`
   This sets the cursor to the next keyframe.
Jump to End (|last|) :kbd:`Shift-Right`
   This sets the cursor to the end of frame range.
Pause (|pause|) :kbd:`Spacebar`
   This stops the animation.


Frame Controls
^^^^^^^^^^^^^^

Current Frame :kbd:`Alt-Wheel`
   The current frame of the animation/playback range.
   Also the position of the *Playhead*.
Preview Range (clock icon)
   This is a temporary frame range used for previewing a smaller part of the full range.
   The preview range only affects the viewport, not the rendered output.
   See :ref:`graph-preview-range`.
Start Frame
   The start frame of the animation/playback range.
End Frame
   The end frame of the animation/playback range.

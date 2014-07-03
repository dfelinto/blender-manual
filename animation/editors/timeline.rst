
..    TODO/Review: {{review|text=Some parts need to be updated, wiki notes have been added below.}} .


The Timeline
============

The *Timeline* window, identified by a clock icon,
is shown by default at the bottom of the screen.


.. figure:: /images/K_Doc_Timeline.jpg
   :width: 700px
   :figwidth: 700px

   Timeline 2.69


The *Timeline* is not much of an editor, but more of a information and control window.

Here you can have an overview of the animation part of your scene
   What is the current time frame, either in frames or in seconds, where are the keyframes of the active object,
   the start and end frames of your animation, markers, etc...

The *Timeline* has *Player Controls*\ , to play, pause the animation,
and to skip though parts of the scene.

It also has some tools for *Keyframes*\ , *Keying Sets*\ , and *Markers*\ .


Timeline Elements
=================

Time Cursor
-----------

.. figure:: /images/K_Doc_Timeline_Cursor.jpg

   Time Cursor


The *Time Cursor* is the green line, its used to set and display the current time frame.

The *Time Cursor* can be set or moved to a new position by pressing or holding
:kbd:`lmb` in the Timeline window.

The current frame or second can be displayed on the *Time Cursor*\ ,
check the View menu for settings.

The *Time Cursor* can be moved in steps by pressing :kbd:`Arrow Left` or
:kbd:`Arrow Right`\ , or in steps of 10 frames by pressing :kbd:`Shift-Arrow up` or
:kbd:`Shift-Arrow Down`\ .


Keyframes
---------

For the active and selected objects, keyframes are displayed as a yellow line.

For *Armatures*\ , the object keyframes and the pose bones keyframes are drawn.

*Only Selected Channels* can be enabled. *Timeline > View > Only Selected Channels*\ .
For *Armatures*\ , this will draw the object keyframes,
and the keyframes for the active and selected pose bones.


Markers
-------

Markers are the small triangles, with their name near them.

Markers are usually used to identify key parts of the animation.


.. figure:: /images/K_Doc_Timeline_Markers.jpg
   :width: 700px
   :figwidth: 700px

   Markers


Markers can be selected by pressing :kbd:`RMB` or :kbd:`Shift-RMB` to select more.

See :doc:`Marker Menu <animation/editors/timeline#marker_menu>` below or :doc:`Markers <animation/markers>` for more info.


Adjusting the View
==================

Timeline Area
-------------

The main *Timeline* area displays the animation frames over time.


.. figure:: /images/K_Doc_Timeline_Main.jpg
   :width: 700px
   :figwidth: 700px

   Timeline Main Area


The *Timeline* can be panned by holding :kbd:`mmb`\ ,
then dragging the area left or right.

You can zoom the *Timeline* by using :kbd:`ctrl-mmb`\ , the mouse :kbd:`wheel`\ ,
or pressing the :kbd:`-` and :kbd:`+` keys on the numpad.

By default, the *Playback/Rendering Range* (Frame Start 1 to Frame End 200)
is a lighter shade of gray.
The start and end frame can be set to the *Time Cursor* by pressing :kbd:`S` or
:kbd:`E`\ .
The *Playback Range* can also be set by pressing :kbd:`P` then drawing a box.


Timeline Header
===============

View Menu
---------

The *View Menu* controls what you see, and what it looks like.

*Toggle Full Screen*
    Maximize or minimize the *Timeline* window. :kbd:`ctrl-Arrow Up` or :kbd:`ctrl-Arrow Down`

*Duplicate Area into New Window*
    This creates a new OS window, and sets the editor window to the *Timeline*\ .

*Bind Camera to Markers*
    This is used switch cameras during animation.
    It binds the active camera to the selected markers.
    First select a camera. Then select the marker(s). Then use the function. :kbd:`Ctrl-B`

*Cache*
    This will display the baked *Cache Steps* for the active object.


.. figure:: /images/K_Doc_Timeline_Cache.jpg

   Timline Cache


   *Show Cache*
       Show all enabled types.

   *Softbody*\ , *Particles*\ , *Cloth*\ , *Smoke*\ , *Dynamic Paint*\ , *Rigid Body*\ .

*Only Selected Channels*
    For *Armatures*\ , this will draw the object keyframes, and the keyframes for the active and selected pose bones.

*Show Frame Number Indicator*
    This will draw the current frame or seconds on the *Time Cursor*\ .

*View All*
    Maximize the *Timeline* area based on the Animation Range. :kbd:`home`

*Show Seconds*
    Show time in seconds for the *Timeline* and the the *Time Cursor* based on the FPS. :kbd:`Ctrl-T`


Marker Menu
-----------

Jump to Previous Marker

Jump to Next Marker

Grab/Move Marker
    Grab/Move the selected markers. :kbd:`G`

Rename Marker
    Rename the active marker. :kbd:`Ctrl-M`

Delete Marker
    Delete selected markers. :kbd:`X`

Duplicate Marker to Scene...
    Duplicate the selected markers to another scene.

Duplicate Marker
    Duplicate the selected markers. :kbd:`Shift-D`

Add Marker
    Add marker to the current frame. :kbd:`M`


Frame Menu
----------

*Auto-Keyframing Mode*
    This controls how the Auto Keyframe mode works.
    Only one mode can be used at a time.

   *Add & Replace*
       Add or Replace existing keyframes.

   *Replace*
       Only Replace existing keyframes.


Playback Menu
-------------

- *Audio Scrubbing*
  If your animation has sound,
  this option plays bits of the sound wave while you move the time cursor with LMB or keyboard arrows.
- *Audio Muted*
  Mute the sound from Sequence Editors.
- *AV-sync*
  Play back and sync with audio clock, dropping frames if frame display is too slow.
  See :doc:`Header Controls <animation/editors/timeline#header_controls>` **IV** Synchronize Playback for more info.
- *Frame Dropping*
  Play back dropping frames if frames are too slow.
  See :doc:`Header Controls <animation/editors/timeline#header_controls>` **IV** Synchronize Playback for more info.
- *Clip Editors*
  While playing, updates the *Movie Clip Editor*.
- *Node Editors*
  While playing, updates the Node properties for the *Node Editor*.
- *Sequencer Editors*
  While playing, updates the *Video Sequence Editor*.

.. admonition:: Image Editors
   :class: note

   TODO Not sure what is updated, maybe gif images or, image sequence.

- *Image Editors*
  Todo
- *Property Editors*
  When the animation is playing, this will update the property values in the UI.
- *Animation Editors*
  While playing, updates the *Timeline*\ , *Dope Sheet*\ , *Graph Editor*\ , *Video Sequence Editor*\ .
- *All 3D View Editors*
  While playing, updates the *3D View* and the the *Timeline*\ .
- *Top-Left 3D Editor*
  While playing, updates the *Timeline* if *Animation Editors* and *All 3D View Editors* disabled.


Header Controls
---------------

The Timeline header controls.


.. figure:: /images/K_Doc_Timeline_Header.jpg
   :width: 700px
   :figwidth: 700px

   Timeline header controls.


'''I''' Range Control
_____________________

   Use Preview Range
       This is an alternative range used to preview animations.
       This works for the UI playback, this will not work for rendering an animation.

   Lock Time Cursor to Playback Range
       This limits the *Time Cursor* to the *Playback Range*\ .


'''II''' Frame Control
______________________

   Start Frame
       The start frame of the animation / playback range.

   End Frame
       The end frame of the animation / playback range.

   Current Frame
       The current frame of the animation / playback range.
       Also the position of the *Time Cursor*\ .


'''III''' Player Control
________________________

    These button are used to set, play, rewind, the *Time Cursor*\ .


.. figure:: /images/K_Doc_Timeline_Player_Controls.jpg

   Player Controls.


   *Jump to start*
       This sets the cursor to the start of frame range. :kbd:`shift-ctrl-Arrow Down` or :kbd:`shift-Arrow Left`

   *Jump to previous keyframe*
       This sets the cursor to the previous keyframe. :kbd:`Arrow Down`

   *Rewind*
       This plays the animation sequence in reverse. :kbd:`shift-alt-A`
       When playing the play buttons switch to a pause button.

   *Play*
       This plays the animation sequence. :kbd:`alt-A`
       When playing the play buttons switch to a pause button.

   *Jump to next keyframe*
       This sets the cursor to the next keyframe. :kbd:`Arrow Up`

   *Jump to end*
       This sets the cursor to the end of frame range. :kbd:`shift-ctrl-Arrow Up` or :kbd:`shift-Arrow Right`

   *Pause*
       This stops the animation. :kbd:`alt-A`


'''IV''' Synchronize Playback
_____________________________

.. figure:: /images/Doc_Animation_Red_FPS.jpg

   3D View Red FPS.
   60:54.75


   When you play an animation, the FPS is displayed at the top left of the 3D View.
   If the scene is detailed and playback is slower than the set :doc:`Frame Rate <render/output/video#dimensions_presets>`\ , these options are used to synchronize the playback.

   *No Sync*
       Do not sync, play every frame.

   *Frame Dropping*
       Drop frames if playback is too slow.
       This enables *Frame Dropping* from the *Playback Menu*\ .

   *AV-sync*
       Sync to audio clock, dropping frames if playback is slow.
       This enables *AV-sync* and *Frame Dropping* from the *Playback Menu*\ .


'''V''' Keyframe Control
________________________

.. figure:: /images/Doc_kia_Cube03.jpg

   Timeline Auto Keyframe.


   *Auto Keyframe*
       The "Record" red-dot button enables something called *Auto Keyframe*\ : It will add and/or replace existing keyframes for the active object when you transform it in the 3D view.

       For example, when enabled, first set the *Time Cursor* to the desired frame, then move an object in the 3d view, or set a new value for a property in the UI.

       When you set a new value for the properties, blender will add keyframes on the current frame for the transform properties.

      *Auto Keying Set* - Optional if Auto Keyframe enabled.
          *Auto Keyframe* will insert new keyframes for the properties in the active *Keying Set*\ .

      Note that *Auto Keyframe* only works for transform properties (objects and bones), in the 3D views (i.e. you cant use it e.g. to animate the colors of a material in the Properties window…).


.. admonition:: Layered
   :class: note

   Todo.


.. figure:: /images/Doc_Animation_Timeline_Layered.jpg

   Timeline Layered.


      *Layered* - Optional while playback.
          // Todo.


.. figure:: /images/Doc_kia_Cube02.jpg

   Timeline Keying Sets.


   *Active Keying Set*
       *Keying Sets* are a set of keyframe channels in one.

       They are made so the user can record multiple properties at the same time.

       With a keying set selected, when you insert a keyframe, blender will add keyframes for the properties in the active *Keying Set*\ .

       There are some built in keying sets, 'LocRotScale', and also custom keying sets.

       Custom keying sets can be defined in the in the panels *Properties > Scene > Keying Sets + Active Keying Set*\ .

   Insert Keyframes
       Insert keyframes on the current frame for the properties in the active *Keying Set*\ .

   Delete Keyframes
       Delete keyframes on the current frame for the properties in the active *Keying Set*\ .


User Preferences
================

Some related user preferences from the **Editing** tab.

*Playback*
      *Allow Negative Frames*
          Time Cursor can be set to negative frames with mouse or keyboard.
          When using *Use Preview Range*\ , this also allows playback.
*Keyframing*
      *Visual Keying*
          When an object is using constraints, the objects property value doesnt actually change.
          *Visual Keying* will add keyframes to the object property, with a value based on the visual transformation from the constraint.
      *Only Insert Needed*
          This will only insert keyframes if the value of the propery is different.
      *Auto Keyframing*
          Enable *Auto Keyframe* by default for new scenes.
      *Show Auto Keying Warning*
          Displays a warning at the top right of the *3D View*\ , when moving objects, if *Auto Keyframe* is on.
      *Only Insert Available*
          With *Auto Keyframe* enabled, this will only add keyframes to channel F-Curves that already exist.



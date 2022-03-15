
**********
Navigation
**********

.. figure:: /images/editors_preferences_section_navigation.png

   Blender Preferences navigation section.


.. _prefs-input-orbit-style:

Orbit & Pan
===========

Orbit Method
   Choose you are preferred method of interactively rotating the 3D Viewport.

   Turntable
      Rotates the view keeping the horizon horizontal.

      This behaves like a potter's wheel or record player where you have two axes of rotation available,
      and the world seems to have a better definition of what is "Up" and "Down" in it.

      The drawback to using the *Turntable* style is that you lose some flexibility when working with your objects.
      However, you gain the sense of "Up" and "Down" which can help if you are feeling disoriented.
   Trackball
      Is less restrictive, allowing any orientation.

Orbit Sensitivity
   Adjusts the reactivity/speed of orbiting in the 3D Viewport.
   This setting works differently depending on what *Orbit Method* is used:

   - Turntable: *Orbit Sensitivity* controls the amount
     of rotation per-pixel to control how fast the 3D Viewport rotates.
   - Trackball: *Orbit Sensitivity* as a simple factor for how fast the 3D Viewport rotates.

.. _prefs-navigation-orbit_around_selection:

Orbit Around Selection
   The selection center becomes the rotation center of the viewport.
   When there is no selection the last selection will be used.

   This uses the selected object (bounding box center), in Object Mode and
   select elements in edit/pose modes.

   .. note::

      While this may seem like ideal behavior,
      it can be inconvenient for larger objects such as a terrain mesh,
      where the center is not necessarily a point of interest.


Auto
   .. _prefs-navigation-auto_depth:

   Perspective
      When enabled, the view switches to perspective when orbiting the view,
      setting axis views (Top, Side, Front, Back, etc.), sets the view to orthographic.

      When disabled, orthographic/perspective mode needs to be changed manually.

   .. _prefs-navigation-auto_perspective:

   Auto Depth
      Use the depth under the mouse to improve view pan, rotate, zoom functionality.
      Useful in combination with *Zoom To Mouse Position*.

Smooth View
   Time (in milliseconds) the animation takes when changing views
   (Top/Side/Front/Camera...). Reduce to zero to remove the animation.

.. _prefs-navigation-rotation_angle:

Rotation Angle
   Rotation step size in degrees, when :kbd:`Numpad4`, :kbd:`Numpad6`, :kbd:`Numpad8`,
   or :kbd:`Numpad2` are used to rotate the 3D Viewport.


Zoom
====

Zoom Method
   Choose your preferred style of zooming in and out,
   when using interactive zoom.

   Scale
      *Scale* zooming depends on where you first click in the view.
      To zoom out, move the cursor to the area center.
      To zoom in, move the cursor away from the area center.
   Continue
      The *Continue* zooming option allows you to control the speed
      (and not the value) of zooming by moving away from the initial cursor position.

      Moving up from the initial click point or to the right will zoom out,
      moving down or to the left will zoom in. The further away you move,
      the faster the zoom movement will be.
      The directions can be altered by the *Vertical* and *Horizontal* radio buttons and
      the *Invert Zoom Direction* option.
   Dolly
      *Dolly* zooming works similarly to *Continue* zooming except that zoom speed is constant.

Zoom Axis
   The axis of the mouse to use for zooming.

   Vertical
      Moving up zooms out and moving down zooms in.
   Horizontal
      Moving left zooms in and moving right zooms out.

.. _prefs-zoom-mouse-pos:

Zoom to Mouse Position
   When enabled, the mouse pointer position becomes the focus point of zooming instead of the 2D window center.
   Helpful to avoid panning if you are frequently zooming in and out.

   .. tip::

      This is useful in combination with :ref:`Auto Depth <prefs-navigation-auto_depth>`
      to quickly zoom into the point under the cursor.

Invert Zoom Direction
   Mouse
      Inverts the Zoom direction for *Dolly* and *Continue* zooming.
   Wheel
      Inverts the direction of the mouse wheel zoom.


Fly & Walk
==========

View Navigation
   The default mode for interactive first person navigation.

   See :ref:`3dview-fly-walk`.


Walk
----

Reverse Mouse
   Inverts the mouse's Y movement.
Mouse Sensitivity
   Speed factor for when looking around, high values mean faster mouse movement.
Teleport Duration
   Interval of time warp when teleporting in navigation mode.
Walk Speed
   Base speed for walking and flying.
Speed Factor
   The multiplication factor for the speed boost.


Gravity
-------

Simulates the effect of gravity when walking.

View Height
   The distance from the ground floor to the camera when walking.
Jump Height
   The maximum height of a jump.

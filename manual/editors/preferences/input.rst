.. _bpy.types.PreferencesInput:

*****
Input
*****

In the Input preferences, you can customize how Blender reacts to the mouse and keyboard
as well as define your own keymap.

.. figure:: /images/editors_preferences_section_input.png


Keyboard
========

Emulate Numpad
   The Numpad keys are used quite often in Blender and are not assigned to the same action as
   the regular number keys. If you have a keyboard without a Numpad (e.g. on a laptop),
   you can tell Blender to treat the standard number keys as Numpad keys by checking *Emulate Numpad*.
Default to Advanced Numeric Input
   For transform mode, default to :ref:`transform-numeric-input-advanced`,
   otherwise :ref:`transform-numeric-input-simple` is used.


Mouse
=====

.. _preferences-input-emulate-mouse:

Emulate 3 Button Mouse
   Blender can be configured to work with pointing devices which do not have an :kbd:`MMB`.
   The functionality of the three mouse buttons by holding :kbd:`Alt-LMB`.

   Mouse/Keyboard combinations referenced in this manual
   can be expressed with the combinations shown in the table. For example:

   :kbd:`MMB` drag becomes :kbd:`Alt-LMB` drag for example.

   .. warning::

      This option prevents certain features from being accessed,
      since :kbd:`Alt-LMB` is used for some operations.

      - Modifying multiple items values at once (objects, bones... etc).
      - Deselecting edge/face rings in Edit Mode.
      - Detaching node links.
      - Moving the Compositor background image.

      Some touchpads support three-finger tap for middle mouse button,
      which may be an alternative to using this option.

   Modifier *(unsupported on Microsoft Windows)*
      :kbd:`Alt`
         Use the :kbd:`Alt` key to emulate the middle mouse button.
      :kbd:`OSKey`
         Use the :kbd:`OSKey` to emulate the middle mouse button.

         This has the advantage that it doesn't conflict with existing :kbd:`Alt-MMB` shortcuts,
         noted above.

Continuous Grab
   This feature is used to prevent the problem where an action such as moving objects or panning a view,
   is limited by your screen bounds.

   This is done by warping the mouse within the view.

   .. note::

      Cursor warping is only supported by *relative* input devices (mouse, trackball, trackpad).

      Graphics tablets, however, typically use *absolute* positioning,
      this feature is disabled when a tablet is being used.

      This is detected for each action,
      so the presence of a tablet will not disable *Continuous Grab* for mouse cursor input.

Release Confirms
   Dragging :kbd:`LMB` on an object will move it.
   To confirm this (and other) transform, an :kbd:`LMB` is necessary by default.
   When this option is activated, the release of :kbd:`LMB` acts as confirmation of the transform.
Mouse Drag Threshold
   The number of pixels that a User Interface element has to be moved before it is recognized by Blender,
   values below this will be detected as click events.
Tablet Drag Threshold
   The drag threshold for tablet events.
Drag Threshold
   The drag threshold for non mouse/tablet events (keyboard or :term:`NDOF` for example).

   This affects :ref:`Pie Menu on Drag <keymap-pref-py_menu_on_drag>` keymap preference.
Motion Threshold
   The number of pixels the cursor must be moved before the movement is registered.
   This is helpful for tablet pens that are a lot more difficult to keep still,
   then this could help to reduce stuttering of the cursor position.

   .. note::

      Unlike the click/drag distinction, this is used to detect small movements
      for example, picking selection cycles through elements near the cursor.
      Once the cursor moves past this threshold, selection stops cycling and picks the closest item.


Tablet
======

Tablet API (Windows only)
   Select the native Windows Ink or older Wintab system for pressure sensitivity.
   Blender automatically selects the API for your operating system and tablet,
   however in case of problems this can be set manually.
   You may need to restart Blender for changes to take affect.
Max Threshold
   Amount of pressure required to achieve full intensity.
Softness
   Controls how the softness of the low pressure response onset using a gamma curve.


.. _editors_preferences_input_ndof:

NDOF
====

These preferences control how an :ref:`NDOF device <hardware-ndof>` interacts with the 3D Viewport.
These preferences can also be accessed using the :kbd:`NDOFMenu` button on the NDOF device
to open a pop-up menu to adjust the settings directly from the 3D Viewport.

Pan Sensitivity
   The overall sensitivity for panning in the 3D Viewport.
Orbit Sensitivity
   The overall sensitivity for orbiting in the 3D Viewport.
Deadzone
   The threshold for the amount of movement needed from
   the device's rest position for Blender to interrupt that movement.

Navigation
   Navigation style for the viewport.

   Free
      Uses the full 6-degrees of freedom.
   Orbit
      Orbit about the view center.

Rotation
   Rotation style for the viewport.

   Turntable
      Rotates the view keeping the horizon horizontal.
   Trackball
      Is less restrictive, allowing any orientation.

Show Navigation Guide
   Display the pivot point and axis during rotation.
Invert Zoom
   Zoom using opposite direction.
Swap Y and Z Axes
   Pan using up/down on the NDOF devices instead of forward/backwards.
Invert Axis Pan
   Reverses the panning axis on the selected axes.
Orbit
   Reverses the orbit axis on the selected axes.
Fly/Walk
   Settings to control how the NDOF device is used while using :ref:`Walk/Fly Navigation <3dview-fly-walk>`.

   Lock Horizon
      Keeps the horizontal axis level file flying.
   Helicopter Mode
      Moves the 3D Viewport up or down when moving the NDOF device up/down.

.. _3dview-fly-walk:

*******************
Fly/Walk Navigation
*******************

There are cases where it's preferable to navigate with first person controls,
especially for large environments such as architectural models.
In these cases orbiting around the view center is limiting.
While zoom, pan and dolly can be used, it's inconvenient.

With walk/fly navigation you can navigate around the scene where view rotation is
performed from the cameras location.

.. figure:: /images/editors_3dview_navigate_walk-fly_view-navigation-panel.png

   View Navigation.

In the :doc:`Preferences editor </editors/preferences/navigation>`
select the navigation method you want to use as default when invoking the View Navigation operator.
Alternatively you can call the individual methods from the :menuselection:`View --> Navigation` menu.

Common use cases for walk/fly include:

Navigation
   This can be a quick way to navigate a large scene.
Camera Placement
   When activated from a camera view, this will move the camera too.
Recording Animation
   Running from a camera with auto-keyframe and playing animation
   will record the motion as you make it allowing you to record the walk-through.


.. _bpy.types.WalkNavigation:

Walk Navigation
===============

.. reference::

   :Mode:      All modes
   :Shortcut:  :kbd:`Shift-AccentGrave`
   :Menu:      :menuselection:`View --> Navigation --> Walk Navigation`

On activation the mouse pointer will move at the center of the view,
and a cross marker will appear...

This navigation method behaves similar to the first person navigation system available in most 3D world games.
It works with a combination of keyboard arrow keys and mouse movement.


Usage
-----

Move the mouse in the direction you want to look and use the following hotkeys to walk around the scene.

When you are happy with the new view, press :kbd:`LMB` to confirm.
In case you want to go back from where you started, press :kbd:`Esc` or :kbd:`RMB`, as usual.

If the defaults values (speed, mouse sensitivity, etc...) need adjustments for your project,
in the :doc:`Preferences </editors/preferences/index>`.

.. list-table::
   :widths: 10 90

   * - :kbd:`W`/:kbd:`Up`
     - Move forward.
   * - :kbd:`S`/:kbd:`Down`
     - Move backward.
   * - :kbd:`A`/:kbd:`Left`
     - Strafe left.
   * - :kbd:`D`/:kbd:`Right`
     - Strafe right.
   * - :kbd:`E`
     - Move up -- only available if *Gravity* off.
   * - :kbd:`Q`
     - Move down -- only available if *Gravity* off.
   * - :kbd:`Spacebar`
     - Teleport location at the cross-hair
       (offset by the *Camera Height* value set in the :doc:`Preferences </editors/preferences/index>`).
   * - :kbd:`WheelUp`/:kbd:`NumpadPlus`
     - Increase the movement speed for this open session.
   * - :kbd:`WheelDown`/:kbd:`NumpadMinus`
     - Decrease the movement speed for this open session.
   * - :kbd:`Shift`
     - Speed up the movement temporarily.
   * - :kbd:`Alt`
     - Slow down the movement temporarily.
   * - :kbd:`V`
     - Jump -- only available if *Gravity* is on.
   * - :kbd:`Tab`
     - Toggle *Gravity*.


Fly Navigation
==============

.. reference::

   :Mode:      All modes
   :Shortcut:  :kbd:`Shift-AccentGrave`
   :Menu:      :menuselection:`View --> Navigation --> Fly Navigation`

On activation the cursor is centered inside a rectangle that defines a safe region.
When the cursor is outside this region the view will rotate/pan.


Usage
-----

Move the mouse outside the safe region in the direction you want to look.

Click :kbd:`LMB` or press :kbd:`Spacebar` to keep the current view and exit fly navigation.
In case you want to go back from where you started, press :kbd:`Esc` or :kbd:`RMB`.

.. list-table::
   :widths: 10 90

   * - :kbd:`W`/:kbd:`Up`
     - Accelerate forward.
   * - :kbd:`S`/:kbd:`Down`
     - Accelerate backwards.
   * - :kbd:`A`/:kbd:`Left`
     - Accelerate left.
   * - :kbd:`D`/:kbd:`Right`
     - Accelerate right.
   * - :kbd:`E`
     - Move up -- only available if *Gravity* off.
   * - :kbd:`Q`
     - Move down -- only available if *Gravity* off.
   * - :kbd:`MMB`
     - Drag to pan the view.
       In this case the view can move laterally on its local axis at the moment you drag the mouse.
   * - :kbd:`WheelUp`/:kbd:`NumpadPlus`
     - Increase the acceleration in the direction of motion,
       if there is no motion, start accelerating forward.
   * - :kbd:`WheelDown`/:kbd:`NumpadMinus`
     - Decrease the acceleration in the direction of motion,
       if there is no motion, start accelerating backward.
   * - :kbd:`Alt`
     - Precision (slow the momentum).
   * - :kbd:`Ctrl`
     - Disable rotation -- while held, the view rotation doesn't influence the flight direction,
       this allows you to fly past an object, keeping it centered in the view,
       even as you fly away from it.

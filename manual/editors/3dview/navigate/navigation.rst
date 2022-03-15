
**********
Navigation
**********


.. _bpy.ops.view3d.view_orbit:

Orbit
=====

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Orbit`
   :Shortcut:  :kbd:`MMB`, :kbd:`Numpad2`, :kbd:`Numpad4`, :kbd:`Numpad6`,
               :kbd:`Numpad8`, :kbd:`Ctrl-Alt-Wheel`, :kbd:`Shift-Alt-Wheel`

Rotate the view around the point of interest.
Click and drag :kbd:`MMB` on the viewport's area.
If you start in the middle of the area and move up and down or left and right,
the view is rotated around the middle of the area.

Holding :kbd:`Alt` while dragging locks to axes.

To change the viewing angle in discrete steps, use :kbd:`Numpad8` and :kbd:`Numpad2`
or use :kbd:`Numpad4` and :kbd:`Numpad6`
to rotate the scene around the global Z axis from your current point of view.
Finally :kbd:`Numpad9` switches to the opposite side of the view.

.. seealso::

   - :ref:`Orbit Style Preference <prefs-input-orbit-style>`
   - :ref:`Auto-Perspective Preference <prefs-navigation-auto_perspective>`


Roll
====

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Roll`
   :Shortcut:  :kbd:`Shift-Numpad4`, :kbd:`Shift-Numpad6`

Rotate the viewport camera around its local Z axis in 15° discrete steps by default,
see :ref:`rotation angle <prefs-navigation-rotation_angle>` preference to configure.


.. _bpy.ops.view3d.view_pan:

Pan
===

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Pan`
   :Shortcut:  :kbd:`Shift-MMB`, :kbd:`Ctrl-Numpad2`, :kbd:`Ctrl-Numpad4`,
               :kbd:`Ctrl-Numpad6`, :kbd:`Ctrl-Numpad8`

Moves the view up, down, left and right.
To pan the view, hold down :kbd:`Shift` and drag :kbd:`MMB` in the 3D Viewport.
For discrete steps, use the hotkeys :kbd:`Ctrl-Numpad8`, :kbd:`Ctrl-Numpad2`,
:kbd:`Ctrl-Numpad4` and :kbd:`Ctrl-Numpad6` as with orbiting
(note: you can replace :kbd:`Ctrl` with :kbd:`Shift`).


.. _bpy.ops.view3d.zoom:
.. _editors_3dview_navigation_zoom:

Zoom In/Out
===========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Zoom In/Out`
   :Shortcut:  :kbd:`Ctrl-MMB`, :kbd:`Wheel`, :kbd:`NumpadPlus`, :kbd:`NumpadMinus`

Moves the camera forwards and backwards.
You can zoom in and out by holding down :kbd:`Ctrl` and dragging :kbd:`MMB`.
To zoom in with discrete steps, use the hotkeys :kbd:`NumpadPlus` and :kbd:`NumpadMinus`.
If you have a wheel mouse, you can zoom by rotating the :kbd:`Wheel`.

.. hint:: If You Get Lost

   If you get lost in 3D space, which is not uncommon, two hotkeys will help you:
   :kbd:`Home` changes the view so that you can see all objects :menuselection:`View --> Frame All`,
   while :kbd:`NumpadPeriod` zooms the view to the currently selected objects
   when in perspective mode :menuselection:`View --> Frame Selected`.


.. _3dview-nav-zoom-region:

Zoom Region
===========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Zoom Region...`
   :Shortcut:  :kbd:`Shift-B`

The *Zoom Region* tool allows you to specify a rectangular region and zoom in
so that the region fills the 3D Viewport.

You can access this through via the shortcut :kbd:`Shift-B`,
then :kbd:`LMB` click and drag a rectangle to zoom into.

Alternatively you can zoom out using the :kbd:`MMB`.


.. _3dview-nav-zoom-dolly:

Dolly Zoom
==========

.. reference::

   :Mode:      All modes
   :Shortcut:  :kbd:`Shift-Ctrl-MMB`

In most cases its sufficient to zoom the view to get a closer look at something,
however, you may notice that at a certain point you cannot zoom any closer.

This is because Blender stores a view-point that is used for orbiting and zooming.
It works well in many cases, but sometimes you want to move the view-point to a different place.
This is what Dolly supports, allowing you to transport the view from one place to another.

You can dolly back and forth by holding down :kbd:`Shift-Ctrl` and dragging with :kbd:`MMB`.

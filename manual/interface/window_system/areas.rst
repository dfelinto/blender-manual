.. _bpy.types.Area:
.. _bpy.types.AreaSpaces:

*****
Areas
*****

.. figure:: /images/interface_window-system_areas_borders.png
   :align: right
   :width: 250px
   :figwidth: 250px

   Area boundaries are indicated by rounded corners (yellow highlights).

The Blender window is divided up into a number of rectangles called Areas.
Areas reserve screen space for :doc:`/editors/index`, such as the 3D Viewport, or the Outliner.
In general an Editor provides a way to view and modify your work through a specific part of Blender.
All hotkeys you press will affect the contents of the Editor in the Area the mouse pointer is located.
Area boundaries are indicated by rounded (beveled) corners.

Areas can be customized to match specific tasks called
:doc:`Workspaces </interface/window_system/workspaces>`,
which can then be named and saved for later use.


Resizing
========

.. figure:: /images/interface_window-system_areas_resize.png
   :align: right
   :width: 250px
   :figwidth: 250px

You can resize areas by dragging their borders with :kbd:`LMB`.
Move your mouse cursor over the border between two areas,
so that the cursor changes to a double-headed arrow, and then click and drag.


Splitting
=========

.. figure:: /images/interface_window-system_areas_split.png
   :align: right
   :width: 250px
   :figwidth: 250px

Splitting an area will create a new area. Placing the mouse cursor
in an area corner will change the cursor to a cross (+) to indicate that
pressing down :kbd:`LMB` will activate splitting or joining operator.
Dragging from area corner **inward** will *split* the area.
You define the split direction by dragging either horizontally or vertically.


Joining
=======

.. figure:: /images/interface_window-system_areas_join.png
   :align: right
   :width: 250px
   :figwidth: 250px

   Properties is being joined to the Outliner.

Dragging from an area corner **outward** will *join* two areas.
The area that will be closed shows a dark overlay.
You can select which area will be closed by moving the mouse over areas.
Release the :kbd:`LMB` to complete the join.
If you press :kbd:`Esc` or :kbd:`RMB` before releasing the mouse,
the operation will be canceled.


Area Options
^^^^^^^^^^^^

:kbd:`RMB` on the border opens the *Area Options*.

Vertical/Horizontal Split
   Shows an indicator line that lets you select the area and position where to split.
   :kbd:`Tab` switches between vertical/horizontal.
Join Areas
   Shows the join direction overlay.
Swap Areas
   Swaps this area with the adjacente one.


Swapping Contents
-----------------

You can swap the contents between two areas with :kbd:`Ctrl-LMB`
on one of the corners of the initial area, dragging towards the target area,
and releasing the mouse there. The two areas do not need to be side-by-side,
though they must be inside the same window.


.. _bpy.ops.screen.area_dupli:

Duplicate Area into new Window
==============================

.. reference::

   :Menu:      :menuselection:`View --> Area --> Duplicate Area into new Window`

A new floating window containing an area can be created from
:menuselection:`View --> Area --> Duplicate Area into new Window`. (Not available in some editors.)

The new window is a fully functional window, which is part of the same instance of Blender.
This can be useful, e.g. if you have multiple monitors.

You can also create a new window from an existing area by :kbd:`Shift-LMB`
on the area corner, then drag outward slightly.

The window can be closed with the OS *Close Window* button.


.. _bpy.ops.screen.screen_full_area:

Toggle Maximize Area
====================

.. reference::

   :Menu:      :menuselection:`View --> Area --> Toggle Maximize Area`
   :Shortcut:  :kbd:`Ctrl-Spacebar`

The maximized area fill the whole application window. You can maximize an area
with :menuselection:`View --> Area --> Toggle Maximize Area` menu entry or keyboard shortcut.
To return to normal size, use the keyboard shortcut again or the *Back to Previous* button on the Topbar.

.. note::

   The area your mouse is currently hovering over is the one
   that will be maximized using the keyboard shortcuts.


Toggle Fullscreen Area
======================

.. reference::

   :Menu:      :menuselection:`View --> Area --> Toggle Fullscreen Area`
   :Shortcut:  :kbd:`Ctrl-Alt-Spacebar`

The fullscreen area contains only the main region of the editor.
To exit fullscreen use the keyboard shortcut or move the mouse to the top right corner
of the area to reveal the return icon.

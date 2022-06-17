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

The Blender window is divided into a number of rectangles called Areas.
Areas reserve screen space for :doc:`/editors/index`, such as the
:doc:`3D Viewport </editors/3dview/introduction>` or the
:doc:`Outliner </editors/outliner/introduction>`.
Each editor offers a specific piece of functionality.

Areas are grouped into :doc:`Workspaces </interface/window_system/workspaces>`,
which are geared towards particular tasks (modeling, animating and so on).

.. note::
   While some keyboard shortcuts in Blender are global (such as :kbd:`Ctrl-S`
   for saving), many depend on which editor the mouse cursor is hovering over.

   As an example, say you just selected two objects in the Outliner and want
   to join them. If you pressed the shortcut for this (:kbd:`Ctrl-J`)
   while the cursor is still in the Outliner, nothing would happen as the
   shortcut isn't valid there; you first need to move your cursor
   to the 3D Viewport.


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
pressing down :kbd:`LMB` will activate splitting or joining.
Dragging from an area corner **inward** will *split* the area.
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
You can select which area will be closed by moving the mouse over it.
Release the :kbd:`LMB` to complete the join.
If you press :kbd:`Esc` or :kbd:`RMB` before releasing the mouse,
the operation will be canceled.

.. tip::

   The cursor will also turn into a cross when hovering over either
   end of the border between two areas. When splitting or joining,
   it's best not to start dragging from this border, but from a
   corner inside one of the areas.


Area Options
^^^^^^^^^^^^

:kbd:`RMB` on the border opens the *Area Options*.

Vertical/Horizontal Split
   Shows an indicator line that lets you select the area and position where to split.
   :kbd:`Tab` switches between vertical/horizontal.
Join Areas
   Shows the join direction overlay.
Swap Areas
   Swaps this area with the adjacent one.


Swapping Contents
-----------------

You can swap the contents of two areas by pressing :kbd:`Ctrl-LMB`
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

You can also create a new window from an existing area by pressing :kbd:`Shift-LMB`
on an area corner, then dragging outward slightly.


.. _bpy.ops.screen.screen_full_area:

Toggle Maximize Area
====================

.. reference::

   :Menu:      :menuselection:`View --> Area --> Toggle Maximize Area`
   :Shortcut:  :kbd:`Ctrl-Spacebar`

Expands the Area so it fills the whole window (while keeping the Topbar and Status Bar visible).
To return to normal size, use the keyboard shortcut again or click the *Back to Previous* button in the Topbar.


Toggle Fullscreen Area
======================

.. reference::

   :Menu:      :menuselection:`View --> Area --> Toggle Fullscreen Area`
   :Shortcut:  :kbd:`Ctrl-Alt-Spacebar`

Expands the Area so it fills the whole window, hiding the Topbar, Status Bar, and even the
secondary :doc:`regions </interface/window_system/regions>` (toolbars etc.) of the Area's own editor.
To return to normal size, use the keyboard shortcut again or click the icon in the Area's top right corner
(only becomes visible when hovering).

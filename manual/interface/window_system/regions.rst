.. _bpy.types.Region:
.. _ui-region:

*******
Regions
*******

Every Editor in Blender is divided into Regions.
Regions can have smaller structuring elements like
:doc:`tabs and panels </interface/window_system/tabs_panels>`
with buttons, controls and widgets placed within them.

.. figure:: /images/interface_window-system_regions_3d-view.png
   :align: center

   The regions of the 3D Viewport showing the Sidebar and
   the Adjust Last Operation panel after adding a Cube.

   Header (green), Main region (yellow), Toolbar (blue),
   Sidebar (red) and Adjust Last Operation panel (pink).


.. _ui-region-window:

Main Region
===========

At least one region is always visible.
It is called the Main region and is the most prominent part of the editor.

Each editor has a specific purpose, so the main region and
the availability of additional regions are different between editors.
See specific documentation about each editor in the :doc:`Editors </editors/index>` chapter.


.. _ui-region-header:
.. _bpy.types.Header:

Header
======

A header is a small horizontal strip, which sits either at the top or bottom of an area.
All editors have a header acting as a container for menus and commonly used tools.
:ref:`Menus <ui-header-menu>` and buttons will change with the editor type and
the selected object and mode.

.. figure:: /images/editors_3dview_introduction_3d-view-header-object-mode.png

   The Header of the 3D Viewport.


.. _bpy.ops.screen.header:

Context Menu
------------

:kbd:`RMB` on a header reveals a context menu with a couple options:

Show Header
   Toggles the visibility of the header.
   If a header is hidden it can be made visible again by dragging
   the small arrow that appears at the top/bottom right of the editor.
Show Tool Settings
   Toggles the visibility of the `Tool Settings`_.
Show Menus
   Toggles whether the :ref:`Menus <ui-header-menu>` are collapsed or not.
Flip to Bottom/Top
   Toggles whether the header or Tool Settings appear on the top or bottom of the editor.
Maximize Area
   See :ref:`bpy.ops.screen.screen_full_area`.


Toolbar
=======

The *Toolbar* (on the left side of the editor area) contains a set of interactive tools.
:kbd:`T` toggles the visibility of the Toolbar.

This is further documented here: :ref:`Toolbar <ui-region-toolbar>`.


Tool Settings
=============

The *Tool Settings* (at the top/bottom of the editor area)
contains as its name suggests the settings of the active tool.
It's visibility can be toggled with the header's context menu just as its position
with the *Flip to Bottom/Top* operator.


Adjust Last Operation
=====================

The *Adjust Last Operation* is a region that shows tool options when tools (operators) are run.

This is further documented here: :ref:`Adjust Last Operation <ui-undo-redo-adjust-last-operation>`.


.. _ui-region-sidebar:

Sidebar
=======

The *Sidebar* (on the right side of the editor area)
contains :ref:`Panels <ui-panels>`
with settings of objects within the editor and the editor itself.
:kbd:`N` toggles the visibility of the Sidebar.


Footer
======

Some editors show a bar (on top/bottom of the editor area)
that displays information about for example the active tool.


Arranging
=========

Scrolling
---------

A region can be scrolled vertically and/or horizontally by dragging it with the :kbd:`MMB`.
If the region has no zoom level, it can be scrolled by using the :kbd:`Wheel`,
while the mouse hovers over it.


Changing the Size and Hiding
----------------------------

Resizing regions works by dragging their border, the same way as
:doc:`/interface/window_system/areas`.

To hide a region resize it down to nothing.
A hidden region leaves a little arrow sign.
:kbd:`LMB` on this icon to make the region reappear.

.. list-table:: Hiding and showing the Sidebar.

   * - .. figure:: /images/interface_window-system_regions_sidebar-hide.png

     - .. figure:: /images/interface_window-system_regions_sidebar-show.png

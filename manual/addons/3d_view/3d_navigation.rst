
*************
3D Navigation
*************

This custom menu is in part a virtual numpad emulator and a user perspective navigation tool.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click 3D View then 3D Navigation to enable the script.


Interface
=========

Located in the :menuselection:`3D Viewport --> Sidebar --> View`.
This add-on is split over two panels.


3D Navigation
-------------

.. figure:: /images/addons_3d-view_3d-navigation_panel1.jpg
   :align: right
   :width: 220px

This panel provides some common navigation tools and emulates the numpad hotkeys.

View Global/Local
    Switch Global/Local view.
View Perspective/Orthographic
   Switch perspective/orthographic view mode.
View Camera
   View from active camera.

Align View from
   Front/Back
      Align view to front/back.

   Left/Right
      Align view to left/right.

   Top/Bottom
      Align view to top/bottom.

Lock View to Object
   Select an object to align view, from the list.

View to Select
   Align view on selected object.

Cursor
   World Origin
      Snap cursor to center (scene 0,0,0).
   View
      Align view to center (scene 0,0,0).
   Cursor to Selected
      Snap cursor to object center (selected).


Pan Orbit Zoom Roll
-------------------

.. figure:: /images/addons_3d-view_3d-navigation_panel2.jpg
   :align: right
   :width: 220px

This panel provides incremental "User Screen View Perspective" navigation in the Sidebar.

Up
   Move towards the top of your screen.

Down
   Move towards the bottom of your screen.

Left
   Move to the users left or left of screen as you view it.

Right
   Move to the users right or right of screen as you view it.

Zoom In/Out
   Zoom the view in/out.

Roll Left/Right
   Roll the view left/right.

.. admonition:: Reference
   :class: refbox

   :Category:  3D View
   :Description: Navigate the 3D Viewport and camera from the Sidebar.
   :Location: :menuselection:`3D Viewport --> Sidebar --> View tab`
   :File: space_view3d_3d_navigation.py
   :Author: Demohero, uriel, meta-androcto
   :Maintainer: Brendon Murphy (meta-androcto)
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.

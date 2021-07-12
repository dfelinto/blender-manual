
************
Stored Views
************

Stored Views has three modes of operation, depending on which the following are saved or restored.
Save stored views to your blend-file to easily have access to saved views later.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click 3D View then Stored Views to enable the script.


Interface
=========

Located in the :menuselection:`3D Viewport --> Sidebar --> View tab`.

.. figure:: /images/addons_3d-view_stored-views_ui.jpg
   :align: right
   :width: 220px

View
   Save multiple view locations for easy navigation between views.
POV
   Save Point of View --> Perspective and Local modes.

Camera to View
   Move the selected camera to current view.
New Camera to View
   Create a new camera to current view.
Save Current
   Save the View or :abbr:`POV (Point Of View)`.

Camera Selector
   Tools for camera selection and management.

Camera
   Make the camera active.
Preview Camera
   Make the camera active, selected and *Camera to View* in one button.
Add Camera Marker
   Add a camera marker to help animating between cameras.


Instructions
============

- First activate the user interface and storage by pressing *Initialize*.
- With the *View* button active, Zoom, move or rotate the camera into a position you like.
  (Useful setting up camera locations and modeling specific areas of a mesh.)
- Or with the *POV* button active, change the user perspective or local views.
- Press *Save Current* to create a list of each stored view or point of view.
- You can move selected camera or create a new camera to the stored view.
  (Useful for setting up camera shots to different views.)
- The camera selector works in a similar way. Each camera is listed and
  you can make a camera active by pressing the camera icon.
- You can view each camera pressing the screen icon and also add camera markers using the arrow icon.
  (Useful for setting up camera switching during animations.)

As all stored definitions are saved in the blend-file, you can save the file and
the next time you use it, the stored views or point of view will be ready.

.. reference::

   :Category:  3D View
   :Description: Save and restore user defined views, :abbr:`POV (Point Of View)` and camera locations.
   :Location: :menuselection:`3D Viewport --> Sidebar --> View tab`
   :File: space_view3d_stored_views.py
   :Author: nfloyd, Francesco Siddi
   :Maintainer: Brendon Murphy (meta-androcto)
   :Contributors: ramboblender
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.

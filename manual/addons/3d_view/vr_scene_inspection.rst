
*******************
VR Scene Inspection
*******************

The :abbr:`VR (Virtual Reality)` Scene Inspection add-on exposes and extends
the native virtual reality features of Blender in the user interface.
The feature set is limited to scene inspection use cases.
More advanced use cases may be enabled through further development inside of Blender.

VR support in Blender is based on the OpenXR specification and requires some set up steps.
These are explained in the :ref:`Head-Mounted Displays (HMD) <hardware-head-mounted-displays>` section.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click 3D View then VR Scene Inspection to enable the script.


Interface
=========

Located in the :menuselection:`3D Viewport --> Sidebar --> VR tab`.

.. figure:: /images/addons_3d-view_vr-scene-inspection_example.jpg
   :align: right
   :width: 220px


VR Session
----------

Start VR Session
   Try to set up a connection to the OpenXR platform to share the viewport with
   an :ref:`HMD <hardware-head-mounted-displays>`.
Positional Tracking
   Only track rotational changes of the head, do not allow the HMD to affect the location of
   the viewer in virtual space.


View
----

Floor
   Set visibility of the ground plane in the VR view.
Annotations
   Set visibility of annotation strokes in the VR view.
Clip Start/End
   Clipping values of the VR view, :ref:`as in the 3D Viewport <3dview-view-clip>`.


Landmarks
---------

Landmarks are used to store reusable base poses (position and rotation) for the viewer in the virtual space.

Landmark
   A :ref:`list view <ui-list-view>`.

   Selected Landmark
      Defines which landmark's settings are shown below the list.
      Changing the selected landmark does not have an influence on the VR view.
   Activate (star icon)
      Activates a landmark, making it change the base pose of the VR view.
   Add ``+``
      Create a landmark.
   Remove ``-``
      Deletes the selected landmark.
Type
   Scene Camera
      Follow the :ref:`scene's active camera<scene-camera>` to define the base pose of the viewer.
   Custom Camera
      Set an arbitrary camera to define the base pose of the viewer.


Viewport Feedback
-----------------

Show VR Camera
   Draw an indicator of the current VR viewer pose (location and rotation in the virtual space)
   in the current 3D Viewport.
Mirror VR Session
   Make the current 3D Viewport follow the perspective of the VR view.


.. admonition:: Reference
   :class: refbox

   :Category:  3D View
   :Description: View the viewport with virtual reality glasses (head-mounted displays).
   :Location: :menuselection:`3D Viewport --> Sidebar --> VR tab`
   :File: viewport_vr_preview.py
   :Author: Julian Eisel
   :Maintainer: Julian Eisel
   :License: GPL
   :Support Level: Official
   :Note: This add-on is bundled with Blender.

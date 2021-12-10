
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

.. figure:: /images/addons_3d-view_vr-scene-inspection_interface.jpg
   :width: 220px


VR Session
----------

.. figure:: /images/addons_3d-view_vr-scene-inspection_vr-session.jpg
   :align: right
   :width: 220px

Start VR Session
   Try to set up a connection to the OpenXR platform to share the viewport with
   an :ref:`HMD <hardware-head-mounted-displays>`.
Tracking
   Positional
      Only track rotational changes of the head, do not allow the HMD
      to affect the location of the viewer in virtual space.
   Absolute
      Skip eye offsets that are normally added for placing the viewer
      exactly at landmarks. This allows the tracking origin to be defined
      independently of the HMD position.
Use Controller Actions
   Enable default controller actions for viewport navigation,
   controller tracking, and haptics.


View
----

.. figure:: /images/addons_3d-view_vr-scene-inspection_view.jpg
   :align: right
   :width: 220px

Show
   Floor
      Set visibility of the ground plane in the VR view.
   Annotations
      Set visibility of annotation strokes in the VR view.
   Selection
      Set visibility of selection outlines in the VR view.
   Controllers
      Set visibility of VR motion controllers.
      Requires enabling the `Use Controller Actions <VR Session_>`_ option.
   Custom Overlays
      Set visibility of custom operator drawing (e.g. default teleport beam).
Controller Style
   Preferred visualization of VR motion controllers.
Clip Start/End
   Clipping values of the VR view, :ref:`as in the 3D Viewport <3dview-view-clip>`.


Landmarks
---------

Landmarks are used to store reusable base poses (position and rotation) for the viewer in the virtual space.
In addition, a base viewer reference scale can be set for landmarks of types Custom Object and Custom Pose.

.. figure:: /images/addons_3d-view_vr-scene-inspection_landmarks.jpg
   :align: right
   :width: 220px

Landmark
   A :ref:`list view <ui-list-view>`.

   Selected Landmark
      Defines which landmark's settings are shown below the list.
      Changing the selected landmark does not have an influence on the VR view.
   Activate ``〇``
      Activates a landmark, making it change the base pose of the VR view.
   Add ``+``
      Create a landmark.
   Remove ``-``
      Delete the selected landmark.
   Add from Session ``⊕``
      Create a landmark from the viewer pose of the running VR session.
   Landmark Controls ``v``
      Add Landmark from Camera
         Add a new landmark from the active camera object.
      Update Custom Landmark
         Update the selected landmark from the current VR viewer pose.
      Cursor to Landmark
         Move the 3D Cursor to the selected landmark.
      Scene Camera to Landmark
         Position the scene camera at the selected landmark.
      Camera from Landmark
         Create a new camera from the selected landmark.
Type
   Scene Camera
      Follow the :ref:`scene's active camera<scene-camera>` to define the base pose of the viewer.
   Custom Object
      Set an arbitrary object to define the base pose of the viewer.
   Custom Pose
      Manually define a position and rotation to use as the base pose of the viewer.


Action Maps
-----------

.. figure:: /images/addons_3d-view_vr-scene-inspection_action-maps.jpg
   :align: right
   :width: 220px

Gamepad
   Use input from a gamepad (Microsoft Xbox Controller) instead of motion controllers for
   VR actions such as viewport navigation.
Extensions
   Enable additional controller bindings to ensure correct input-to-action mappings.
   Note that a given extension may not be supported by all
   :ref:`VR platforms <hardware-head-mounted-displays>`.

   HP Reverb G2
      Enable bindings for the HP Reverb G2 controllers.
   HTC Vive Cosmos
      Enable bindings for the HTC Vive Cosmos controllers.
   Huawei
      Enable bindings for the Huawei controllers.


Viewport Feedback
-----------------

.. figure:: /images/addons_3d-view_vr-scene-inspection_viewport-feedback.jpg
   :align: right
   :width: 220px

Show VR Camera
   Draw an indicator of the current VR viewer pose (location and rotation in the virtual space)
   in the current 3D Viewport.
Show VR Controllers
   Draw indicators of tracked VR motion controllers in the current 3D viewport.
   Requires enabling the `Use Controller Actions <VR Session_>`_ option.
Show Landmarks
   Draw `landmark <Landmarks_>`_ indicators in the current 3D Viewport.
Mirror VR Session
   Make the current 3D Viewport follow the perspective of the VR view.


.. reference::

   :Category:  3D View
   :Description: View the viewport with virtual reality glasses (head-mounted displays).
   :Location: :menuselection:`3D Viewport --> Sidebar --> VR tab`
   :File: viewport_vr_preview folder
   :Author: Julian Eisel, Sebastian Koenig, Peter Kim
   :Maintainer: Julian Eisel, Peter Kim
   :License: GPL
   :Support Level: Official
   :Note: This add-on is bundled with Blender.

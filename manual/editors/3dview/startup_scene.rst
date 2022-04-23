
*************
Startup Scene
*************

After closing the splash, the startup scene is displayed in the 3D Viewport
if no other blend-file was loaded. A customized startup scene
can be saved as a part of the :doc:`startup file </getting_started/configuration/defaults>`.

.. figure:: /images/editors_3dview_startup-scene_labels.png

   The Startup scene.


Elements
========

Cube
   The gray cube in the center of the scene is a :doc:`mesh </modeling/meshes/index>` object.
   Because the cube is selected it is displayed with an orange outline.

   Object Origin
      The :doc:`Origin of the object </scene_layout/object/origin>` is displayed as
      an orange dot and it marks the cube's (relative) position.
Light
   The circles with a thin line to the bottom is a light source illuminating the cube.
   Lights in: :doc:`General Settings </render/lights/light_object>`.

Camera
   The pyramid with a big triangle pointing upward is the camera used as point of view for rendering.
   See also: cameras in :doc:`Cycles </render/cameras>`.
3D Cursor
   The :doc:`3D cursor </editors/3dview/3d_cursor>`, a cross with a red-and-white circle,
   is used for placing objects in the scene.
Grid Floor
   The gray squares forming a floor mark the zero height of the world.
   The red and green lines are the axes of the world coordinate system.
   They meet at the origin, which is also the position of the *Cube*.
   The Grid Floor settings are in the :doc:`Viewport Overlays </editors/3dview/display/overlays>` popover.


Text Info
---------

The visibility and settings of the overlays can be set
in the :doc:`Viewport Overlays </editors/3dview/display/overlays>` popover.

View Name
   If the viewport camera is not aligned, the view is named "User" plus
   the perspective of the viewport camera.
Playback Frame Rate (FPS)
   Displays the Frames Per Second screen rate, while playing an animation back.
Object Info
   Shown in brackets is the current frame. Followed by the path of the :ref:`active object <object-active>`.
   And optionally the selected :doc:`shape key </animation/shape_keys/index>` and
   in brackets (<>) the :doc:`/animation/markers` name on the current frame.
   The color of the Object Info is set by the :ref:`animation-state-colors` (keyframe only).

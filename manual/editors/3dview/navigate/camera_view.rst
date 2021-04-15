.. _3dview-camera-navigate:

***********
Camera View
***********

.. figure:: /images/editors_3dview_navigate_camera-view_example.png

   Demonstration of camera view.

The Camera view shows the current scene as seen from the currently active camera's view point.

The Camera view can be used to virtually compose shots and preview how the scene will look when rendered.
The rendered image will contain everything within the dashed line.

.. seealso::

   :doc:`Camera Settings </render/cameras>` for details how camera settings are used for display & rendering.

.. hint::

   The active camera can be selected while in camera view using the camera frame
   *(assuming the object isn't hidden).*


Viewing the Active Camera
=========================

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Cameras --> Active Camera`
   :Shortcut:  :kbd:`Numpad0`

This switches the view to the active camera.
The triangle above the camera will become shaded when active.


Setting the Active Camera
=========================

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`View --> Cameras --> Set Active Object as Camera`
   :Shortcut:  :kbd:`Ctrl-Numpad0`

.. figure:: /images/editors_3dview_navigate_camera-view_cameras.png

   Active camera (left) displayed with a solid triangle above it.

   This is the camera currently used for rendering and when viewing from the camera.

This sets the current active object as the active camera & switches to the camera view.

The active camera can also be set in the *Scene* tab of the *Properties*.

.. note::

   The active camera, as well as the layers, can be specific to a given view,
   or global (locked) to the whole scene.
   See :doc:`Local Camera </editors/3dview/sidebar>`.


Animated Camera Switching
-------------------------

By default a scene contains one camera. However, a scene can contain more than one camera,
but only one of them will be used at a time.
So you will only need to add a new camera if you are making cuts between them.
See :ref:`Animating Cameras <bpy.ops.marker.camera_bind>`.


.. _bpy.ops.view3d.view_center_camera:

Frame Camera Bounds
===================

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`View --> Cameras --> Frame Camera Bounds`
   :Shortcut:  :kbd:`Home`

Centers the camera view inside the 3D Viewport's screen area
and resizes the view to fit within the area's bounds.


Camera Navigation
=================

There are several different ways to navigate and position the camera in your scene,
some of them are explained below.

Zooming in and out is possible in this view, but to change the viewpoint,
you have to move or rotate the camera.

.. hint::

   The active "camera" might be any kind of object.
   So these actions can be used, for example, to position and aim a light.


Move Active Camera to View
--------------------------

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Shortcut:  :kbd:`Ctrl-Alt-Numpad0`

This matches the active camera to a regular (non camera) view,
for a convenient method of placing the camera without having to move the object directly.


Camera View Positioning
-----------------------

By enabling :ref:`Lock Camera to View <3dview-lock-camera-to-view>` in the View panel of the Sidebar region,
while in camera view, you can navigate the 3D Viewport as usual,
while remaining in camera view. Controls are exactly the same as when normally moving in 3D.

.. seealso::

   :ref:`Fly/Walk Navigation <3dview-fly-walk>` for first person navigation that moves the active camera too.


Roll, Pan, Dolly, and Track
---------------------------

To perform these camera moves, the camera must first be *selected* so transform operations apply to it.
The following actions also assume that you are in camera view.
Having done so, you can now manipulate the camera using the same tools that are used to transform any object:

Roll
   Press :kbd:`R` to enter object rotation mode. The default will be to rotate the camera in its local Z axis
   (the axis orthogonal to the camera view), which is the definition of a camera "roll".
Vertical Pan or Pitch
   This is just a rotation along the local X axis. Press :kbd:`R` to enter object rotation mode,
   then :kbd:`X` twice (the first press selects the *global* axis,
   pressing the same letter a second time selects the *local* axis -- this works with any axis;
   see the :doc:`axis locking page </scene_layout/object/editing/transform/control/axis_locking>`).
Horizontal Pan or Yaw
   This corresponds to a rotation around the camera's local Y axis.
   Press :kbd:`R`, and then :kbd:`Y` twice.
Dolly
   To dolly the camera, press :kbd:`G` then :kbd:`MMB` (or :kbd:`Z` twice).
Sideways Tracking
   Press :kbd:`G` and move the mouse (you can use :kbd:`X` twice or :kbd:`Y`
   to get pure-horizontal or pure-vertical sideways tracking).


..    TODO/Review: {{review|text=Options reviewed for v2.70; Video is for old version}} .


Introduction
************

A :guilabel:`Camera` is an object that provides a means of rendering images from Blender.
It defines which portions of a scene is visible at render time.
Scenes can have multiples cameras, but *must* contain, at minimum,
one camera in order to generate any images.


Add a new camera
================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :menuselection:`Add --> Camera`
   | Hotkey:   :kbd:`shift-A` to add new.


In :guilabel:`Object` mode simply press :kbd:`shift-A` and in the popup menu,
choose :menuselection:`Add --> Camera`.


Change active camera
====================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Hotkey:   :kbd:`ctrl-pad0`


.. figure:: /images/Manual-CameraView-ActiveCamera.jpg
   :width: 200px
   :figwidth: 200px

   Active camera (left one).


The *active* camera is the camera that is currently being used for rendering and camera view
(:kbd:`pad0`).
Select the camera you would like to make active and press :kbd:`ctrl-pad0` (by doing so,
you also switch the view to camera view). In order to render,
each scene **must** have a camera.

The active camera is the one with the filled "up" triangle on top seen in the 3D viewport,
for example, the left camera in (*Active camera (left one)*).


 .. warning::

    The active camera, as well as the layers, can be specific to a given view, or global (locked) to the whole scene -
    see :doc:`this part of the 3D view options page </3d_interaction/navigating/3d_view_options#lock_to_scene>`.


Camera Settings
===============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Camera`


Cameras are invisible in renders, so they don't have any material or texture settings.
However, they do have :guilabel:`Object` and :guilabel:`Editing` setting panels available
which are displayed when a camera is the selected (active!) object.

`Camera Lens panel. <http://wiki.blender.org/index.php/File:Manual-CameraPanel-2.57>`__


Lens
----


Perspective / Orthographic / Panoramic
   Select what projection type to use. :guilabel:`Perspective` is the default and makes objects further away
   appear smaller while :guilabel:`Orthographic` maintains the exact measures of objects. A
   :guilabel:`Perspective` projection is more similar to what an image obtained with a real camera would look like
   while an :guilabel:`Orthographic` projection is a more technical view, best for blueprints,
   but worst to convey distances between objects.
   To configure these projections,
   see :doc:`this page </render/camera/perspective>`on vanishing points and isometric view.
   :guilabel:`Panoramic` renders the scene with a cylindrical projection.

   .. figure:: /images/Manual-CameraView-Camera.jpg
      :width: 200px
      :figwidth: 200px

      A camera with the clipping limits and focal point visible.

Focal Length
    Available in Perspective and Panoramic camera types, represents the lens focal length,
    represented in degrees or millimeters. When :guilabel:`Orthographic` mode is selected,
    the :guilabel:`Focal Length` setting changes to the :guilabel:`Orthographic Scale` setting.
    This setting determines the size of the camera's visible area.
Shift X/Y
    Shifts the camera viewport. Note that most of the time,
    this setting should not be used to adjust the camera position,
    as the :guilabel:`Shift` setting is relative to the actual camera position, which will not be changed.
Clipping Start/End
    Sets the clipping limits. Only objects within the limits are rendered.
    If :guilabel:`Limits` in the :guilabel:`Display` panel is enabled,
    the clip bounds will be visible as two yellow connected dots on the camera line of sight.


   .. note::

      The :guilabel:`3D View` window contains settings similar to the camera,
      such as :guilabel:`Orthographic` / :guilabel:`Perspective` and :guilabel:`Clip Start` / :guilabel:`Clip End`.
      These settings have no effect on the camera rendering,
      and only change the view settings when *not* in :guilabel:`Camera` view.
      These settings are accessed through the :menuselection:`View` menu of the :guilabel:`3D View`.

      See the :doc:`3D view options page </3d_interaction/navigating/3d_view_options#view_properties_panel>`
      for more details.


Camera Presets
==============

.. figure:: /images/Manual-Camera-presets-panel.jpg
   :width: 270px
   :figwidth: 270px

   Camera Presets panel.


   ToDo

- :guilabel:`Camera Presets`
- :guilabel:`Sensor`


Depth of Field
==============

.. figure:: /images/Manual-Camera-dof-panel.jpg
   :width: 270px
   :figwidth: 270px

   Camera Display panel


Depth of Field Object
   When using :doc:`Depth of Field </render/camera/depth_of_field>`,
   the linked object will determine the focal point. Linking an object will deactivate the distance parameter.
Distance
   Distance to the focal point. It is shown as a yellow cross on the camera line of sight.
   :guilabel:`Limits` must be enabled to see the cross.
   It is used in combination with the :doc:`Defocus Compositing Node </composite_nodes/types/filter#defocus>`.


Display
=======

.. figure:: /images/Manual-Camera-display-panel.jpg
   :width: 270px
   :figwidth: 270px

   Camera Display panel


Limits
   Toggles viewing of the limits on and off.
Mist
   Toggles viewing of the mist limits on and off.
   The limits are shown as two connected white dots on the camera line of sight.
   The mist limits and other options are set in the :guilabel:`World` panel,
   in the :doc:`Mist section </world/mist>`.


.. figure:: /images/Manual-Camera-camera-view.jpg
   :width: 350px
   :figwidth: 350px

   Camera view displaying safe areas, sensor and name


Safe Areas
   When this is enabled, extra dotted frames are drawn when in camera view,
   delimiting the area considered as "safe" for important things.
Sensor
   Displays a dotted frame in camera view.
Name
   Toggle name display on and off in camera view.
Size
   Size of the camera icon in the 3D view. This setting has no effect on the render output of a camera,
   and is only a cosmetic setting.
   The camera icon can also be scaled using the standard Scale :kbd:`S` transform key.
Passepartout, Alpha
   This mode darkens the area outside of the camera's field of view, based on the :guilabel:`Alpha` setting.


Composition Guides
==================

:guilabel:`Composition Guides` are available from the drop-down menu, which can help when framing a shot.
There are 8 types of guides available:


Center
   Adds lines dividing the frame in half vertically and horizontally.
Center Diagonal
   Adds lines connecting opposite corners.
Thirds
   Adds lines dividing the frame in thirds vertically and horizontally.
Golden
   Divides the width and height into Golden proportions (About 0.618 of the size from all sides of the frame).
Golden Triangle A
   Draws a diagonal line from the lower-left to upper-right corners,
   then adds perpendicular lines that pass through the top left and bottom right corners.
Golden Triangle B
   Same as A, but with the opposite corners.
Harmonious Triangle A
   Draws a diagonal line from the lower-left to upper-right corners,
   then lines from the top left and bottom right corners to 0.618 the lengths of the opposite side.
Harmonious Triangle B
   Same as A, but with the opposite corners.


Camera Navigation
=================

Here you will find some handy ways to navigate and position your camera in your scene.


.. note::

   Remember that the active "camera" might be any kind of object.
   So these actions can be used e.g. to position and aim a lamp...


Move active camera to view
==========================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Hotkey:   :kbd:`ctrl-alt-pad0`


This feature allows you to position and orient the active camera to match your current
viewport.

Select a camera and then move around in the 3D view to a desired position and direction for
your camera (so that you're seeing what you want the camera to see). Now press
:kbd:`ctrl-alt-pad0` and your selected camera positions itself to match the view,
and switches to camera view.


Camera View Positioning
=======================

By enabling :guilabel:`Lock Camera to View` in the View menu of the View Properties panel,
while in camera view, you can navigate the 3d viewport as usual,
while remaining in camera view. Controls are exactly the same as when normally moving in 3d.


Roll, Pan, Dolly, and Track
===========================

To perform these camera moves, the camera must first be *selected*,
so that it becomes the active object (while viewing through it,
you can :kbd:`rmb` -click on the solid rectangular edges to select it).
The following actions also assume that you are in camera view
(:kbd:`pad0`)! Having done so, you can now manipulate the camera using the same commands
that are used to manipulate any object:

Roll
   Press :kbd:`R` to enter object rotation mode. The default will be to rotate the camera in its local Z-axis
   (the axis orthogonal to the camera view), which is the definition of a camera "roll".
Vertical Pan or Pitch
   This is just a rotation along the local X-axis. Press :kbd:`R` to enter object rotation mode, then :kbd:`X` twice
   (the first press selects the *global* axis - pressing the same letter a second time selects the *local* axis -
   this works with any axis; see the :doc:`axis locking page </3d_interaction/transform_control/axis_locking>`).
Horizontal Pan or Yaw
   This corresponds to a rotation around the camera's local Y axis... Yes, that's it, press :kbd:`R`,
   and then :kbd:`Y` twice!
Dolly
   To dolly the camera, press :kbd:`G` then :kbd:`mmb` (or  :kbd:`Z` twice).
Sideways Tracking
   Press :kbd:`G` and move the mouse
   (you can use  :kbd:`X` twice or :kbd:`Y` to get pure-horizontal or pure-vertical sideways tracking).


Aiming the camera in Flymode
============================

When you are in :guilabel:`Camera` view,
the :doc:`fly mode </3d_interaction/navigating#fly_mode>` actually moves your active camera...

.. youtube:: bTRrHNn-d4w


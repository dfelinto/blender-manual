
Introduction
************

To be able to work in the three dimensional space that Blender uses,
you must be able to change your viewpoint as well as the viewing direction of the scene.
While we will describe the :guilabel:`3D View` window,
most of the other windows have similar functions. For example,
it is possible to translate and zoom a :guilabel:`Buttons` window and its panels.


.. tip:: Mouse Buttons and Numpad

   If you have a mouse with less than three buttons or a keyboard without numpad,
   please refer to the :doc:`Keyboard and Mouse <interface/keyboard_and_mouse>`
   page of the manual to learn how to use them with Blender.


Perspective and Orthographic Views
**********************************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`View --> Perspective` / :menuselection:`View --> Orthographic`
   | Hotkey:   :kbd:`pad5`


Description
===========

Each 3D viewport supports two different types of projection.
These are demonstrated in the *Orthographic (left) and perspective (right)
projections* image below.


.. figure:: /images/Manual-Part-I-3DPerspective.jpg
   :width: 630px
   :figwidth: 630px

   Orthographic (left) and perspective (right) projections.


Our eye is used to perspective viewing because distant objects appear smaller.
Orthographic projection often seems a bit odd at first,
because objects stay the same size regardless of their distance.
It is like viewing the scene from an infinitely distant point. Nevertheless,
orthographic viewing is very useful
(it is the default in Blender and most other 3D applications),
because it provides a more "technical" insight into the scene,
making it easier to draw and judge proportions.


Options
=======

.. figure:: /images/Manual-Part-I-3DCameraView-2.5.jpg

   Demonstration of camera view.


To change the projection for a 3D view,
choose the :menuselection:`View --> Orthographic` or the :menuselection:`View --> Perspective` menu entry.
The :kbd:`pad5` shortcut toggles between the two modes.
Changing the projection for a 3D view does not affect the way the scene will be rendered.
Rendering is in perspective by default. If you need to create an orthographic rendering,
select the camera, go to the :guilabel:`Object Data` context and press the
:guilabel:`Orthographic` button in the :guilabel:`Lens` panel.

The :menuselection:`View --> Camera` menu entry sets the 3D view to camera mode (:kbd:`pad0`).
The scene is then displayed as it will be rendered later
(see *Demonstration of camera view*).
The rendered image will contain everything within the orange dotted line.
Zooming in and out is possible in this view, but to change the viewpoint,
you have to move or rotate the camera.

If you have a large scene, viewing it through Camera View may not display all of the Objects in the scene.
One possibility may be that the :doc:`clipping distance <render/camera#camera_settings>` of the camera is too low.
The camera will only show objects that fall within the clipping range.


:doc:`Read more about Render perspectives » <render/camera/perspective>`

:doc:`Read more about Camera View » <3d_interaction/navigating/camera_view>`

:doc:`Read more about Camera clipping » <render/camera#camera_settings>`


Technical Details
=================

Perspective definition
----------------------

A *perspective* view is geometrically constructed by taking a scene in 3D and placing an
observer at point ``O``. The 2D perspective scene is built by placing a plane (e.g.
a sheet of paper) where the 2D scene is to be drawn in front of point ``O``,
perpendicular to the viewing direction.
For each point ``P`` in the 3D scene a ``PO`` line is drawn,
passing by ``O`` and ``P``. The intersection point ``S`` between
this ``PO`` line and the plane is the perspective projection of that point.
By projecting all points ``P`` of the scene you get a perspective view.


Orthographic definition
-----------------------

In an *orthographic* projection,
you have a viewing direction but not a viewing point ``O``. The line is then drawn
through point ``P`` so that it is parallel to the viewing direction. The intersection
``S`` between the line and the plane is the orthographic projection of the point
``P``.
By projecting all points ``P`` of the scene you get the orthographic view.


Rotating the View
*****************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`View --> Navigation`
   | Hotkey:   :kbd:`mmb` / :kbd:`pad2` / :kbd:`pad4` / :kbd:`pad6` / :kbd:`pad8` / :kbd:`ctrl-alt-wheel`


Description
===========

.. figure:: /images/Manual-Part-I-3DView2.5.jpg
   :width: 300px
   :figwidth: 300px

   A 3D viewport's View menu.


Blender provides four default viewing directions: :guilabel:`Side`, :guilabel:`Front`,
:guilabel:`Top` and :guilabel:`Camera` view.
Blender uses a right-angled "Cartesian" coordinate system with the Z axis pointing upwards.
"Side" corresponds to looking along the X axis, in the negative direction,
"Front" along the Y axis, and "top" along the Z axis.
The :guilabel:`Camera` view shows the current scene as seen from the camera view point.


Options
=======

You can select the viewing direction for a 3D viewport with the :guilabel:`View` menu entries,
or by pressing the hotkeys :kbd:`pad3` for "side", :kbd:`pad1` for "front",
:kbd:`pad7` for "top". You can select the opposite directions if you hold
:kbd:`Ctrl` while using the same numpad shortcuts.
Finally :kbd:`pad0` gives access to the "camera" viewpoint.

Apart from these four default directions, the view can be rotated to any angle you wish.
Click and drag :kbd:`mmb` on the viewport's area.
If you start in the middle of the window and move up and down or left and right,
the view is rotated around the middle of the window. Alternatively, if the :guilabel:`Emulate 3
button mouse` option is select in the :guilabel:`User Preferences` you can press and hold
:kbd:`Alt` while dragging :kbd:`lmb` in the viewport's area.

To change the viewing angle in discrete steps, use :kbd:`pad8` and :kbd:`pad2`
(which correspond to vertical :kbd:`mmb` dragging, from any viewpoint),
or use :kbd:`pad4` and :kbd:`pad6` (or :kbd:`ctrl-alt-wheel`)
to rotate the scene around the Z global axis from your current point of view.


.. admonition:: Hotkeys
   :class: note

   Remember that most hotkeys affect **the active window** (the one that has focus),
   so check that the mouse cursor is in the area you want to work in before your use the hotkeys.


TrackBall/Turntable
-------------------

By default, when you rotate the view as described above,
you are using the **turntable** method.
For some users this is intuitive and for others it is not. If you feel you are having
difficulties with this style of 3D window rotation you can switch to the "\ **trackball** "
style. With the trackball style you are rotating the scene as though you are rolling your hand
across a "\ **trackball** "

The :guilabel:`Turntable` style is fashioned more like a record player where you have two axes
of rotation available,
and the world seems to have a better definition of what is "Up" and "Down" in it. The downside
to using the :guilabel:`Turntable` style is that you lose some flexibility when working with
your objects. However,
you gain the sense of "Up" and "Down" which can help if you are feeling disoriented.
Of course you can always switch between the styles depending on what you are working on.


.. figure:: /images/Manual-Part-I-Interface-Navigating-InfoWindow-ViewRotation2.5.jpg

   View rotation.


To change the rotation "style", use the :doc:`User Preferences window <preferences>`.
Click on the :guilabel:`Input` button and you will see an option for choosing the Orbit style.
There are two additional checkboxes for controlling the display in the 3D window in the :guilabel:`Interface` tab in
the :guilabel:`User Preferences`.
:guilabel:`Auto Perspective` will automatically switch to perspective whenever the view is rotated using :kbd:`mmb`.
:guilabel:`Rotate Around Selection` will rotate the view around the center of the current selection.
If there is no selection at that moment (e.g. if you used :kbd:`A` to deselect everything),
the last selection will be used anyway.



Panning the View
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :guilabel:`View` → :guilabel:`Navigation`
   | Hotkey:   :kbd:`shift-Mmb` / :kbd:`ctrl-pad2` / :kbd:`ctrl-pad4` / :kbd:`ctrl-pad6` / :kbd:`ctrl-pad8` / :kbd:`shift-alt-Lmb`


Description
===========

To pan the view, hold down :kbd:`Shift` and drag :kbd:`mmb` in the 3D Viewport.
For discrete steps, use the hotkeys :kbd:`ctrl-pad8`, :kbd:`ctrl-pad2`,
:kbd:`ctrl-pad4` and :kbd:`ctrl-pad6` as with rotating (note:
you can replace :kbd:`Ctrl` by :kbd:`Shift`).
For those without a middle mouse button,
you can hold :kbd:`Shift` :kbd:`Alt` while dragging with :kbd:`lmb`.


Zooming the View
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :guilabel:`View` → :guilabel:`Navigation`
   | Hotkey:   :kbd:`ctrl-mmb` / :kbd:`wheel` / :kbd:`pad+` / :kbd:`pad-`


Description
===========

You can zoom in and out by holding down :kbd:`Ctrl` and dragging :kbd:`mmb`.
The hotkeys are :kbd:`pad+` and :kbd:`pad-`.
The :menuselection:`View --> Navigation` sub-menu holds these functions too as well.
Refer to the 3D viewport's :guilabel:`View` menu image above for more information.

If you have a wheel mouse, you can perform all of the actions in the 3D viewport that you
would do with :kbd:`pad+` and :kbd:`pad-` by rotating the :kbd:`wheel`.
To zoom a :guilabel:`Buttons` window,
hold :kbd:`CTRL-MMB` and move your mouse up and down.


.. admonition:: If You Get Lost
   :class: note

   If you get lost in 3D space, which is not uncommon, two hotkeys will help you:
   :kbd:`home` changes the view so that you can see all objects (:menuselection:`View --> View All` menu entry),
   while :kbd:`pad.` zooms the view to the currently selected objects when in perspective mode
   (:menuselection:`View --> View Selected` menu entry).



Zoom Border
===========

The :guilabel:`Zoom Border` tool allows you to specify a rectangular region and zoom in so
that the region fills the 3d view.

You can access this through the :guilabel:`View` menu,
or the shortcut :kbd:`shift-B` then click and drag rectangle to zoom in.


Dolly the View
**************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`ctrl-shift-mmb`


Description
===========

In most cases its sufficient to zoom the view to get a closer look at something,
however you may notice that at a certain point you cannot zoom any closer.

This is because Blender stores a view-point thats used for orbiting and zooming, This works
well in many cases but sometimes you want to move the view-point to a different place - This
is what Dolly supports, allowing you to transport the view from one place to another.

You can dolly back and fourth by holding down :kbd:`Ctrl-Shift` and dragging
:kbd:`mmb`.


Aligning the View
*****************

Align View
==========

These options allow you to align and orient the view in different ways.
They are found in the :guilabel:`View Menu`

   :guilabel:`Align View to Selected` menu
      These options align your view with specified local axes of the selected object or, in :guilabel:`Edit` mode,
      with the normal of the selected face.


      :guilabel:`Top` :kbd:`shift-pad7`
      :guilabel:`Bottom` :kbd:`shift-ctrl-pad7`
      :guilabel:`Front` :kbd:`shift-pad1`
      :guilabel:`Back` :kbd:`shift-ctrl-pad1`
      :guilabel:`Right` :kbd:`shift-pad3`
      :guilabel:`Left` :kbd:`shift-ctrl-pad3`

   :guilabel:`Center Cursor and View All` (:kbd:`shift-C`)
      moves the cursor back to the origin **and** zooms in/out so that you can see everything in your scene.
   :guilabel:`Align Active Camera to View`, :kbd:`ctrl-alt-pad0`
      Gives your active camera the current viewpoint
   :guilabel:`View selected`, :kbd:`pad.`
      Focuses view on currently selected object/s by centering them in the viewport,
      and zooming in until they fill the screen.
   :guilabel:`Center view to cursor`, :kbd:`alt-home`
      Centers view to 3D-cursor

:guilabel:`View Selected`
   See above
:guilabel:`View All` :kbd:`home`
   Frames all the objects in the scene, so they are visible in the viewport.


Local and Global View
*********************

You can toggle between :guilabel:`Local` and :guilabel:`Global` view by selecting the option
from the :guilabel:`View Menu` or using the shortcut :kbd:`pad/`.
Local view isolates the selected object or objects,
so that they are the only ones visible in the viewport.
This is useful for working on objects that are obscured by other ones, or have heavy geometry.
Press :kbd:`pad/` to return to :guilabel:`Global View`.


Quad View
*********

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`View --> Toggle Quad View`
   | Hotkey:   :kbd:`ctrl-alt-q`


.. figure:: /images/3D_Interaction-Navigating-3D_view-Quad_View.jpg
   :width: 340px
   :figwidth: 340px

   Quad View


Toggling Quad View will split the 3D window into 4 views: Top Ortho, Front Ortho,
Right Ortho and Camera / User View.
This view will allow you to instantly see your model from a number of view points.
In this arrangement,
you can zoom and pan each view independently but you cannot rotate the view.
Note that this is different from splitting the windows and aligning the view manually.
In Quad View, the four views are still part of a single 3D window.
If you want to be able to rotate each view,
you will need to split the 3D window into separate windows.

:doc:`Read more about splitting windows » <interface/window_system/arranging_frames>`


View Clipping Border
********************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`View --> Set Clipping Border`
   | Hotkey:   :kbd:`alt-B`


Description
===========

.. figure:: /images/3D_Interaction-Navigating-3D_view-Region_Clipping.jpg
   :width: 340px
   :figwidth: 340px

   Region/Volume clipping.


To assist in the process of working with complex models and scenes,
you can set the view clipping to visually isolate what you're working on.

Once clipping is used, you will only see whats inside a volume you've defined.
Tools such as paint, sculpt, selection, transform-snapping etc.
will also ignore geometry outside the clipping bounds.

Once activated with :kbd:`alt-B`, you have to draw a rectangle with the mouse,
in the wanted 3D view. The created clipping volume will then be:

- A right-angled `parallelepiped <http://en.wikipedia.org/wiki/Parallelepiped>`__
  (of infinite length) if your view is orthographic.
- A rectangular-based pyramid (of infinite height) if your view is in perspective.

To delete this clipping, press :kbd:`alt-B` again.


Example
=======

The *Region/Volume clipping* image shows an example of using the clipping tool with a cube.
Start by activating the tool with :kbd:`alt-B` (upper left of the image).
This will generate a dashed cross-hair cursor.
Click with the :kbd:`lmb` and drag out a rectangular region shown in the upper right.
Now a region is defined and clipping is applied against that region in 3D space.
Notice that part of the cube is now invisible or clipped. Use the :kbd:`mmb` to rotate
the view and you will see that only what is inside the pyramidal volume is visible.
All the editing tools still function as normal but only within the pyramidal clipping volume.

The dark gray area is the clipping volume itself.
Once clipping is deactivated with another :kbd:`alt-B`,
all of 3D space will become visible again.


View Navigation
***************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`shift-F`


Description
===========

When you have to place the view, normally you do as described above.

However, there are cases in which you really prefer to just navigate your model,
especially if it's very large, like environments or some architectural model.
In these cases viewing the model in perspective mode has limitations,
for example after zooming a lot of panning is extremely uncomfortable and difficult,
or you apparently cannot move the camera any nearer. As an example,
try to navigate to a very distant object in the view with traditional methods
(explained above) and see what you can get.

With  :doc:`Walk mode <3d_interaction/navigating/3d_view/navigation_modes#walk_mode>` and
:doc:`Fly mode <3d_interaction/navigating/3d_view/navigation_modes#fly_mode>` you move, pan and tilt,
and dolly the camera around without any of those limitations.


.. figure:: /images/3D_Interaction-Navigating-3D_view-Navigation_Mode.jpg
   :width: 173px
   :figwidth: 173px

   View Navigation.


In the :doc:`User Preferences window <preferences>`
select the navigation mode you want to use as default when invoking the View Navigation operator.
Alternatively you can call the individual modes from the View Navigation menu.



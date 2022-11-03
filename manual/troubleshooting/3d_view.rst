.. (Todo <2.8 add) GL texture limit.

***********
3D Viewport
***********

Rendering
=========

.. _troubleshooting-depth:

Depth Buffer Glitches
---------------------

Sometimes when setting a large :ref:`clipping range <bpy.types.SpaceView3D.clip_start>`
will allow you to see both near and far objects,
but reduces the depth precision resulting in artifacts.

.. list-table::

   * - .. figure:: /images/troubleshooting_3d-view_graphics-z-fighting-none.png
          :width: 200px

          Model with no clipping artifacts.

     - .. figure:: /images/troubleshooting_3d-view_graphics-z-fighting-example.png
          :width: 200px

          Model with clipping artifacts.

     - .. figure:: /images/troubleshooting_3d-view_graphics-z-fighting-example-editmode.png
          :width: 200px

          Mesh with artifacts in Edit Mode.

To avoid this:

- Increase the near clipping when working on large scenes.
- Decrease the far clipping when objects are not viewed at a distance.

When perspective is disabled only the far Clip End is used, very high values can still result in artifacts.
This is **not** specific to Blender, all graphics applications have these same limitations.


Objects Invisible in Camera View
--------------------------------

If you have a large scene, viewing it through Camera View may not display all of the objects in the scene.
One possibility may be that the :ref:`clipping distance <camera-clipping>` of the camera is too low.
The camera will only show objects that fall within the clipping range.


Performance
===========

Slow Rendering
--------------

There are a couple of reasons why you may be experiencing a slow viewport.

Old Hardware
   Sometimes your hardware, mainly your graphics card, may be too slow to keep up with your model.
Upgrade Graphics Driver
   In some cases, slow selection is resolved by using updated drivers.


Slow Selection
--------------

Blender uses OpenGL for selection, some graphics card drivers are slow at performing this operation.

This becomes especially problematic on dense geometry.

Possible Solutions:

GPU Depth Picking (Preferences)
   See :menuselection:`Preferences --> Viewport --> Selection`.

   This option is enabled by default, disabling it may give a better performance at
   the cost of selection accuracy.
Upgrade Graphics Driver
   In some cases, slow selection is resolved by using updated drivers.
   *It is generally good to use recent drivers when using 3D software.*
Select Centers (Workaround)
   In *Object Mode*, holding :kbd:`Ctrl` while selecting uses the object center point.
   While this can be useful on its own, it has the side effect of not relying on OpenGL selection.
Change Display Mode (Workaround)
   Using *Wireframe* display mode can be used to more quickly select different objects.

.. note::

   Obviously, the workarounds listed here are not long term solutions,
   but it is handy to know if you are stuck using a system with poor OpenGL support.

   Ultimately, if none of these options work out it may be worth upgrading your hardware.


Navigation
==========

Lost in Space
-------------

When navigating your scene, you may accidentally navigate away from your scene
and find yourself with a blank viewport. There are two ways to fix this:

#. Select an object in the :doc:`Outliner </editors/outliner/index>`,
   then zoom to that object with :menuselection:`View --> Frame Selected` or :kbd:`NumpadPeriod`.
#. Use :kbd:`Home` to fit all objects into the 3D Viewport.


Invisible Limit Zooming In
--------------------------

Sometimes when navigating you may be trying to zoom in but it seems that you have hit a limit
to how far you can zoom.
This is because Blender uses a central point to orbit around.

In practice this is good for modeling an object which you rotate about a lot to see from all sides
(think of a potter using a wheel).
However, this makes it awkward to explore a scene or model an object from the 'inside', for example.


Solutions
^^^^^^^^^

- Use :ref:`View Dolly <bpy.ops.view3d.dolly>`.
- Use :ref:`Walk/Fly Navigation <3dview-fly-walk>`.
- Use :ref:`Auto Depth <prefs-navigation-auto_depth>` and :ref:`Zoom to Mouse Position <prefs-zoom-mouse-pos>`.
  These tools will make sure the distance is always the value under the mouse cursor,
- Use :ref:`bpy.ops.view3d.zoom_border` as it also resets the center point when zooming.
- Center the view around the mouse cursor :kbd:`Alt-MMB`.
  This will take the position under the cursor and make it your viewpoint center.
- Use an :abbr:`NDOF (N-Degrees of Freedom)`, also known as a 3D mouse,
  see :ref:`configuring peripherals <hardware-ndof>` for more information.


Tools
=====

.. _troubleshooting-3dview-invalid-selection:

Invalid Selection
-----------------

There are times when selection fails under some configurations,
often this is noticeable in mesh *Edit Mode*,
selecting vertices/edges/faces where random elements are selected.

Internally Blender uses :term:`OpenGL` for selection,
so the graphics card driver relies on giving correct results.

Possible Solutions:

Disable :term:`Multisampling`
   This is by far the most common cause of selection issues.

   There are known problems with some graphics cards when using multisampling.

   You can disable this option by turning multisampling off in your graphics card driver options.

Change Anti-Aliasing Sample Settings
   Depending on your OpenGL configuration,
   some specific sample settings may work while others fail.

   Unfortunately finding working configuration involves trial & error testing.
Upgrade Graphics Driver
   As with any OpenGL-related issues, using recent drivers can resolve problems.

   However, it should be noted that this is a fairly common problem and remains unresolved with many drivers.

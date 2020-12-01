
*******
Sidebar
*******

Item
====

Shows :doc:`Transform </scene_layout/object/editing/transform/introduction>` settings
of the active objects.


Tool
====

Show settings of the active tool and Workspace.


View
====

View Panel
----------

The *View* panel lets you set other settings regarding the 3D Viewport.
You can show it with the :menuselection:`View --> View Properties...` menu entry.

Focal Length
   Control the focal length of the 3D Viewport camera in millimeters,
   unlike a :doc:`rendering camera </render/cameras>`.

.. _3dview-view-clip:

Clip Start/End
   Adjust the minimum and maximum distances range to limit the visible range to the area
   between two planes that are orthogonal to the viewing direction of the viewport camera.
   Objects outside the range will not be shown.

   .. note::

      The definition of the two planes depends on the kind of view:

      - Perspective view: The planes with distance of start and end from viewport camera.

      - Orthographic view: The planes with distance of negative end and positive end from the focus point,
        in this case the *Start* is ignored.

   .. warning::

      A large clipping range will allow you to see both near and far objects,
      but reduces the depth precision resulting in artifacts.

      In some cases, a very large range may cause operations that depend on the depth buffer to become unreliable
      although this depends on the graphics card and drivers.

      See :ref:`Troubleshooting Depth Buffer Glitches <troubleshooting-depth>` for more information.

Local Camera
   Use a local camera in this view, selected from the object selector,
   rather than the scene's (global) active camera.

Render Region
   Use a Render Region when not looking through a camera.
   Using :kbd:`Ctrl-B` to draw a region will automatically enable this option.


.. _bpy.types.SpaceView3D.lock:

View Lock
^^^^^^^^^

Lock to Object
   A :ref:`ui-data-id` that defines an object as the center of the view.
   In this case, the view can be rotated around or zoomed towards that central object,
   but not while you move the object itself
   (this option is not available in a camera view).

.. _3dview-lock-camera-to-view:

Lock
   To 3D Cursor
      Lock the center of the view to the position of the 3D cursor.
      It is only available when *Lock to Object* is not active.
   Camera to View
      When in camera view, all changes in the view (pans, rotations, zooms) will affect the active camera.
      The camera frame will be outlined with a red dashed line.

.. hint::

   This will move the camera's parent which can be useful with camera rigs.
   Use the :ref:`Camera Parent Lock <bpy.types.Object.use_camera_lock_parent>` property to change this behavior.


3D Cursor
---------

Location
   The location of the 3D Cursor.

Rotation
   The rotation of the 3D Cursor.

Rotation Mode
   The Rotation mode of the 3D Cursor.


.. _bpy.types.SpaceView3D.use_local_collections:

Collections
-----------

The *Collections* panel shows a list of collections
and can be used to control the visibility of collections in the viewport.
If a collection contains objects, there is a circle to the left of the collection name.
If a collection is empty, there is no circle to the left of the collection name.

Local Collections
   Allows the list of visible collections to be controlled per viewport rather than globally.

Hide in Viewport (eye icon)
   Collections can be hidden in the viewport by clicking on the eye icon.

By clicking directly on the collection names,
it "isolates" the collection by hiding all other collections,
and showing the direct parents and all the children of the selected collection.

.. seealso::

   Read more about :doc:`Collections </scene_layout/collections/index>`.


Annotations
-----------

See :doc:`Annotations </interface/annotate_tool>` for more information.

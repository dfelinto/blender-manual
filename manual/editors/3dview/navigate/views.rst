
****************
Contextual Views
****************

By default, the 3D Viewport only shows the scene from one viewpoint.
By using Quad Views, you can see it from multiple viewpoints at the same time,
which gives more context about the changes you're making.


.. _bpy.ops.screen.region_quadview:

Quad View
=========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Area --> Toggle Quad View`
   :Shortcut:  :kbd:`Ctrl-Alt-Q`

Toggling Quad View will split the 3D Viewport into four views:
three orthographic side views and one user perspective view.

.. note::

   Quad View is different from :doc:`splitting the area </interface/window_system/areas>`
   and aligning the views manually. In Quad View, the four views are still part of a single 3D Viewport,
   so that they share the same display options.

.. figure:: /images/editors_3dview_navigate_views_quad.png

   Quad View.


Options
-------

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Sidebar --> View --> Quad View`

.. _bpy.types.RegionView3D.lock_rotation:

Lock Rotation
   When disabed, makes it possible to orbit in the orthographic views as well
   (turning them into perspective views instead).

.. _bpy.types.RegionView3D.show_sync_view:

Sync Zoom/Pan
   Syncs the view position between side views. (Requires *Lock Rotation* to be enabled.)

.. _bpy.types.RegionView3D.use_box_clip:

Clip Contents
   Clip objects based on what is visible in the other side views. 

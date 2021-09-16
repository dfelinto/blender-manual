
****************
Contextual Views
****************

The 3D Viewport has several "contextual view" modes that can be set for a particular 3D Viewport.
These views can change how the overall 3D Viewport looks or how you interact with objects.


.. _bpy.ops.screen.region_quadview:

Quad View
=========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Area --> Toggle Quad View`
   :Shortcut:  :kbd:`Ctrl-Alt-Q`

Toggling Quad View will split the 3D Viewport into four views:
Three *Orthographic* "side views" and one *Camera*/*User View*.
This view will allow you to instantly see your model from a number of view points.
In this arrangement, you can zoom and pan each view independently but you cannot rotate the view.

.. note::

   Quad View is different from :doc:`splitting the area </interface/window_system/areas>`
   and aligning the view manually. In Quad View, the four views are still part of a single 3D Viewport.
   So they share the same display options and layers.

.. figure:: /images/editors_3dview_navigate_views_quad.png

   Quad View.


Options
-------

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Sidebar --> View --> Quad View`

.. _bpy.types.RegionView3D.lock_rotation:

Lock Rotation
   If you want to be able to rotate each view, you can uncheck the *Locked* option.

.. _bpy.types.RegionView3D.show_sync_view:

Sync View/Pan 
   Syncs the view position between side views. (Requires *Lock* to be enabled.)

.. _bpy.types.RegionView3D.use_box_clip:

Clip Contents
   Clip objects based on what is visible in other side views. (Requires *Box* to be enabled.)

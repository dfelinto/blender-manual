
************
View Regions
************

.. _bpy.ops.view3d.clip_border:

Clipping Region
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`View --> View Regions --> Clipping Region...`
   :Shortcut:  :kbd:`Alt-B`

Allows you to define a clipping region to limit the 3D Viewport display to a portion of 3D space.
It can assist in the process of working with complex models and scenes.

Once activated, you have to draw a rectangle with the mouse,
in the wanted 3D Viewport. It becomes a clipping volume of four planes:

- A right-angled `parallelepiped <https://en.wikipedia.org/wiki/Parallelepiped>`__
  (of infinite length) if your view is orthographic.
- A rectangular-based pyramid (of infinite height) if your view is in perspective.

Once clipping is used, you will only see what's inside the volume you have defined.
Tools such as paint, sculpt, selection, transform snapping, etc.
will also ignore geometry outside the clipping bounds.

To delete this clipping, press :kbd:`Alt-B` again.


Example
-------

.. list-table:: Region/Volume clipping.

   * - .. figure:: /images/editors_3dview_navigate_regions_border1.png
          :width: 320px

          Selecting a region.

     - .. figure:: /images/editors_3dview_navigate_regions_border2.png
          :width: 320px

          Region selected.

     - .. figure:: /images/editors_3dview_navigate_regions_border3.png
          :width: 320px

          View rotated.

The *Region/Volume clipping* image shows an example of using the clipping tool with a cube.
Start by activating the tool with :kbd:`Alt-B` (upper left of the image).
This will generate a dashed cross-hair cursor.
Click with the :kbd:`LMB` and drag out a rectangular region shown in the upper right.
Now a region is defined and clipping is applied against that region in 3D space.
Notice that part of the cube is now invisible or clipped. Use the :kbd:`MMB` to rotate
the view and you will see that only what is inside the pyramidal volume is visible.
All the editing tools still function as normal but only within the pyramidal clipping volume.

The dark gray area is the clipping volume itself.
Once clipping is deactivated with another :kbd:`Alt-B`,
all of 3D space will become visible again.


.. _editors-3dview-navigate-render-region:

Render Region
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`View --> View Regions --> Render Region...`
               :menuselection:`View --> View Regions --> Clear Render Region`
   :Shortcut:  Mark: :kbd:`Ctrl-B`
               Clear: :kbd:`Ctrl-Alt-B`

When using :ref:`rendered shading <view3d-viewport-shading>` mode,
it can be quite slow to render the entire 3D Viewport. To fix this,
you can define a subregion to render just a portion of the viewport
instead of the entire viewport.
This can be very useful for reducing render times for quick previews on an area of interest.

.. list-table:: Render region and associated render.
   :widths: 65 35

   * - .. figure:: /images/editors_3dview_navigate_regions_render-border-1.png

     - .. figure:: /images/editors_3dview_navigate_regions_render-border-2.png

.. tip::

   You can also use this region in a final render by setting a render region
   from within the :doc:`Camera View </editors/3dview/navigate/camera_view>`
   and enabling :ref:`region <bpy.types.RenderSettings.use_border>` in the Dimensions panel.

.. seealso::

   :ref:`3dview-nav-zoom-region`.

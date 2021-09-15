
***********
Performance
***********

.. reference::

   :Panel:     :menuselection:`Render --> Performance`


Threads
=======

.. _bpy.types.RenderSettings.threads_mode:

Mode
   Method to determine the maximum number of CPU cores to use while rendering.

   :Auto-Detect:
      Automatically chooses the amount of threads to match the number of logical processors on your computer.
   :Fixed:
      Manually choose the maximum number threads to use for rendering.
      This can be useful for example, if you want to use your computer while rendering,
      you can set the property to a thread count lower the amount of logical processors on your computer.

.. _bpy.types.RenderSettings.threads:

Threads
   The maximum number of CPU cores to use simultaneously while rendering.


Tiles
=====

.. _bpy.types.RenderSettings.tile_x:
.. _bpy.types.RenderSettings.tile_y:

Tiles X, Y
   The size of the tiles for rendering.

   Depending on what device you are using for rendering, different tile sizes can give faster renders.
   For CPU rendering smaller tiles sizes (like 32 × 32) tend to be faster, while for
   :doc:`GPU rendering </render/cycles/gpu_rendering>` larger tile sizes give a better performance (like 256 × 256).

.. _bpy.types.CyclesRenderSettings.tile_order:

Order
   Order of rendering tiles. This does not significantly affect the performance.

.. _bpy.types.CyclesRenderSettings.use_progressive_refine:

Progressive Refine
   Instead of rendering each tile until it has finished every sample, refine the whole image progressively.
   Note that progressive rendering is slightly slower than tiled rendering,
   but time can be saved by manually stopping the render when the noise level is low enough.

   For rendering animations it is best to disable this feature, as stopping a frame early is not possible.


Acceleration Structure
======================

.. _bpy.types.CyclesRenderSettings.debug_use_spatial_splits:

Use Spatial Splits
   Spatial splits improve the rendering performance in scenes with a mix of large and small polygons.
   The downsides are longer BVH build times and slightly increased memory usage.

.. _bpy.types.CyclesRenderSettings.debug_use_hair_bvh:

Use Hair BVH
   Use a special type of :term:`BVH` for rendering hair.
   The bounding boxes are not axis aligned allowing a spatially closer fit to the hair geometry.
   Disabling this option will reduce memory, at the cost of increasing hair render time.

.. _bpy.types.CyclesRenderSettings.debug_bvh_time_steps:

BVH Time Steps
   Split BVH primitives by this number of time steps to speed up render time at the expense of memory.


Final Render
============

.. _bpy.types.RenderSettings.use_save_buffers:

Save Buffers
   Saves all render layers and passes to the temp directory on a drive,
   and reads them back after rendering has finished. This saves memory (RAM) usage during rendering,
   particularly when using many render layers and passes. This can be read back in the Compositor
   and Image editor by using :ref:`bpy.ops.node.read_viewlayers`.

.. _bpy.types.RenderSettings.use_persistent_data:

Persistent Data
   Keep render data in memory after rendering for faster re-renders and animation renders
   at the cost of extra memory usage while performing other tasks in Blender.

   When using multiple :doc:`View Layers </render/layers/view_layer>`,
   only data from a single view layer is preserved to keep memory usage within bounds;
   however, objects shared between view layers are preserved.


Viewport
========

.. _bpy.types.RenderSettings.preview_pixel_size:

Pixel Size
   Option to control the resolution for viewport rendering.
   Allows you to speed up viewport rendering, which is especially useful for displays with high DPI.

.. _bpy.types.CyclesRenderSettings.preview_start_resolution:

Start Pixels
   Resolution to start rendering preview at, progressively increase it to the full viewport size.


***********
Performance
***********

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Performance`


Threads
=======

Mode
   Auto-detect
      Automatically chooses the amount of threads to match the number of logical processors on your computer.

   Fixed
      Manually choose the maximum number threads to use for rendering.
      This can be useful for example, if you want to use your computer while rendering,
      you can set the property to a thread count lower the amount of logical processors on your computer.


Tiles
=====

Tile Order
   Order of rendering tiles. This does not significantly affect the performance.

Tile Size X/Y
   The size of the tiles for rendering.

   Depending on what device you are using for rendering, different tile sizes can give faster renders.
   For CPU rendering smaller tiles sizes (like 32 × 32) tend to be faster, while for
   :doc:`GPU rendering </render/cycles/gpu_rendering>` larger tile sizes give a better performance (like 256 × 256).

Progressive Refine
   Instead of rendering each tile until it has finished every sample, refine the whole image progressively.
   Note that progressive rendering is slightly slower than tiled rendering,
   but time can be saved by manually stopping the render when the noise level is low enough.

   For rendering animations it is best to disable this feature, as stopping a frame early is not possible.

.. _render_properties_save-buffers:

Save Buffers
   Saves all render layers and passes to the temp directory on a drive,
   and reads them back after rendering has finished. This saves memory (RAM) usage during rendering,
   particularly when using many render layers and passes. This can be read back in the Compositor
   and Image editor by using :ref:`bpy.ops.node.read_viewlayers`.


Acceleration Structure
======================

Use Spatial Splits
   Spatial splits improve the rendering performance in scenes with a mix of large and small polygons.
   The downsides are longer BVH build times and slightly increased memory usage.
Use Hair BVH
   Use a special type of :term:`BVH` for rendering hair.
   The bounding boxes are not axis aligned allowing a spatially closer fit to the hair geometry.
   Disabling this option will reduce memory, at the cost of increasing hair render time.
BVH Time Steps
   Split BVH primitives by this number of time steps to speed up render time at the expense of memory.


Final Render
============

Persistent Images
   Keep image data in memory after rendering, for faster re-renders at the cost of extra memory usage when
   performing other tasks in Blender.


.. _render_cycles_settings_perfomance_viewport:

Viewport
========

Pixel Size
   Option to control the resolution for viewport rendering.
   Allows you to speed up viewport rendering, which is especially useful for displays with high DPI.

Start Pixels
   Resolution to start rendering preview at, progressively increase it to the full viewport size.

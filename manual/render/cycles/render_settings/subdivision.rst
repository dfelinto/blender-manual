.. _bpy.types.CyclesRenderSettings.*dicing_rate:
.. _cycles-subdivision-rate:

***********
Subdivision
***********

.. reference::

   :Panel:     :menuselection:`Render --> Subdivision`

.. note::

   These settings are only available if :ref:`Experimental Feature Set <cycles-experimental-features>` is turned on.

These settings are used to control :doc:`Adaptive Subdivision </render/cycles/object_settings/adaptive_subdiv>`.

Render
   Size of :term:`Micropolygons` in pixels.
Viewport
   Size of :term:`Micropolygons` in pixels while preview rendering.

.. _bpy.types.CyclesRenderSettings.offscreen_dicing_scale:

Offscreen Scale
   Multiplier for dicing rate of geometry outside of the camera view.
   The dicing rate of objects is gradually increased the further they are outside the camera view.
   Lower values provide higher quality reflections and shadows for off screen objects,
   while higher values use less memory.

.. _bpy.types.CyclesRenderSettings.max_subdivisions:

Max Subdivisions
   Stop subdividing when this level is reached even if the dicing rate would produce finer :term:`Tessellation`.

.. _bpy.types.CyclesRenderSettings.dicing_camera:

Dicing Camera
   Camera to use as reference point when subdividing geometry,
   useful to avoid crawling artifacts in animations when the scene camera is moving.

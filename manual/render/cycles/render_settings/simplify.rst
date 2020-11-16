.. _render-cycles-settings-scene-simplify:
.. _bpy.types.RenderSettings.simplify_subdivision:
.. _bpy.types.CyclesRenderSettings.texture_limit:

********
Simplify
********

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Render --> Simplify`


.. rubric:: Common Settings

Max Subdivision
   Maximum number of subdivision by the Subdivision Surface modifiers.
Child Particles
   Show only a subset of all child hairs and particles.
Texture Limit
   Automatically scales textures down so that they are no larger than the values chosen.
   This can help reduce computer memory resources when rendering large scenes with huge textures.
AO Bounces
   Replace global illumination with ambient occlusion after the specified number of bounces.
   This can reduce noise in interior scenes with little visual difference.


Viewport
========

See Common Settings above.

.. _bpy.types.RenderSettings.simplify_volumes:

Volume Resolution
   Resolution percentage of :doc:`volume objects </modeling/volumes/index>` in the viewport.
   This mostly affects memory usage rather than computation times.


Render
======

See Common Settings above.


.. _bpy.types.CyclesRenderSettings.use_camera_cull:
.. _bpy.types.CyclesRenderSettings.camera_cull_margin:
.. _bpy.types.CyclesRenderSettings.use_distance_cull:
.. _bpy.types.CyclesRenderSettings.distance_cull_margin:

Culling
=======

Camera Cull
   Automatically culls objects based on the camera frustum defined by the *Margin*.
Distance Cull
   Automatically culls objects based on their distance from the active camera.
   This is set via the *Distance* property.


.. _bpy.types.RenderSettings_simplify_gpencil:
.. _bpy.types.RenderSettings_simplify_gpencil_onplay:
.. _bpy.types.RenderSettings_simplify_gpencil_view_fill:
.. _bpy.types.RenderSettings_simplify_gpencil_view_modifier:
.. _bpy.types.RenderSettings_simplify_gpencil_shader_fx:
.. _bpy.types.RenderSettings_simplify_gpencil_tint:
.. _bpy.types.RenderSettings.simplify_gpencil_antialiasing:

Grease Pencil
=============

Playback Only
   Activates the simplification process only during animation playback.
Fill
   Shows the fill component in Grease Pencil materials.
Modifiers
   Shows Grease Pencil :doc:`modifiers </grease_pencil/modifiers/index>`.
Shader Effects
   Shows Grease Pencil :doc:`visual effects </grease_pencil/modifiers/index>`.
Layer Tinting
   Shows layers tint overrides.
Anti-Aliasing
   Use :term:`Anti-Aliasing` to smooth stroke edges. The amount of anti-aliasing can be adjusted by
   the :ref:`Anti-Aliasing Threshold <bpy.types.SceneGpencil.antialias_threshold>`.

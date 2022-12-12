.. _bpy.types.CyclesMaterialSettings:

*****************
Material Settings
*****************

.. reference::

   :Panel:     :menuselection:`Material --> Settings` and :menuselection:`Shader Editor --> Sidebar --> Settings`


Surface
=======

.. _bpy.types.CyclesMaterialSettings.displacement:

Displacement Method
   Method used to perform :doc:`Displacement </render/materials/components/displacement>` on materials.

   :Displacement Only:
      Mesh vertices will be displaced before rendering, modifying the actual mesh.
      This gives the best quality results, if the mesh is finely subdivided.
      As a result, this method is also the most memory intensive.
   :Bump Only:
      When executing the surface shader, a modified surface normal is used instead of the true normal.
      This is a less memory intensive alternative to actual displacement, but only an approximation.
      Surface silhouettes will not be accurate and there will be no self-shadowing of the displacement.
   :Displacement and Bump:
      Both methods can be combined, to do displacement on a coarser mesh,
      and use bump mapping for the final detail.

.. _bpy.types.CyclesMaterialSettings.emission_sampling:

Emission Sampling
   The method used for sampling the emissive component of the material.
   This option will only have an influence if the material contains an emissive material node,
   otherwise it will be ignored.

   :None:
      Do not use this surface as a light for sampling.
   :Auto:
      Automatically determine if the surface should be treated as a light for sampling based on
      emission intensity.
   :Front:
      Treat only the front side of the surface as a light, useful for closed meshes whose interior
      is not visible.
   :Back:
      Treat only the back side of the surface as a light for sampling.
   :Front and Back:
      Treat surface as a light for sampling, emitting from both the front and back side.

.. _bpy.types.CyclesMaterialSettings.use_transparent_shadow:

Transparent Shadows
   Use transparent shadows if it contains a :doc:`Transparent BSDF </render/shader_nodes/shader/transparent>`,
   disabling will render faster but will not give accurate shadows.


Volume
======

.. _bpy.types.CyclesMaterialSettings.volume_sampling:

Sampling Method
   :Distance: For dense volumes lit from far away *Distance* sampling is usually more efficient.
   :Equiangular: If you have got a light inside or near the volume then *equiangular* sampling is better.
   :Multiple Importance: If you have a combination of both, then the multiple importance sampling will be better.

.. _bpy.types.CyclesMaterialSettings.volume_interpolation:

Interpolation
   Interpolation method to use for the volume objects and smoke simulation grids.

   :Linear: Simple interpolation which gives good results for thin volumes.
   :Cubic: Smoothed high-quality interpolation needed for more dense volumes, but slower.

.. _bpy.types.CyclesMaterialSettings.homogeneous_volume:

Homogeneous
   Assume volume has the same density everywhere (not using any textures), for faster rendering.
   For example absorption in a glass object would typically not have any textures,
   and so the renderer can be set to avoid taking small steps to sample the volume shader.
   Usually this is automatically determined by the renderer.
   This setting provides a manual control for cases where it is not detected.

.. _bpy.types.CyclesMaterialSettings.volume_step_rate:

Step Rate
   Adjust distance between volume shader samples for volume shaders.
   This is typically used to reduce the step size for procedural shaders that add more detail
   with procedural textures, when it is not captured by the default step size.
   See :doc:`Volume Render Settings </render/cycles/render_settings/volumes>` for more information.

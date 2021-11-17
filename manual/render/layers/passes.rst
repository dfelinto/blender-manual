.. _bpy.types.RenderLayer:

******
Passes
******

.. reference::

   :Panel:     :menuselection:`Scene --> View Layers --> Passes`

Passes can be used to split rendered images into colors, direct and indirect light to edit them individually,
and also to extract data such as depth or normals.


.. _render_layers_passes_data:

Data
====

Cycles
------

Include
   Combined
      The final combination of render passes with everything included.
   Z
      Distance to any visible surfaces.

      .. note::

         The Z pass only uses one sample.
         When depth values need to be blended in case of motion blur or :term:`Depth of Field`, use the mist pass.
   Mist
      Distance to visible surfaces, mapped to the 0.0 - 1.0 range.
      When enabled, settings are in :ref:`World tab <bpy.types.WorldMistSettings>`.
      This pass can be used in compositing to fade out objects that are farther away.
   Position
      World position of objects in the scene.
   Normal
      Surface normal used for shading.
   Vector
      Motion vectors for the Vector Blur node. The four components consist of 2D vectors
      giving the motion towards the next and previous frame position in pixel space.
   UV
      Mapped UV coordinates, used to represent where on a mesh a texture gets mapped too.
      This is represented through the red and green channels of the image.
      The blue channel is encoded with a constant value of 1 but does not hold any information.
   Denoising Data
      Passes needed by the denoiser, for performing animation denoising
      in a second pass after rendering the entire animation.
      For still image denoising as part of the render process these are not needed.
      This also includes a render pass of the original combined pass before denoising.
      Note, the passes adapt to the :ref:`denoiser <render-cycles-settings-viewport-denoising>`
      selected for rendering.

   .. note:: The Z, Object Index, and Material Index passes are not anti-aliased.

Indexes
   Object Index
      Creates a mask of the object that can be later read by
      the :doc:`ID Mask Node </compositing/types/converter/id_mask>` in the Compositor.
   Material Index
      Creates a mask of the material that can be later read by
      the :doc:`ID Mask Node </compositing/types/converter/id_mask>` in the Compositor.

Debug
   Render Time
      Render time in milliseconds per sample and pixel.
   Sample Count
      Number of samples/camera rays per pixel.

Alpha Threshold
   Z, Index, normal, UV and vector passes are
   only affected by surfaces with alpha transparency equal to or higher than this threshold.
   With value 0.0 the first surface hit will always write to these passes, regardless of transparency.
   With higher values surfaces that are mostly transparent can be skipped until an opaque surface is encountered.


Eevee
-----

Include
   Combined
      The final combination of render passes with everything included.
   Z
      Distance to any visible surfaces.
   Mist
      Distance to visible surfaces, mapped to the 0.0 - 1.0 range.
   Normal
      Surface normal used for shading.


Light
=====

Cycles
------

Diffuse
   Direct
      Direct lighting from diffuse and subsurface BSDFs.
      We define direct lighting as coming from lights, emitting surfaces,
      the background, or ambient occlusion after a single reflection or transmission off a surface.
      BSDF color is not included in this pass.
   Indirect
      Indirect lighting from diffuse and subsurface BSDFs. We define indirect lighting as coming from lights,
      emitting surfaces or the background after more than one reflection or transmission off a surface.
      BSDF color is not included in this pass.
   Color
      Color weights of diffuse and subsurface BSDFs.
      These weights are the color input socket for BSDF nodes, modified by any Mix and Add Shader nodes.

Glossy
   Direct, Indirect, Color
      Same as above, but for glossy BSDFs.

Transmission
   Direct, Indirect, Color
      Same as above, but for transmission BSDFs.

Volume
   Direct, Indirect
      Same as above, but for volumetric BSDFs.

Other
   Emission
      Emission from directly visible surfaces.
   Environment
      Emission from the directly visible background. When the film is set to transparent,
      this can be used to get the environment color and composite it back in.
   Shadow
      Shadows from light objects. Mostly useful for compositing objects with shadows into existing footage.
   Ambient Occlusion
      Ambient occlusion from directly visible surfaces. BSDF color or AO factor is not included; i.e.
      it gives a 'normalized' value between 0 and 1.
   Shadow Catcher
      Extra indirect light information collected by objects with
      the :ref:`Shadow Catcher <render-cycles-object-settings-visibility>` option enabled.
      Multiply this pass with existing footage using the :doc:`/compositing/types/color/mix` in the
      :doc:`Compositor </editors/compositor>` to add the indirect lighting information to the footage.

.. note::

   :doc:`Transparent BSDFs are given special treatment </render/cycles/render_settings/light_paths>`.
   A fully transparent surface is treated as if there is no surface there at all;
   a partially transparent surface is treated as if only part of the light rays can pass through.
   This means it is not included in the Transmission passes;
   for that a glass BSDF with index of refraction 1.0 can be used.


Eevee
-----

Diffuse
   Light
      Direct lighting from diffuse BSDFs. We define lighting as coming from lights,
      the background, or ambient occlusion off a surface.
      BSDF color is not included in this pass.
   Color
      Color weights of diffuse BSDFs. These weights are the color input socket for BSDF nodes,
      modified by any Mix and Add Shader nodes.

Specular
   Light, Color
      Same as above, but for specular BSDFs.

Volume
   Light
      The scattering pass from volume objects or world.

Other
   Emission
      Emission from directly visible surfaces.
   Environment
      Emission from the directly visible background. When the film is set to transparent,
      this can be used to get the environment color and composite it back in.
   Shadow
      Shadows from light objects. Mostly useful for compositing objects with shadow into existing footage.
   Ambient Occlusion
      Ambient occlusion from directly visible surfaces. BSDF color or AO factor is not included; i.e.
      it gives a 'normalized' value between 0 and 1.


Effects
=======

:guilabel:`Eevee only`

Bloom
   The influence of the Bloom effect.


Cryptomatte
===========

Cryptomatte is a standard to efficiently create mattes for compositing.
Cycles outputs the required render passes, which can then be used in the Blender Compositor
or another compositor with Cryptomatte support to create masks for specified objects.

Unlike the Material and Object Index passes, the objects to isolate are selected in compositing.
The mattes will be anti-aliased and take into account effects like motion blur and transparency.

.. _bpy.types.ViewLayer.use_pass_cryptomatte_object:

Object
   Render cryptomatte object pass, for isolating objects in compositing.

.. _bpy.types.ViewLayer.use_pass_cryptomatte_material:

Material
   Render cryptomatte material pass, for isolating materials in compositing.

.. _bpy.types.ViewLayer.use_pass_cryptomatte_asset:

Asset
   Render cryptomatte asset pass, for isolating groups of objects with
   the same :doc:`parent </scene_layout/object/editing/parent>` in compositing.

.. _bpy.types.ViewLayer.pass_cryptomatte_depth:

Levels
   Sets how many unique objects can be distinguished per pixel.


Typical Workflow
----------------

#. Enable Cryptomatte Object render pass in the Passes panel, and render.
#. In the compositing nodes, create a Cryptomatte node and
   link the Render Layer matching Image and Cryptomatte passes to it.
#. Attach a Viewer node to the Pick output of the Cryptomatte node.
#. Use the Cryptomatte Add/Remove button to sample objects in the Pick Viewer node.
#. Use the Matte output of the Cryptomatte node to get the alpha mask.

.. seealso::

   :doc:`Cryptomatte Node </compositing/types/matte/cryptomatte>`.


.. _bpy.types.AOV:

Shader AOV
==========

Shader AOVs (Arbitrary Output Variables) provide custom render passes for any shader node components.
As an artist this can be a good way to fix or tweak fine details of a scene in post-processing.
To use Shader AOVs create the pass in the *Shader AOV* panel then reference this pass with
the :doc:`AOV Output </render/shader_nodes/output/aov>` shading node.
Shader AOVs can be added or removed in the *Shader AOV* panel.
In this panel is a list of all AOV passes; each AOV in the list consists of a *Name* and *Data Type*.

.. _bpy.types.ViewLayer.active_aov_index:

Active AOV Index
   The name of the render pass; this is the *Name* that is referenced in the *AOV Output* node.
   Any names can be used for these passes,
   as long as they do not conflict with built-in passes that are enabled.

.. _bpy.types.AOV.type:

Data Type
   Shader AOVs can either express a *Color* or a *Value* output.
   The *Color* type as the name suggest can be used for a color but also for normals.
   A *Value* type can be used for any single numerical value.


Combining
=========

Cycles
------

All these lighting passes can be combined to produce the final image as follows:

.. figure:: /images/render_layers_passes_combine.svg


Eevee
-----

The passes can be combined to produce the final image as follows:

.. figure:: /images/render_layers_passes_eevee-combine.svg


Known Limitations
=================

- Alpha blended materials are not rendered in render passes except the combined pass.
  Use the *Alpha Clip* or *Alpha Hashed* as :ref:`Blending Mode <bpy.types.Material.blend_method>`
  to render transparent materials in render passes.
- Depth of field is not rendered in render passes except the combined pass.
  It is possible to add the depth of field back in the Compositor using
  the :ref:`Defocus node <bpy.types.CompositorNodeDefocus>`.
- Eevee render passes exclude parts of the BSDF equation.
  :doc:`Shader to RGB </render/shader_nodes/converter/shader_to_rgb>` is not supported as it needs
  the full BSDF equation.

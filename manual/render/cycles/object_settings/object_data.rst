
******
Object
******

.. _render-cycles-object-settings-visibility:

Visibility
==========

.. reference::

   :Panel:     :menuselection:`Object Properties --> Visibility`

.. seealso::

   There are several other :doc:`general visibility </scene_layout/object/properties/visibility>` properties.

.. _bpy.types.Object.is_shadow_catcher:

Mask
   Shadow Catcher
      Enables the object to only receive shadow rays. It is to be noted that,
      shadow catcher objects will interact with other CG objects via indirect light interaction.
      This simplifies compositing :abbr:`CGI (Computer-Generated Imagery)` elements into real-world footage.

      .. note::

         The *Shadow Catcher* outputs different results depending on if the *Shadow Catcher* pass is enabled in
         :ref:`Render Layer <render_layers_passes_data>` settings. With the *Shadow Catcher* pass enabled, all
         indirect light interactions are captured. With it disabled, a simple approximation is used instead.
         The simple approximation is used in viewport rendering.

      .. figure:: /images/render_cycles_object-settings_object-data_shadow-catcher.jpg

         Example of the shadow catcher. Note how the material of the plane can still be viewed in the spheres.


.. _cycles-ray-visibility:

Ray Visibility
--------------

Objects can be set to be invisible to particular ray types.
This can be used, for example, to make an emitting mesh invisible to camera rays.
For instanced objects, visibility is inherited; if the parent object is hidden for some ray types,
the children will be hidden for these too.

In terms of performance, using these options is more efficient that using a shader node setup
that achieves the same effect.
Objects invisible to a certain ray will be skipped in ray traversal already,
leading to fewer ray casts and shader executions.

.. _bpy.types.Object.visible_camera:

Camera
   Makes the object visible in camera rays.

.. _bpy.types.Object.visible_diffuse:

Diffuse
   Makes the object visible in diffuse rays.

.. _bpy.types.Object.visible_glossy:

Glossy
   Makes the object visible in glossy rays.

.. _bpy.types.Object.visible_transmission:

Transmission
   Makes the object visible in transmission rays.

.. _bpy.types.Object.visible_volume_scatter:

Volume Scatter
   Makes the object visible in transmission rays.

.. _bpy.types.Object.visible_shadow:

Shadow
   Enables the object to cast shadows.


Culling
-------

In order to activate these options the respectively camera cull options have to be enabled
in the scene :ref:`simplify panel <render-cycles-settings-scene-simplify-culling>`.

.. _bpy.types.CyclesObjectSettings.use_camera_cull:

Use Camera Cull
   Ignore and this way make objects invisible to rays outside of the camera frustum.

.. _bpy.types.CyclesObjectSettings.use_distance_cull:

Use Distance Cull
   Will cull any objects further from the camera than a given distance. When used in combination with
   camera frustum culling, this can be used to avoid culling nearby objects that are outside the camera frustum,
   but still visible in reflections. It is also useful to cull small objects far from the camera.


.. _bpy.types.CyclesObjectSettings.use_motion_blur:

Motion Blur
===========

.. reference::

   :Panel:     :menuselection:`Properties --> Object Properties --> Motion Blur`

Each object has its own motion blur settings along with
the :doc:`Scene Level Motion Blur </render/cycles/render_settings/motion_blur>`.
These settings can be found in the Object Properties tab of the Properties.

.. _bpy.types.CyclesObjectSettings.motion_steps:

Steps
   Controls accuracy of deformation motion blur, more steps uses more memory.
   The actual number of time steps is :math:`2^{steps -1}`.

.. _bpy.types.CyclesObjectSettings.use_deform_motion:

Deformation
   Enables motion blur for deformed meshes such as animated characters, including hair.

   .. warning::

      An object modifier setup that changes mesh topology over time can not render
      deformation motion blur correctly. Deformation blur should be disabled for such objects.
      Common examples of this are animated Booleans, Deformation
      before Edge Split, Remesh, Skin or Decimate modifiers.


Shading
=======

.. reference::

   :Panel:     :menuselection:`Properties --> Object Properties --> Shading`


Shadow Terminator
-----------------

.. _bpy.types.CyclesObjectSettings.shadow_terminator_geometry_offset:

Geometry Offset
   Offset rays from the surface to reduce shadow terminator artifacts on low-poly geometry.
   Higher values affect more triangles, a value of one affecting all triangles and zero having no affect.
   The default value only affects triangles at grazing angles to light and should eliminate most artifacts.

   Unlike the *Shading Offset*, this option has little affect on the lighting
   making it the preferable method to handle shadow terminator artifacts.

.. _bpy.types.CyclesObjectSettings.shadow_terminator_offset:

Shading Offset
   Pushes the shadow terminator (the line that divides the light and dark) towards the light
   to hide artifacts on low-poly geometry such as the ones below:

   .. list-table::

      * - .. figure:: /images/render_cycles_object-settings_object-data_shading-terminator1.jpg

             Shadow Terminator Artifacts.

        - .. figure:: /images/render_cycles_object-settings_object-data_shading-terminator2.jpg

             Result of using an offset of 0.15.

   .. note::

      This property artificially alters the scene's lighting
      and is not energy conserving and consequently not physically accurate (see *Geometry Offset* instead).


Fast GI Approximation
---------------------

.. _bpy.types.CyclesObjectSettings.ao_distance:

AO Distance
   Override for the world's :ref:`AO Distance <bpy.types.CyclesRenderSettings.use_fast_gi>`,
   if the value is zero the world's distance is used.


Caustics
--------

Mark objects as caustic casters or receivers. This is used in conjunction with a
:ref:`Light <bpy.types.CyclesLightSettings.is_caustics_light>` or
:ref:`World Shader <bpy.types.CyclesWorldSettings.is_caustics_light>` with *Shadow Caustics* enabled
to selectively speed up caustic rendering of objects in your scene. 

.. note:: 

   The rendering technique used to speed up the rendering of caustics is based on
   :abbr:`MNEE (Manifold Next Event Estimation)`. There are a number of limitations with this technique
   and it's implementation in Cycles:   

   - Only refractive caustics in the shadows of objects work. Caustics from reflections or caustics that
     fall outside shadows are not rendered with this technique.

   - MNEE Caustics are not supported when the microfacet distribution is set to *Multiscatter GGX*.

   - :ref:`Filter Glossy <bpy.types.CyclesRenderSettings.blur_glossy>` settings are ignored when using
     MNEE for refractive caustics.

   - MNEE Caustic rays can pass through up to 6 Caustic Caster surfaces between a Caustic Reciever and a
     Shadow Caustic light before the ray is terminated and caustics are ignored.

   - MNEE Caustics are treated as direct lighting instead of indirect lighting.

   - MNEE Caustics render best with objects with smooth normals.

   - Volumetric materials can not recieve MNEE caustics.

   - Bump and normal maps are ignored when calculating caustics.

   - The Metal GPU rendering backend is not supported.

.. _bpy.types.CyclesObjectSettings.is_caustics_caster:

Cast Shadow Caustics
   Mark an object as a caustic caster.

.. _bpy.types.CyclesObjectSettings.is_caustics_receiver:

Receive Shadow Caustics
   Mark an object as a caustic receiver.

.. list-table::

   * - .. figure:: /images/render_cycles_object-settings_caustics-example1.png

          Rendering caustics inside an eye without MNEE at 32 samples per pixel.

     - .. figure:: /images/render_cycles_object-settings_caustics-example2.png

          Rendering caustics inside an eye using MNEE at 32 samples per pixel.

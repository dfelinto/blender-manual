
******
Object
******

.. _render-cycles-object-settings-visibility:

Visibility
==========

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Object Properties --> Visibility`

.. seealso::

   There are several other :doc:`general visibility </scene_layout/object/properties/visibility>` properties.

Mask
   Shadow Catcher
      Enables the object to only receive shadow rays. It is to be noted that,
      shadow catcher objects will interact with other CG objects via indirect light interaction.
      This simplifies compositing :abbr:`CGI (Computer-Generated Imagery)` elements into real-world footage.

      .. figure:: /images/render_cycles_object-settings_object-data_shadow-catcher.jpg

         Example of the shadow catcher. Note how the material of the plane can still be viewed in the spheres.

   Holdout
      Render objects as a holdout or matte, creating a hole in the image with zero :term:`Alpha <Alpha Channel>`,
      to fill out in :doc:`compositing </compositing/index>` with real footage or another render.


.. _cycles-ray-visibility:
.. _bpy.types.CyclesVisibilitySettings:

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

Camera
   Makes the object visible in camera rays.
Diffuse
   Makes the object visible in diffuse rays.
Glossy
   Makes the object visible in glossy rays.
Transmission
   Makes the object visible in transmission rays.
Volume Scatter
   Makes the object visible in transmission rays.
Shadow
   Enables the object to cast shadows.


Culling
-------

In order to activate these options the respectively camera cull options have to be enabled
in the scene :ref:`simplify panel <render-cycles-settings-scene-simplify>`.

Use Camera Cull
   Ignore and this way make objects invisible to rays outside of the camera frustum.
Use Distance Cull
   Will cull any objects further from the camera than a given distance. When used in combination with
   camera frustum culling, this can be used to avoid culling nearby objects that are outside the camera frustum,
   but still visible in reflections. It is also useful to cull small objects far from the camera.


.. _render-cycles-settings-object-motion-blur:

Motion Blur
===========

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Object Properties --> Motion Blur`

Each object has its own motion blur settings along with
the :doc:`Scene Level Motion Blur </render/cycles/render_settings/motion_blur>`
These settings can be found
in the Object Properties tab of the Properties.

Steps
   Controls accuracy of deformation motion blur, more steps uses more memory.
   The actual number of time steps is :math:`2^{steps -1}`.

Deformation
   Enables motion blur for deformed meshes such as animated characters, including hair.

   .. warning::

      An object modifier setup that changes mesh topology over time can not render
      deformation motion blur correctly. Deformation blur should be disabled for such objects.
      Common examples of this are animated Booleans, Deformation
      before Edge Split, Remesh, Skin or Decimate modifiers.


Shading
=======

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Object Properties --> Shading`

Shadow Terminator Offset
   Pushes the shadow terminator (the line that divides the light and dark) towards the light
   to hide artifacts on low-poly geometry such as the ones below:

   .. list-table::

      * - .. figure:: /images/render_cycles_object-settings_object-data_1.jpg

             Shadow Terminator Artifacts.

        - .. figure:: /images/render_cycles_object-settings_object-data_2.jpg

             Result of using an offset of 0.15.

   .. note::

      This property artificially alters the scene's lighting
      and is not energy conserving and consequently not physically accurate.

.. _bpy.types.ShaderNodeLightPath:

***************
Light Path Node
***************

.. figure:: /images/node-types_ShaderNodeLightPath.webp
   :align: right
   :alt: Light Path Node.

The *Light Path* node is used to find out for which kind of incoming ray the shader is being executed;
particularly useful for non-physically-based tricks. More information about the meaning of each type
is in the :doc:`Light Paths </render/cycles/render_settings/light_paths>` documentation.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Is Camera Ray
   1.0 if shading is executed for a camera ray, otherwise 0.0.
Is Shadow Ray
   1.0 if shading is executed for a shadow ray, otherwise 0.0.
Is Diffuse Ray
   1.0 if shading is executed for a diffuse ray, otherwise 0.0.
Is Glossy Ray
   1.0 if shading is executed for a glossy ray, otherwise 0.0.
Is Singular Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a singular ray, otherwise 0.0.
Is Reflection Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a reflection ray, otherwise 0.0.
Is Transmission Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a transmission ray, otherwise 0.0.
Ray Length :guilabel:`Cycles Only`
   Distance traveled by the light ray from the last bounce or camera.
Ray Depth
   Number of times the ray has been reflected or transmitted on interaction with a surface.

   .. note::

      Passing through a transparent shader
      :ref:`does not count as a normal "bounce" <render-cycles-light-paths-transparency>`.

Diffuse Depth :guilabel:`Cycles Only`
   Number of times the ray has gone through diffuse reflection or transmission.
Glossy Depth :guilabel:`Cycles Only`
   Number of times the ray has gone through glossy reflection or transmission.
Transparent Depth :guilabel:`Cycles Only`
   Returns the number of transparent surfaces passed through.
Transmission Depth :guilabel:`Cycles Only`
   Replace a Transmission light path after X bounces with another shader, e.g. a Diffuse one.
   This can be used to avoid black surfaces, due to low amount of max bounces.


Eevee Support
=============

Eevee has no real concept of rays. But in order to ease the workflow between Cycles and Eevee
some of the outputs are supported in particular cases.
This node makes it possible to tweak indirect lighting in the shader.

Only a subset of the outputs is supported and the ray depth does not exactly have the same meaning.
In order for *Is Camera*, *Is Shadow*, *Is Diffuse*, and *Is Glossy* outputs to work the object
must be inside an :doc:`Irradiance Volume </render/eevee/light_probes/irradiance_volumes>`
and bake :doc:`/render/eevee/render_settings/indirect_lighting`.

- *Is Camera*: Supported.
- *Is Shadow*: Supported.
- *Is Diffuse*: Supported.
- *Is Glossy*: Supported.
- *Is Singular*: Not supported. Same as Is Glossy.
- *Is Reflection*: Not supported. Same as Is Glossy.
- *Is Transmission*: Not supported. Same as Is Glossy.
- *Ray Length*: Not supported. Defaults to 1.0.
- *Ray Depth*: Indicates the current bounce when baking the light cache.
- *Diffuse Depth*: Same as Ray Depth but only when baking diffuse light.
- *Glossy Depth*: Same as Ray Depth but only when baking specular light.
- *Transparent Depth*: Not supported. Defaults to 0.
- *Transmission Depth*: Not supported. Same as Glossy Depth.

.. note::

   *Is Glossy* does not work with Screen Space Reflections/Refractions
   but does work with reflection planes (whether used with SSR or not).

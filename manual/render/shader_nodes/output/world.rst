.. _bpy.types.ShaderNodeOutputWorld:

**********
World Node
**********

.. figure:: /images/render_shader-nodes_output_world_node.png
   :align: right

   World Node.

The *World Output* node is used to output light a color information
to the scene's :doc:`World </render/lights/world>`.


Inputs
======

Surface
   The appearance of the environment,
   usually preceded by a :doc:`Background </render/shader_nodes/shader/background>` shader.
Volume
   Used to add volumetric effects to the world.
   See the shaders :doc:`Volume Absorption </render/shader_nodes/shader/volume_absorption>`
   and :doc:`Volume Scatter </render/shader_nodes/shader/volume_scatter>` for more information.

   .. note::

      It is not possible to have an HDR and volumetric due to the fact that
      HDR's are assumed to be an infinite distance from the camera.


Properties
==========

Target
   Render engine the input shaders are used for.
   By default shaders are shared between Cycles and Eevee,
   with multiple output nodes specialized shader setups can be created for each.


Outputs
=======

This node has no outputs.

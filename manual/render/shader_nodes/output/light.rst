.. _bpy.types.ShaderNodeOutputLight:

**********
Light Node
**********

.. figure:: /images/render_shader-nodes_output_light_node.png
   :align: right

   Light Node.

The *Light Output* node is used to output light information to a light object.


Inputs
======

Surface
   Shading for the surface of the :doc:`light object </render/lights/light_object>`.


Properties
==========

Target
   Render engine the input shaders are used for.
   By default shaders are shared between Cycles and Eevee,
   with multiple output nodes specialized shader setups can be created for each.


Outputs
=======

This node has no outputs.

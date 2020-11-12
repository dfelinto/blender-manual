.. _bpy.types.ShaderNodeOutputMaterial:

*************
Material Node
*************

.. figure:: /images/render_shader-nodes_output_material_node.png
   :align: right

   Material Node.

The *Material Output* node is used to output surface material information to a surface object.


Inputs
======

Surface
   Shading for the :doc:`surface </render/materials/components/surface>` of the object.
Volume
   Shading for the :doc:`volume </render/materials/components/volume>` inside the object.
Displacement
   Used to create bump mapping or actual subdivided :doc:`displacement </render/materials/components/displacement>`.


Properties
==========

Target
   Render engine the input shaders are used for.
   By default shaders are shared between Cycles and Eevee,
   with multiple output nodes specialized shader setups can be created for each.


Outputs
=======

This node has no outputs.

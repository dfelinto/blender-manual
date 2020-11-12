.. _bpy.types.ShaderNodeHairInfo:

**************
Hair Info Node
**************

.. figure:: /images/render_shader-nodes_input_hair-info_node.png
   :align: right

   Hair Info Node.

The *Hair Info* node gives access to :doc:`Hair </physics/particles/hair/index>` information.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Is Strand
   Returns 1 when the shader is acting on a strand, otherwise 0.
Intercept
   The point along the strand where the ray hits the strand (1 at the tip and 0 at the root).
Thickness
   The thickness of the strand at the point where the ray hits the strand.
Tangent Normal
   Tangent normal of the strand.
Random
   A random per-hair value in the range from 0 to 1.
   It can for example be used in combination with a color ramp, to randomize the hair color.

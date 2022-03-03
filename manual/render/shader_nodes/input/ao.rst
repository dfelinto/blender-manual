.. _bpy.types.ShaderNodeAmbientOcclusion:

*****************
Ambient Occlusion
*****************

.. figure:: /images/render_shader-nodes_input_ao_node.png
   :align: right
   :alt: Ambient Occlusion node.

The *Ambient Occlusion* shader computes how much the hemisphere above the shading point is occluded.
This can be used for procedural texturing, for example to add weathering effects to corners only.

For Cycles, this is an expensive shader and can slow down render significantly.
If render time is a concern, using Pointiness from the Geometry node or baking Ambient Occlusion will render faster.


Inputs
======

Color
   Tint for AO output color.
Distance :guilabel:`Cycles Only`
   Distance up to which other objects are considered to occlude the shading point.
Normal
   Normal used for ambient occlusion; if nothing is connected the default shading normal is used.


Properties
==========

Samples :guilabel:`Cycles Only`
   Number of samples to use for ray-traced ambient occlusion sampling.
   Keep as low as possible for optimal performance.
Inside :guilabel:`Cycles Only`
   Detect convex rather than concave shapes, by computing occlusion inside mesh.
Only Local :guilabel:`Cycles Only`
   Only detect occlusion from the object itself, and not others.


Outputs
=======

Color
   Ambient occlusion with color tint.
AO
   Ambient occlusion factor without color tint.


Example
=======

.. figure:: /images/render_shader-nodes_input_ao_example.jpg

   White AO shader.

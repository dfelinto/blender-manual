.. _bpy.types.ShaderNodeBevel:

**********
Bevel Node
**********

:guilabel:`Cycles Only`

.. figure:: /images/render_shader-nodes_input_bevel_node.png
   :align: right

   Bevel Node.

The Bevel shader node can be used for rendering rounded corners.
Like bump mapping, this does not modify the actual geometry, only the shading is affected.
Slight rounding on edges helps to capture specular highlights that you would also see in the real world.

Note that this is a very expensive shader, and may slow down renders
by 20% even if there is a lot of other complexity in the scene.
For that reason, we suggest to mainly use this for baking or
still frame renders where render time is not as much of an issue.
The Bevel modifier is a faster option when it works, but sometimes fails on complex or messy geometry.


Inputs
======

Radius
   Width of the bevel effect on edges.
Normal
   Normal to apply bevel on top of, to be combined with a Bump node for example.


Properties
==========

Samples
   Number of samples to take for each shader evaluation.
   More samples give more accurate results, but are also slower to render.
   The default value of 4 works well for most cases, with any noise resolved by using more AA samples.


Outputs
=======

Normal
   Standard normal output.


Examples
========

.. figure:: /images/render_shader-nodes_input_bevel_example.jpg

   Bevel shader bringing out specular highlights on the edges.

.. _bpy.types.ShaderNodeTexBrick:

******************
Brick Texture Node
******************

.. figure:: /images/render_shader-nodes_textures_brick_node.png
   :align: right

   Brick Texture Node.

The *Brick Texture* is used to add a procedural texture producing bricks.


Inputs
======

Color 1/2 and Mortar
   Color of the bricks and mortar.
Scale
   Overall texture scale.
Mortar Size
   The size of the filling between the bricks known as "mortar"; 0 means no mortar.
Mortar Smooth
   Blurs/softens the edge between the mortar and the bricks.
   This can be useful with a texture and displacement textures.
Bias
   The color variation between *Color 1/2*.
   Values of -1 and 1 only use one of the two colors; values in between mix the colors.
Brick Width
   The width of the bricks.
Row Height
   The height of the brick rows.


Properties
==========

Offset
   Determines the brick offset of the various rows.
Frequency
   Determines the offset frequency. A value of 2 gives an even/uneven pattern of rows.
Squash
   Amount of brick squashing.
Frequency
   Brick squashing frequency.


Outputs
=======

Color
   Texture color output.
Factor
   Mortar mask (1 = mortar).


Examples
========

.. figure:: /images/render_shader-nodes_textures_brick_example.jpg
   :width: 200px

   Brick texture: Colors changed, Squash 0.62, Squash Frequency 3.

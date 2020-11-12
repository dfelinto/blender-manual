.. _bpy.types.ShaderNodeTexWave:

*****************
Wave Texture Node
*****************

.. figure:: /images/render_shader-nodes_textures_wave_node.png
   :align: right

   Wave Texture Node.

The *Wave Texture* node adds procedural bands or rings with noise distortion.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Scale
   Overall texture scale.
Distortion
   Amount of distortion of the wave.
Detail
   Amount of distortion noise detail.
Detail Scale
   Scale of distortion noise.
Roughness
   Blend between a smoother noise pattern, and rougher with sharper peaks.
Phase Offset
   Position of the wave along the *Bands Direction*.
   This can be used as an input for more control over the distortion.


Properties
==========

Type
   *Bands* or *Rings* shaped waves.
Bands/Rings Direction
   The axis the bands or rings propagate from i.e. which axis they are perpendicular to.
   When using *Bands* a *Diagonal* axis is an option and when using *Rings* the rings
   can propagate outwards from a single point by using *Spherical* direction.
Wave Profile
   Controls the look of the wave type.

   Saw
      Uses a sawtooth profile.
   Sine
      Uses the standard sine profile.


Outputs
=======

Color
   Texture color output.
Factor
   Texture intensity output.


Examples
========

.. figure:: /images/render_shader-nodes_textures_wave_example.png

   Wave Texture.

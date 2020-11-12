.. _bpy.types.ShaderNodeVolumeScatter:

**************
Volume Scatter
**************

.. figure:: /images/render_shader-nodes_shader_volume-scatter_node.png
   :align: right

   Volume Scatter Shader.

The *Volume Scatter* node allows light to be scattered as it passes through the volume.
Typical usage would be to add fog to a scene. It can also be used with
the :doc:`Volume Absorption </render/shader_nodes/shader/volume_absorption>`
node to create smoke.


Inputs
======

Color
   Color of the volume.
Density
   The density of the scatter effect.
Anisotropy
   Controls the look of the scatter effect depending on the direction of the light passing through it.


Properties
==========

Volume
   The Volume Shader output must be plugged into the *Volume Input*
   of the :doc:`Material </render/shader_nodes/output/material>`
   or :doc:`World </render/shader_nodes/output/world>` Output node.


Examples
========

.. figure:: /images/render_shader-nodes_shader_volume-scatter_example.png

   Example of Volume Scatter.

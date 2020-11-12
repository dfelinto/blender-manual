.. _bpy.types.ShaderNodeVolumeInfo:

****************
Volume Info Node
****************

.. figure:: /images/render_shader-nodes_input_volume-info_node.png
   :align: right

   Volume Info Node.

The *Volume Info* node provides information about *Smoke Domains*.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Color
   Smoke color.
Density
   Smoke density.
Flame
   Fire density.
Temperature
   Temperature of the fire.
   Values in the range [0, 1] linearly maps to temperatures in the range [0, 1000] in Kelvin.


Example
=======

.. figure:: /images/render_shader-nodes_input_volume-info_example.jpg

   Smoke density.

.. figure:: /images/render_shader-nodes_input_volume-info_example-fire.jpg

   Computing the color of fire using the *Blackbody* node.
   Since the *Blackbody* node expects its input in Kelvin,
   the temperature output has to be remapped first.

.. _bpy.types.ShaderNodeVolumePrincipled:

*****************
Principled Volume
*****************

.. figure:: /images/render_shader-nodes_shader_volume-principled_node.png
   :align: right

   Principled Volume.

The *Principled Volume* shader combines all volume shading components into
a single easy to use node. Volumes like smoke and fire can be rendered with
a single shader node, which includes scattering, absorption and blackbody emission.


Inputs
======

Color
   Volume scattering color.
Color Attribute
   Volume grid for coloring the volume. Use "color" for smoke simulations.
Density
   Density of the volume.
Density Attribute
   Volume grid to define the density, typically "density".
Anisotropy
   Backward or forward scattering direction.
Absorption Color
   Volume shadow color tint.
Emission Strength
   Amount of light to emit.
Emission Color
   Emission color tint.
Blackbody Intensity
   Blackbody emission for fire. Set to 1 for physically accurate intensity.
Blackbody Tint
   Color tint for blackbody emission.
Temperature
   Temperature in kelvin for blackbody emission, higher values emit more.
Temperature Attribute
   Volume grid to define the temperature, typically "temperature".


Outputs
=======

Volume
   Standard shader output.


Examples
========

.. figure:: /images/render_materials_components_volume_principled.jpg

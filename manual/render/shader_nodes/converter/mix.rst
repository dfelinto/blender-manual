.. _bpy.types.ShaderNodeMix:
.. Editors Note: This page gets copied into:
.. - :doc:`</modeling/geometry_nodes/utilities/mix>`

.. --- copy below this line ---

********
Mix Node
********

The *Mix Node* mixes values, colors and vectors inputs 
using a factor to control the amount of interpolation.
The *Color* mode has additional blending modes.

.. figure:: /images/render_shader-nodes_shader_mix_node.jpg
   :align: right
   :alt: Mix Node.

.. important::
  
   This is a new node as of Blender 3.4. The previous *Mix RGB* node 
   is automatically converted to the Color version of this node in 
   Shader and Geometry node editors.
   Files saved with the new node are not forward compatible.

Inputs
======

Factor
   Controls the amount of mixing between the A and B inputs.
A/B
   The two inputs that are mixed together.


Properties
==========

Data Type
   The data type that is used for mixing. The node supports float, 
   vector and color data types.
   
Factor Mode (Vector only)
   The factor mode can be set to *Uniform* and *Non-Uniform*.   
   In uniform mode, a single float controls the factor.
   In non-uniform mode, a vector controls the factor for
   each XYZ channel separately.

Mix (Color only)
   The Blend modes can be selected in the select menu.
   See :term:`Color Blend Modes` for details on each blending mode.

   Add, Subtract, Multiply, Screen, Divide, Difference,
   Darken, Lighten, Overlay, Color Dodge, Color Burn,
   Hue, Saturation, Value, Color, Soft Light, Linear Light

Clamp Factor
   Limit the factor value between 0.0 and 1.0. If this option is 
   unchecked then the node operates using *Extrapolation*.

Clamp Result (Color only)
   Limit the Result to the range between 0.0 and 1.0.

Outputs
=======

Result
   Output the result of the mix using the data type selected.


Examples
========

See the Color > Mix page for additional examples: 
:doc:`Mix Color Node </render/shader_nodes/color/mix>`
   

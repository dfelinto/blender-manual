.. _bpy.types.ShaderNodeHoldout:

*******
Holdout
*******

.. figure:: /images/render_shader-nodes_shader_holdout_node.png
   :align: right
   :alt: Holdout node.

The *Holdout* shader node is used to create a "hole" in the image with zero alpha
transparency, which is useful for compositing (see :term:`Alpha Channel`).

Note that the holdout shader can only create alpha when
:menuselection:`Properties --> Render --> Film --> Transparent` is enabled.
If it is disabled, the holdout shader will be black.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Holdout
   Standard shader output.


Examples
========

.. figure:: /images/render_shader-nodes_shader_holdout_example.jpg

   The checkered area is a region with zero alpha.

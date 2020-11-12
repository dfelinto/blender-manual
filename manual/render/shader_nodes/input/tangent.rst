.. _bpy.types.ShaderNodeTangent:

************
Tangent Node
************

.. figure:: /images/render_shader-nodes_input_tangent_node.png
   :align: right

   Tangent Node.

The *Tangent* node generates a tangent direction for the Anisotropic BSDF.


Inputs
======

This node has no inputs.


Properties
==========

Direction Type
   The tangent direction can be derived from a cylindrical projection around the X,
   Y, or Z axis (radial), or from a manually created UV Map for full control.


Outputs
=======

Tangent
   The tangent direction vector.

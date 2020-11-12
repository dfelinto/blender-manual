.. _bpy.types.CompositorNodeTexture:

************
Texture Node
************

.. figure:: /images/compositing_node-types_CompositorNodeTexture.png
   :align: right

   Texture Node.

The Texture node makes 3D textures available to the Compositor.


Inputs
======

Offset
   A vector (XYZ) transforming the origin of the texture.
Scale
   A vector (XYZ) to scale the texture.


Properties
==========

Texture
   The texture can be selected from a list of textures available in the current blend-file or linked-in textures.
   The textures themselves can not be edited in the Compositor,
   but in the :doc:`Texture Node Editor </editors/texture_node/index>`.


Outputs
=======

Value
   Gray-scale color values.
Color
   Color values.

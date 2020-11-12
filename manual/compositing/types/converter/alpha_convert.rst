.. _bpy.types.CompositorNodePremulKey:

******************
Alpha Convert Node
******************

.. figure:: /images/compositing_node-types_CompositorNodePremulKey.png
   :align: right

   Alpha Convert Node.

The *Alpha Convert Node* converts the alpha channel interpretation of an image.

For compositing and rendering, premultiplied alpha is the standard in Blender.
Render layers will be premultiplied alpha, and images loaded into rendering
or compositing will be converted to this.

If you want to do a compositing operation with straight alpha,
the *Alpha Convert* node can be used. Typically this would be a color correction operation
where it might give better results working on RGB channels without alpha.
If the alpha is converted to straight in the Compositor,
it should be converted back to premultiplied before the *Composite Output* node,
otherwise some artifacts might occur.


Inputs
======

Image
   Standard image input.


Properties
==========

Mapping
   Straight to Premul, Premul to Straight
      Conversion in both directions. Premul. stands for Premultiplied.
      For details on the difference between both ways to store alpha values see :term:`Alpha Channel`.


Outputs
=======

Image
   Standard image output.

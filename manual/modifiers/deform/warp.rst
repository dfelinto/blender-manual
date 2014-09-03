
..    TODO/Review: {{Review|im= Requires image to show function.}} .


Warp Modifier
*************

.. figure:: /images/26-Manual-Modifiers-Warp-example01.jpg

   Warp modifier


This deformation modifier can be used to warp parts of a mesh to a new location in a very
flexible way by using 2 objects to select the "from" and "to" regions,
with options for using a curve falloff, texture and vertex group.


.. figure:: /images/26-Manual-Modifiers-Warp-example02.jpg

   Warp modifier applied to a grid


The Warp Modifier is a bit tricky at first, but it helps to understand how it works. The modifier requires two points, specified by object centers. The "from" point designates a point in space that is pulled toward the "to" point. It is akin to using the :doc:`Proportional Editing </3d_interaction/transform_control/proportional_edit>` in edit mode.


Options
=======

From:
   Specify the origin object transformation of the warp.
To:
   Specify the destination object transformation of the warp.
Preserve Volume
   Enables volume preservation when rotating one of the transforms.
Vertex Group
   Limit the deformation to a specific vertex group.

Strength
   Sets how strong the effect is.
Radius
   Sets the distance from the transforms that can be warped by the transform handles.
Falloff Type
   Sets the way the strength of the warp change as it goes from the center of the transform to the Radius value. See :doc:`Proportional Editing </3d_interaction/transform_control/proportional_edit>` for descriptions of the falloff types.
Texture
   Specify a texture the strength is offset by to create variations in the displacement.
Texture Coordinates
   Set the way textures are applied to the mesh when using a textured warp.

   Object
      Specify an object to use when set to Object.
   UV Layer
      Specify a UV layer when set to UV.



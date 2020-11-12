.. _bpy.types.CompositorNodeMapUV:

***********
Map UV Node
***********

.. figure:: /images/compositing_node-types_CompositorNodeMapUV.png
   :align: right

   Map UV node.

With this node objects can be "re-textured" after they have been rendered.

To apply a texture to individual enumerated objects
the :doc:`ID Mask Node </compositing/types/converter/id_mask>` could be used.


Inputs
======

Image
   The new 2D texture.
UV
   The input for UV render pass.
   See :doc:`Cycles render passes </render/layers/passes>`.

.. hint::

   To store the UV pass a multi-layer OpenEXR format could be used.


Properties
==========

Alpha
   Alpha threshold is used to fade out pixels on boundaries.


Outputs
=======

Image
   The resulting image is the input image texture distorted to match the UV coordinates.
   That image can then be overlay mixed with the original image to paint
   the texture on top of the original. Adjust alpha and the mix factor to control
   how much the new texture overlays the old.

.. hint::

   When painting the new texture,
   it helps to have the UV maps for the original objects in the scene,
   it is recommended to keep those UV texture outlines around even, when shooting is done.


Examples
========

In the example below,
we have overlaid a grid pattern on top of the two heads after they have been rendered.
During rendering, we enabled the UV layer in the Properties
:menuselection:`Render Layer --> Passes`. Using a Mix node ("Overlay" in figure),
we mix that new UV texture over the original face.
We can use this grid texture to help in any motion tracking that we need to do.

.. figure:: /images/compositing_types_distort_map-uv_example-1.png
   :width: 700px

   Adding a grid UV textures for motion tracking.

In the next example, we overlay a logo on top of a mesh composed of two intersecting cubes,
and we ensure that we Enable the Alpha premultiply button on the Mix node.
The logo is used as additional UV texture on top of the existing texture. Other examples include
the possibility that there was used an unauthorized product box during the initial animation,
and it is needed to substitute in a different product sponsor after rendering.

.. hint::

   Due to limits of this node, it is not recommended to rush pre-production rendering under
   the guise of "fixing it later".

.. figure:: /images/compositing_types_distort_map-uv_example-2.png
   :width: 700px

   Adding UV textures in post-production.

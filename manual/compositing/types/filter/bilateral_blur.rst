.. _bpy.types.CompositorNodeBilateralblur:

*******************
Bilateral Blur Node
*******************

.. figure:: /images/compositing_node-types_CompositorNodeBilateralblur.png
   :align: right

   Bilateral Blur Node.

The Bilateral Blur node performs a high-quality adaptive blur on the source image,
allowing to blur images while retaining their sharp edges.

It can be used for various purposes like: smoothing noisy render passes to avoid longer computation times
in example ray-traced ambient occlusion, blurry refractions/reflections, soft shadows,
or to make non-photorealistic compositing effects.


Inputs
======

Image
   Standard image input.
   If only the image input is connected,
   the node blurs the image depending on the edges present in the source image.
Determinator
   Which is non-obligatory and if the Determinator is connected,
   it serves as the source for defining edges/borders for the blur in the image.
   This has great advantage in case the source image is too noisy,
   but normals in combination with Z-buffer can still define exact borders/edges of objects.


Properties
==========

Iterations
   Defines how many times the filter should perform the operation on the image.
   It practically defines the radius of blur.
Color Sigma
   Defines the threshold for which color differences in the image should be taken as edges.
Space Sigma
   A fine-tuning variable for blur radius.


Outputs
=======

Image
   Standard image output.


Example
=======

.. figure:: /images/compositing_types_filter_bilateral-blur_example-1.png
   :width: 600px

   Bilateral smoothed Ambient Occlusion.
   `blend-file example <https://en.blender.org/uploads/2/2a/Bilateral_blur_example_01.blend>`__

.. list-table::

   * - .. figure:: /images/compositing_types_filter_bilateral-blur_example-1-render.jpg
          :width: 320px

          Render result.

     - .. figure:: /images/compositing_types_filter_bilateral-blur_example-1-composite.jpg
          :width: 320px

          Composite.

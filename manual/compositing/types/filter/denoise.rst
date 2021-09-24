.. _bpy.types.CompositorNodeDenoise:

************
Denoise Node
************

.. figure:: /images/compositing_node-types_CompositorNodeDenoise.png
   :align: right

   Denoise Node.

The Denoise node is used to denoise renders from :doc:`Cycles </render/cycles/index>`
and other ray tracing renderers. This helps to significantly reduce render time by
rendering with fewer samples.

It is uses `Open Image Denoise <https://www.openimagedenoise.org/>`__,
which transforms noisy images into clean images with machine learning.


Inputs
======

Image
   Noisy image input.
Normal
   Optional normal render pass to better preserve detail.
   For Cycles, it is recommended to use the Denoising Normal render pass,
   which is available when enabling the Denoising Data passes.
Albedo
   Optional albedo render pass to better preserve detail.
   For Cycles, it is recommended to use the Denoising Albedo render pass,
   which is available when enabling the Denoising Data passes.


Properties
==========

Prefilter
   :None: 
      Does not apply any prefiltering to the *auxiliary passes*. This option retains the most detail and
      is the fastest, but assumes the *auxiliary passes* are noise free which may require a high sample
      count. If the *auxilary passes* aren't noise free, then noise will remain in the image after 
      denoising.
   :Fast: 
      Assumes the *auxiliary passes* are not noise free, but does not apply prefiltering to the 
      *auxiliary passes*. This option is faster than *Accurate* but produces a blurrier result.
   :Accurate: 
      Prefilters the auxiliary passes before denoising to reduce noise. This option usually produces
      more detailed results than *Fast* with increased processing time.
HDR
   Preserve colors outside the 0 to 1 range.


Outputs
=======

Image
   Denoised image output.


Examples
========

.. figure:: /images/compositing_types_filter_denoise_example.jpg

   Render before and after denoising, with a very low number of samples as input.
   As more samples are used, the denoiser will be able to better preserve detail.

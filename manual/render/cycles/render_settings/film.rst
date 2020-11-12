
****
Film
****

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Film`

Exposure
   This can be used to change the brightness of an image.
   Different than the *Exposure* option found in the :ref:`Color management <render-post-color-management>` panel,
   this exposure option works *on the data* while the Color management exposure is *on the view*.


Pixel Filter
============

Due to limited resolution of images and computer screens, pixel filters are needed to avoid :term:`Aliasing`.
This is achieved by slightly blurring the image to soften edges.

Type
   Pixel Filtering algorithm to use.

   Box
      No filter.
   Gaussian
      Smooth filter.
   Blackman-Harris
      Default filter with a better balance between smoothness and detail preservation.

Width
   Lower values give more crisp renders, higher values are softer and reduce aliasing.


Transparent
===========

Render the background transparent, for compositing the image over another background after rendering.

Transparent Glass
   Render transmissive surfaces as transparent, for compositing glass over another background.
Transparent Roughness
   For transparent glass, keep surfaces with roughness above the threshold opaque.

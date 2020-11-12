.. _bpy.types.CompositorNodeLensdist:

********************
Lens Distortion Node
********************

.. figure:: /images/compositing_node-types_CompositorNodeLensdist.png
   :align: right

   Lens Distortion Node.

Use this node to simulate distortions that real camera lenses produce.


Inputs
======

Image
   Standard image input.
Distort
   This creates a bulging or pinching effect from the center of the image.
Dispersion
   This simulates chromatic aberrations, where different wavelengths of light refract slightly differently,
   creating a rainbow colored fringe.


Properties
==========

Projector
   Enable or disable slider projection mode.
   When on, distortion is only applied horizontally. Disables *Jitter* and *Fit*.
Jitter
   Adds jitter to the distortion. Faster, but noisier.
Fit
   Scales image so black areas are not visible. Only works for positive distortion.


Outputs
=======

Image
   Standard image output.

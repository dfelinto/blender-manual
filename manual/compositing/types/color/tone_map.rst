.. _bpy.types.CompositorNodeTonemap:

*************
Tone Map Node
*************

.. figure:: /images/compositing_node-types_CompositorNodeTonemap.png
   :align: right

   Tone Map Node.

Tone mapping is a technique used in image processing and computer graphics to map one set of
colors to another in order to approximate the appearance of high dynamic range images
in a medium that has a more limited dynamic range.

Essentially, tone mapping addresses the problem of strong contrast reduction from the scene values
(radiance) to the displayable range, while preserving the image details and color appearance.
This is important to appreciate the original scene content.


Inputs
======

Image
   :abbr:`HDR (High Dynamic Range)` image.


Properties
==========

Type
   Rh Simple
      Key
         The value the average luminance is mapped to.
      Offset
         Normally always 1, but can be used as an extra control to alter the brightness curve.
      Gamma
         If not used, set to 1.

   R/D Photoreceptor
      Intensity
         If less than zero, darkens image; otherwise, makes it brighter.
      Contrast
         Set to 0 to use estimate from input image.
      Adaptation
         If 0, global; if 1, based on pixel intensity.
      Color Correction
         If 0, same for all channels; if 1, each independent.


Outputs
=======

Image
   :abbr:`LDR (Low Dynamic Range)` image.

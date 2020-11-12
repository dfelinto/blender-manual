
****
Mask
****

.. figure:: /images/sculpt-paint_texture-paint_tool-settings_mask_panel.png
   :align: right

   Mask settings.


.. _bpy.types.ImagePaint.stencil:

Stencil Mask
============

The mask can be deactivated by the checkbox in the header.

Stencil Image
   Image used as a mask. See :ref:`ui-data-block`.
UV Layer
   Allows you to select the UV layer for the mask image.
Display Color
   Mask color in the viewport. See :ref:`ui-color-picker`.

   Invert Stencil (black/white icon)
      Inverts the mask.


.. _bpy.types.Paint.use_cavity:

Cavity Mask
===========

Cavity masking means that the brush will be masked if there is a cavity or a hill
on the mesh surface depending on the mesh options. The cavity algorithm is vertex-based.

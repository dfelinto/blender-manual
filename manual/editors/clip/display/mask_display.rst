
************
Mask Display
************

This popover controls mask display options.

.. _bpy.types.SpaceClipEditor.show_mask_spline:

Spline
   Toggles the display of the mask splines.
   This option is useful while combined with the *Overlay* option below to see a simplified view of the mask.
   Note the splines must be enabled to select and edit the spline points.

   .. _bpy.types.SpaceClipEditor.mask_display_type:

   Edge Display Type
      Style of the edge.

.. _bpy.types.SpaceClipEditor.show_mask_overlay:

Overlay
   Added mask overlay to both Image and Clip editors.

   .. _bpy.types.SpaceClipEditor.mask_overlay_mode:

   Overlay Mode
      :Alpha Channel:
         Which displays the rasterized mask as a grayscale image.
      :Combined:
         Displays both the clip along with the mask overlayed on top.

.. _bpy.types.SpaceClipEditor.blend_factor:

Blending Factor
   How much the clip is mixed with the grayscale mask representation when using "Combined" *Overlay Mode*.

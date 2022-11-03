.. _bpy.types.BrushTextureSlot.mask:

************
Texture Mask
************

With a Texture Mask the brush strength is masked by a texture.

Texture
   In paint modes the texture is used as a color source,
   while for sculpting it is used to determine the strength of the brush.

.. _bpy.types.BrushTextureSlot.mask_map_mode:

Mask Mapping
   Sets the way the texture is applied to the brush stroke.

   :View Plane:
      If *View Plane* is enabled, the current view angle is used to project the brush texture onto the model.
      I.e. the texture follows the mouse, so it appears that the texture is being dragged across the model.
      In 2D painting, the texture moves with the brush.
   :Tiled:
      The *Tile* option tiles the texture across the screen,
      so moving the brush appears to move separately from the texture.
      The *Tile* option is most useful with tileable images, rather than procedural textures.
   :Random:
      Picks a random texture coordinate to sample from for each dab.
   :Stencil:
      Stencil mapping works by projecting the paint from the camera space on the mesh or canvas.
      Painting is applied only inside the boundaries of the stencil.
      The stencil is displayed as a screen space overlay on the viewport.
      To the transform the stencil texture and the stencil mask with additional :kbd:`Alt` pressed:

      - Move :kbd:`RMB`
      - Scale :kbd:`Shift-RMB`
      - Rotate :kbd:`Ctrl-RMB`

      When using stencil scaling, :kbd:`X` and :kbd:`Y` are used to constrain the scaling to one axis.
      Pressing one of the buttons twice reverts to unconstrained scaling.

      Image Aspect
         Restore the aspect ratio of the original image to reset stretching introduce by scaling,
         (Image textures only.) This operator can use the tiling and scale values of the brush texture
         if the relevant are enabled in :ref:`bpy.ops.screen.redo_last` panel.
      Reset Transform
         Restores the position of the stencil.

.. _bpy.types.Brush.use_pressure_masking:

Pressure Masking
   A mask cut-off function. It allows to clip the mask result based on pressure,
   creating areas of no paint when low pressure is applied to the brush,
   similar to how a real brush would behave.

   :Off: Deactivated.
   :Ramp: Distributes the mask effect above the pressure value.
   :Cutoff: Simply selects between zero and one based on stylus pressure.

Angle
   This is the rotation angle of the texture brush.
Rake
   Angle follows the direction of the brush stroke.
Random
   Angle is randomized per dab.

   Random Angle
      Constraints the random deviation to a range.
Offset X, Y, Z
   Offset the texture map placement in X, Y, and Z axes.
Size X, Y, Z
   Set the scale of the texture in each axis. Not available for *Drag* sculpting textures.

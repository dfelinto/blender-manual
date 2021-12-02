.. _bpy.types.MaterialLineArt:

********
Line Art
********

.. reference::

   :Panel:     :menuselection:`Material --> Line Art`

.. figure:: /images/render_materials_line-art_panel.png
   :align: right

   Line Art material properties.

.. _bpy.types.MaterialLineArt.use_material_mask:

Material Mask
   Material masks provide line art a way to record extra information about faces
   that caused the occlusion, so edges occluded by those faces can be selected to have different styles.

.. _bpy.types.MaterialLineArt.use_material_mask_bits:

Masks
   The layer to to include faces of the current material.

.. _bpy.types.MaterialLineArt.mat_occlusion:

Levels
   Faces with this material will behave as if it has set number of layers in occlusion.

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
   Material masks are a way to provide Line Art extra information about faces that caused the occlusion.
   So edges occluded by those faces can be selected to have different styles.

.. _bpy.types.MaterialLineArt.use_material_mask_bits:

Masks
   The layer to include faces of the current material.

.. _bpy.types.MaterialLineArt.mat_occlusion:

Levels
   Faces with this material will behave as if it has set number of layers in occlusion.
